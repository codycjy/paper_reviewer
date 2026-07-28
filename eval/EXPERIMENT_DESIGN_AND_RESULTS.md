# AI 论文评审 Pipeline — 实验设计与结果矩阵

> 生成时间：2026-07-25。本文档汇总当前分支（`feat/eval-data`，已 rebase 到 `origin/main`）上的完整实验方案、数据集、跑过的条件矩阵，以及每份结果的有效性说明。**代码已提交，结果数据文件尚未提交**（按要求）。

---

## 1. 系统架构

```
mas_loop.py (主循环)
├── RAG 证据构建（可选，rag/orchestrator.py）
│   ├── 阶段一：Related-work RAG（相关工作检索）
│   │   ├── 检索源：arXiv / OpenAlex / Semantic Scholar
│   │   ├── LLM 生成检索 query → 三源并行检索 → LLM 重排（rerank）
│   │   └── 输出：background summary + cutoff_report（按 cutoff_date 过滤 + 排除目标论文自身）
│   └── 阶段二：Review-memory RAG（历史评审校准，可选，默认关闭）
│       ├── 对 rerank 后排名靠前的相关论文，去 OpenReview 查真实官方评审
│       └── LLM 汇总为「decision pattern / score range / common strengths & weaknesses」校准上下文
├── Reviewer Agent(s)：reviewer_nopersona（中立单评审）或 reviewer_a/b/c（三种 persona）
├── AI Author（作者反驳，n_iter > 1 时逐轮响应评审意见）
├── AI Detector（可选，检测评审文本是否像 AI 生成，注入下一轮评审的参考信息）
└── Conference Recommender（会议录用建议）
```

每篇论文的输出现在包含 `iterations` 字段（本次 session 新增），完整记录每一轮的 review / author_response / ai_detector_response，使 AI Detector 的实际效果可以事后追溯，而不只是看最终一轮结果。

---

## 2. 实验条件矩阵（`eval/experiment.py::CONDITIONS`）

7 个条件，两两对照可以分离出 4 个独立变量的效应：

| ID | label | n_iter | reviewer | RAG(相关工作) | RAG(评审记忆) | AI Detector | 作者反驳 | 用途 |
|----|-------|--------|----------|:---:|:---:|:---:|:---:|------|
| 1 | no_rag_1iter_1rev | 1 | 中立×1 | ✗ | ✗ | ✗ | (n_iter=1 时无效) | **基线** |
| 2 | rag_1iter_1rev | 1 | 中立×1 | ✓ | ✗ | ✗ | (无效) | 相关工作 RAG 的效果 |
| 3 | no_rag_2iter_aidetect_noauthor | 2 | 中立×1 | ✗ | ✗ | ✓ | ✗ | AI Detector 效果（实验组） |
| 4 | no_rag_3iter_author | 3 | 中立×1 | ✗ | ✗ | ✗ | ✓ | 作者反驳的效果（3 轮） |
| 5 | no_rag_1iter_3rev | 1 | persona×3 (A/B/C) | ✗ | ✗ | ✗ | (无效) | 多 persona 集成 vs 单评审 |
| 6 | no_rag_2iter_noaidetect_noauthor | 2 | 中立×1 | ✗ | ✗ | ✗ | ✗ | AI Detector 的**对照组**（本次新增） |
| 7 | rag_reviewmem_1iter_1rev | 1 | 中立×1 | ✓ | ✓ | ✗ | (无效) | 评审记忆 RAG 的增量效果（本次新增） |

**隔离逻辑**（差分对照）：
- `(3 − 6)`：条件相同（2 轮、无作者反驳），唯一差异是 AI Detector 开关 → 分离出 Detector 的净效应
- `(6 − 1)`：条件相同（都无 Detector），唯一差异是多一轮迭代 → 分离出「多一轮但无额外信号」本身的效应（用来确认 3 vs 1 的差异是 Detector 带来的还是单纯多轮带来的）
- `(7 − 2)`：条件相同（都是相关工作 RAG），唯一差异是评审记忆 RAG 开关 → 分离出第二个 RAG 的增量效应
- `(5 − 1)`：分离出「3 个 persona 投票/综合」vs 单一中立评审的效应

---

## 2.1 每个方案具体做了什么

以下按机制展开，涉及的具体代码路径都标出来，方便核对。

### 条件 1 — 基线（no_rag_1iter_1rev）

单个 `reviewer_nopersona` agent，只读一遍论文全文，直接产出一份 review（分数 + strengths + weaknesses + 决策建议），无任何外部证据、无第二轮、无作者互动。这是所有其他条件的对照零点。

`reviewer_nopersona` 的 persona（`prompts/reviewer_nopersona.py`）只有一句「You are a paper reviewer」，不带任何风格倾向，共享 `prompts/reviewer_common.py` 里定义的统一评审标准（`TASK`、`EVAL_CRIT` 评分维度、输出 JSON 格式）。

### 条件 2 — 相关工作 RAG（rag_1iter_1rev）

在条件 1 的基础上，评审开始前先跑一遍 `rag/orchestrator.py::build_rag_package()` 的**阶段一**：

1. 用 LLM 读论文摘要/引言，生成若干条检索 query（按「方法」「问题设定」「实验对比」等维度分组）
2. 三个检索源（arXiv / OpenAlex / Semantic Scholar）并行搜索，返回候选相关论文列表
3. 按 `cutoff_date`（默认 2024-12-31）过滤掉晚于截止日期的论文，避免用「未来」文献泄漏信息；同时排除论文自身（`num_removed_as_target`）
4. LLM 对候选做 rerank，选出最相关的一批
5. LLM 把这批论文的标题/摘要/关系汇总成一段「相关工作背景」（background summary），拼进 reviewer 的 prompt

评审 agent 因此在写 review 前，多了一段「这篇论文相对于已有工作的定位」的背景信息，理论上应该能帮它更准确判断 novelty，也更容易发现「这其实是重复工作」之类的问题。**注意**：本次 15-paper 和 60-paper 的 deepseek cond2 数据因检索被限流打空而失效（见 §6），gpt-4o-mini 的 60-paper cond2 是唯一验证过的有效样本。

### 条件 3 — AI Detector 消融·实验组（no_rag_2iter_aidetect_noauthor）

2 轮迭代，`enable_ai_detector=True`，`enable_author_rebuttal=False`。具体时序（`mas_loop.py:253-287`）：

1. **第 1 轮**：reviewer 正常产出初稿 review（同条件 1）
2. **第 2 轮前**：`AIDetector` agent（`prompts/ai_detector.py`）读取第 1 轮的 review 文本，从 5 个维度（具体性/推理深度/句式变化/批判的真实感/…）打一个 1-10 的「像不像人写的」分数，并给出改进建议；同时因为 `enable_author_rebuttal=False`，作者位置被填充一句占位符「(No rebuttal was submitted for this iteration.)」而不产出真实反驳
3. **第 2 轮**：reviewer 收到 `###AUTHOR_RESPONSE###`（占位符）+ `###AICHECKER_RESPONSE###`（Detector 的完整点评），被要求参考这些信息重新给出一份 review

设计意图：观察「被人告知你的评审看起来太像 AI 写的」是否会让 reviewer agent 主动把评审写得更具体、更有变化、更「像人」——间接也可能影响它的判断质量。**结果：完全没有观察到效应**，15 篇论文里第 2 轮相对第 1 轮的分数变化是 0/15（详见 §6.1）。

### 条件 4 — 作者反驳（no_rag_3iter_author）

3 轮迭代，`enable_author_rebuttal=True`，`enable_ai_detector=False`。这是唯一真正跑「审稿-反驳-再审」全流程的条件：

1. **第 1 轮**：reviewer 产出初稿 review
2. **第 2 轮前**：`Author` agent（`prompts/author.py`，被 prompt 成「不情绪化、策略性、证据驱动」的作者人格）针对每条 reviewer 意见逐条回应：判断是否合理 → 若合理就承认限制并说明后续可行的缓解方式，若不合理就用论文里的证据反驳
3. **第 2 轮**：reviewer 读到作者的回应，更新 review（可能改分）
4. **第 3 轮前**：作者再针对第 2 轮的新意见回应一次
5. **第 3 轮**：reviewer 做最终 review，这轮的结果就是 `final_reviews`

设计意图：模拟真实同行评审的 rebuttal 阶段，看模型是否会被有理有据的反驳说服而改变判断（这是正向能力）还是无差别地被「态度好」说服而无脑抬分（这是需要警惕的失败模式）。目前观察（deepseek/haiku 均如此）：分数普遍上移但 decision_accuracy 没有同步提升，需要结合具体案例判断是「合理采纳」还是「态度打分」。

### 条件 5 — 三 Persona 评审（no_rag_1iter_3rev）

不是条件 1 跑 3 次取平均，而是**三个不同倾向的 agent 各自独立审一遍**，各自产出完整 review（各自的分数、strengths、weaknesses），最后一起喂给 Conference Recommender 做综合会议推荐：

- `reviewer_a`（"Senior Researcher"）：偏好 **Novelty**，方法论小瑕疵可以容忍，只要核心想法够新
- `reviewer_b`（"Young Professor"）：偏好 **Soundness**，逻辑/数学/实验的严谨性是硬指标，novelty 不够但做得扎实也能接受
- `reviewer_c`（"Experienced Practitioner"）：偏好 **Significance + Clarity**，看重实际可用性、可复现性、诚实讨论局限性

设计意图：模拟真实会议「3 个评审各有侧重」的评审委员会效果，理论上应该比单一中立视角更全面。**实测：SRC_overall 明显更高，但这是指标伪影**（3 份 review 叠加导致 strengths/weaknesses 条数是其他条件的 ~3 倍，SRC 是纯 recall 指标）；decision_accuracy 和 Spearman ρ 并未同步提升，15-paper 上 ρ=0.353 反而是所有条件里最低且不显著。

### 条件 6 — AI Detector 消融·对照组（no_rag_2iter_noaidetect_noauthor，本次新增）

和条件 3 完全一样是 2 轮迭代、无作者反驳，**唯一区别是 `enable_ai_detector=False`**。第 2 轮前作者位置和 Detector 位置都是占位符/None，reviewer 在第 2 轮拿到的额外信息量为零，纯粹是被要求「再看一遍论文重新写一份 review」。

存在的意义：如果没有条件 6，就无法判断「条件 3 相对条件 1 的差异」到底是 Detector 反馈起了作用，还是仅仅「多看一遍论文/多一次机会」本身就会改变输出（LLM 采样的随机性、更长的上下文预热等）。有了条件 6 才能做 `(3−6)` 这个干净的差分。

### 条件 7 — 相关工作 + 评审记忆 RAG（rag_reviewmem_1iter_1rev，本次新增）

在条件 2 的基础上，`build_rag_package()` 多跑**阶段二**（`rag/review_memory.py`）：

1. 拿阶段一 rerank 后排名最高的相关论文候选列表
2. 对每个候选，先尝试从其 metadata 里直接抽取 OpenReview forum id（如果有 OpenReview URL），否则用论文标题去 OpenReview `/notes/search` 查找对应的评审论坛
3. 找到论坛后，拉取该论坛下所有 official review 类型的 note（用一堆启发式规则区分「这是不是一条正式评审」，排除作者回复、meta-review、决定通知等），过滤出公开可读的（`readers` 包含 "everyone"）
4. 把找到的第一个「有真实评审内容」的候选论文包装成一个 `ReviewMemoryCase`：包含该论文的历史 decision（accept/reject）、评分区间、每条评审的原文
5. LLM 把这个 case 总结成结构化的「校准上下文」：decision pattern、常见 strengths/weaknesses 模式、评分区间，明确标注「这是辅助校准信息，不是对目标论文的直接证据」
6. 这段总结连同阶段一的相关工作背景一起注入 reviewer 的 prompt

设计意图：让 reviewer 不仅知道「这篇论文和哪些工作相关」，还知道「和它相关的论文，历史上大概会被打几分、通常因为什么原因被拒/被收」，从而校准自己的评分尺度（比如避免对某个子领域普遍偏松或偏严）。**目前完全跑不通**：OpenReview 对匿名访问的 `/notes?forum=...` 返回 403，即便论文完全公开也一样，需要账号认证才能拉到评审内容（细节见 §6.4）。已验证的是排除目标论文自身评审的逻辑正确工作（不会泄漏 ground truth）。

### Conference Recommender（贯穿所有条件，不是独立方案）

每个条件跑完最后一轮评审后，都会额外跑一次 `ConferenceRecommender` agent（`prompts/conf_rec.py`），把所有 reviewer 的最终 review 喂给它，让它结合 ICLR/ICML/NeurIPS 的 Call for Papers 定位，判断这篇论文最适合投哪个会议、以及当前会议下的录用建议是否合理。这个不是被消融的自变量，而是所有条件共享的固定后处理步骤，其准确率反映在结果矩阵的 `conference_check_accuracy` 列（当前始终和 `decision_accuracy` 一样，因为评估脚本只在 accept/reject 判断本身一致时才认为 conference check 通过——这是评估方法的一个简化假设，不是模型真的在做会议匹配判断，值得注意但不在本次范围内深挖）。

---

## 3. 数据集

| 数据集 | 论文数 | 会议分布 | 用途 |
|---|---|---|---|
| `eval/papers.json`（及历史变体）| 300+ | 混合 | 早期大规模跑，历史遗留 |
| 60-paper 集（`exp_results_60_*`）| 60 | 未按会议均衡 | 上一阶段 5-条件对比（模型间比较） |
| **`eval/openreview_15_conf3.json`（本次新建）** | **15** | **ICLR/ICML/NeurIPS 各 5** | 本次 5×3×6 小实验主数据集，8 accept / 7 reject |

15 篇均已有本地 markdown（`data/md/`），来自 OpenReview 真实录用/拒稿论文，作为 ground truth。

---

## 4. 已跑过的模型

| 模型 | 接入方式 | 状态 |
|---|---|---|
| `deepseek/deepseek-chat-v3.1` | OpenRouter | 15-paper 全 6 条件已跑完；60-paper 5 条件已跑完 |
| `gpt-4o-mini-2024-07-18` | OpenRouter | 60-paper 5 条件已跑完 |
| `anthropic/claude-haiku-4.5` | OpenRouter | 15-paper 仅 cond1 + cond4（本次按你的要求抽样跑了「最可能出好结果」的 2 个条件） |
| cond7（review-memory RAG）| 任意模型 | **未产出有效结果**（见 §6，OpenReview 匿名访问被拒） |

---

## 5. 结果矩阵

### 5.1 主结果：15-paper × 3-conference（GT: 8 accept / 7 reject）

| system | dec_acc | 预测分布(accept/reject) | Spearman ρ | p | SRC_strength | SRC_weakness | SRC_overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| **haiku-4.5** cond1（基线） | **0.800** | 11/4 | **0.719** | 0.0025 | 0.423 | 0.327 | 0.375 |
| **haiku-4.5** cond4（作者反驳×3轮） | **0.800** | 11/4 | 0.714 | 0.0028 | 0.414 | 0.306 | 0.360 |
| deepseek cond1（基线） | 0.600 | 14/1 | 0.558 | 0.031 | 0.398 | 0.267 | 0.333 |
| deepseek cond2（相关工作RAG）⚠️无效 | 0.533 | 15/0 | 0.576 | 0.025 | 0.402 | 0.262 | 0.332 |
| deepseek cond3（+AI Detector） | 0.600 | 14/1 | 0.477 | 0.072 | 0.399 | 0.257 | 0.328 |
| deepseek cond4（作者反驳×3轮） | 0.667 | 13/2 | 0.538 | 0.038 | 0.398 | 0.242 | 0.320 |
| deepseek cond5（3-persona） | 0.600 | 14/1 | 0.353 | 0.197 | 0.475 | 0.333 | 0.404 |
| deepseek cond6（Detector对照组） | 0.600 | 14/1 | 0.471 | 0.076 | 0.402 | 0.265 | 0.333 |
| deepseek cond7（评审记忆RAG） | — | — | — | — | — | — | — | 未产出（见 §6） |
| 全预测 accept 基线 | 0.533 | 15/0 | — | — | — | — | — |

**⚠️ cond2（deepseek）标记无效**：15 篇里除 2 篇外全部 `num_used = 0`（RAG 检索因并发限流被 OpenAlex/arXiv 429/超时打空，实际未注入任何相关工作证据）。这份数据只是「和 cond1 几乎一样但多了一层无效的 RAG 调用」，**不能**用来评估相关工作 RAG 的真实效果。原始文件已移到 `eval/exp_results_15_conf3_deepseek/_invalid_rag_empty/`（未删除）。

### 5.2 对照：60-paper 集，gpt-4o-mini vs deepseek，5 条件（GT 未在此列出，见 eval_results 原文件）

| system | dec_acc | Spearman ρ | p | SRC_overall |
|---|---:|---:|---:|---:|
| gpt-4o-mini cond1 | 0.517 | 0.251 | 0.053 | 0.347 |
| gpt-4o-mini cond2（RAG，**有效**） | 0.517 | 0.454 | 0.0003 | 0.351 |
| gpt-4o-mini cond3（+Detector） | 0.517 | 0.123 | 0.350 | 0.343 |
| gpt-4o-mini cond4（作者反驳） | 0.517 | 0.085 | 0.518 | 0.339 |
| gpt-4o-mini cond5（3-persona） | 0.517 | 0.457 | 0.0002 | 0.423 |
| deepseek cond1 | 0.600 | 0.604 | <0.001 | 0.343 |
| deepseek cond2（RAG）⚠️无效同上 | 0.617 | 0.556 | <0.001 | 0.342 |
| deepseek cond3（+Detector） | 0.583 | 0.515 | <0.001 | 0.340 |
| deepseek cond4（作者反驳） | 0.617 | 0.530 | <0.001 | 0.337 |
| deepseek cond5（3-persona） | 0.517 | 0.510 | <0.001 | 0.414 |

这份 60-paper 的 deepseek cond2 同样被确认 `num_used = 0`（同一批并发限流问题），无效标记同上。**gpt-4o-mini 的 60-paper cond2 是本次审计中唯一确认有效的 RAG 数据**（跑于 07-23，早于那次并发限流事故，`num_used=12`），其 ρ 从 0.251（无RAG）提升到 0.454（+RAG），是目前唯一一份「RAG 确实带来提升」的干净证据，但用的是较弱的 gpt-4o-mini，且未与 cond7 对比。

---

## 6. 已知问题清单

1. **AI Detector（cond3 vs cond6）测不出效果**：decision_accuracy 完全相同（0.600 = 0.600），SRC_overall 只差 0.005。逐轮 trace 显示 15 篇论文里 **0 篇**在 Detector 介入后改变过 review 分数，尽管 Detector 平均给出 8.47/10 的高「AI 味」判断并附带约 1500 字批评——**评审 agent 根本没有对 Detector 的反馈做出任何反应**，这是当前 pipeline 的一个功能性缺口，不是评估方法的问题。

2. **cond5（3-persona）的 SRC 虚高是指标伪影**：cond5 生成的 strengths/weaknesses 条数是其他条件的 ~3 倍（3 个评审各自写一份），而 SRC 是纯 recall 指标，条数越多分数天然越高。60-paper 和 15-paper 两次独立跑都复现了这个模式（SRC_overall 0.40+ vs 其他条件 0.32~0.35），但 decision_accuracy 和 Spearman ρ 并未同步提升（15-paper 上 ρ=0.353 反而是所有条件里最低且不显著）——说明「写得多」不等于「判断得准」。

3. **cond2 数据（相关工作 RAG）大面积失效**：15-paper 和 60-paper 的 deepseek 跑法都撞上同一次事故——15 路并发同时打 OpenAlex/arXiv，触发了 IP 级限流，13/15（15-paper 集）RAG 检索拿到 0 篇论文。本次 session 已修复根因（见 §7），但**历史 cond2 数据尚未重新产出有效版本**。

4. **cond7（评审记忆 RAG）目前完全跑不通**，原因分两层：
   - 检索候选相关论文标题 → OpenReview `/notes/search` 有时返回 200 但 `searchUnavailable: true`（后端瞬时抖动，非速率限制），本次已修好重试逻辑；
   - 找到候选论坛后，实际拉取评审内容 `/notes?forum=...` **对匿名访问返回 HTTP 403**，即便是完全公开的论文也一样。用一个已知公开的 ICLR 论坛 ID 直接测试同样 403，说明这是 OpenReview API2 平台级的认证门槛，跟我们的 IP/并发无关。**需要 `OPENREVIEW_USERNAME`/`OPENREVIEW_PASSWORD`（或 `OPENREVIEW_ACCESS_TOKEN`）才能跑通**，代码里登录换 token 的逻辑已就绪，只是没有凭证。
   - 好消息：target-paper 排除逻辑验证有效（`cutoff_report.num_removed_as_target: 1`），确认不会把论文自己的 ground-truth review 泄漏进评审记忆证据里。

---

## 7. 本次 session 的基础设施修复

| 问题 | 修复 | commit |
|---|---|---|
| RAG 检索无重试，并发下大量请求静默失败（无证据注入却不报错） | `PaperSearchProvider._fetch` 加指数退避重试（Retry-After 感知） | `07ce9ca` |
| OpenAlex 被限流后，仍对剩余每个 query 组重复走满 4 次重试，一篇论文浪费几分钟 | 加熔断：单个 provider 实例首次遇到不可重试的限流错误后，直接短路后续请求 | `6f0d79a` |
| 抓取用代理会误把 OpenRouter 的 LLM 请求也代理出去 | 新增专用 `RAG_HTTP_PROXY` 环境变量，只作用于 RAG provider 的 HTTP fetch，与 LLM 客户端使用的 `HTTP_PROXY`/`HTTPS_PROXY` 完全隔离 | `e8eb84c` |
| OpenReview 搜索接口偶发 `searchUnavailable: true`（200 响应），旧代码把这个失败结果也写进缓存，导致重试直接读到同一个坏结果 | 加 `_should_cache` hook，`searchUnavailable` 响应不落盘缓存 | `e8eb84c` |
| AI Detector 效果不可追溯（只保留最后一轮评审） | `mas_loop.py` 返回值新增 `iterations` 字段，完整保留每轮 review/author_response/ai_detector_response | `9361c2d` |
| 旧测试硬编码两条件 A/B 设计，加条件 6/7 后全部失败 | 重写 `tests/test_run_review_experiment.py`，从 `CONDITIONS` 动态推导期望值 | `9361c2d` |

当前测试基线：198 passed，8 failed（8 个失败均为 rebase 前 `origin/main` 上已存在、与本次改动无关的失败，未引入新增回归）。

---

## 8. 待办 / 下一步

- [ ] 用修好的重试+熔断+代理，重新产出**有效的** cond2（相关工作 RAG）数据（deepseek，及可选 haiku-4.5）
- [ ] 决定是否注册 OpenReview 账号以解锁 cond7（评审记忆 RAG），有账号后重跑 `(7 − 2)` 对照
- [ ] 若继续用 haiku-4.5，补齐 cond2/3/5/6/7，与 deepseek 做完整 6/7 条件对比（目前 haiku 只有 cond1/cond4 两个点）
- [ ] 考虑给评审 agent 补一个「必须回应 AI Detector 反馈」的机制，再重新评估 cond3 vs cond6，验证问题 6-1 到底是 Detector 本身没用，还是没被 agent 采纳
