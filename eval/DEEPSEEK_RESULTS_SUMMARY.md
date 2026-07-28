# DeepSeek v3.1 评审实验结果汇总

统计截止:2026-07-26。覆盖目前所有跑过 `deepseek/deepseek-chat-v3.1`(经 OpenRouter)的实验批次:15 篇集(cond1-6)、60 篇集(cond1-5)、以及新增的 cond7(RAG + 3轮迭代 + 作者反驳,在 30 篇集和 60 篇集上都跑完),另外加了外部系统 PaperReviewer.ai 在同一 ground truth 子集上的成绩作对照,以及 **`anthropic/claude-haiku-4.5` 在 60 篇集上跑的 cond1(基线)和 cond7(RAG+作者反驳)两个条件**(标题虽然还叫"DeepSeek"但本文档已经扩展到跨模型对比)。**cond7 的两次 DeepSeek 跑(30篇集、60篇集)现在都已经把 JSON 解析失败的论文重跑修复,是干净的全量数据(30/30、60/60);Haiku 4.5 的两次跑(cond1、cond7)都是一次过、0 解析失败。**

评测方法统一用 `eval/evaluation.py`:对每篇论文的生成 review 与 OpenReview 真实评审做比较,核心指标:

- **decision_accuracy**:accept/reject 判断是否与真实决议一致
- **score_spearman_rho**:生成打分(归一化到 [0,1])与真实平均分的 Spearman 相关系数
- **src_overall_mean**(Semantic Review Coverage):生成的 strengths/weaknesses 在语义上覆盖真实评审要点的程度(strengths 和 weaknesses 两个子分数的均值)

## 条件定义(`eval/experiment.py::CONDITIONS`)

| ID | label | RAG | n_iter | reviewer | 作者反驳 | AI Detector | 说明 |
|----|-------|-----|--------|----------|----------|--------------|------|
| 1 | no_rag_1iter_1rev | ✗ | 1 | 中立×1 | (n_iter=1 时无效) | ✗ | 基线 |
| 2 | rag_1iter_1rev | ✓(实时检索) | 1 | 中立×1 | (无效) | ✗ | 相关工作 RAG 的效果 |
| 3 | no_rag_2iter_aidetect_noauthor | ✗ | 2 | 中立×1 | ✗ | ✓ | AI Detector 实验组 |
| 4 | no_rag_3iter_author | ✗ | 3 | 中立×1 | ✓ | ✗ | 作者反驳(3轮)效果 |
| 5 | no_rag_1iter_3rev | ✗ | 1 | persona×3(A/B/C) | (无效) | ✗ | 多 persona 集成 vs 单评审 |
| 6 | no_rag_2iter_noaidetect_noauthor | ✗ | 2 | 中立×1 | ✗ | ✗ | cond3 的对照组 |
| 7 | rag_3iter_author | ✓(**本地缓存**) | 3 | 中立×1 | ✓ | ✗ | RAG + 作者反驳的组合效果 |

cond7 与 cond4 的差异**只有** RAG 开关,因此 `(cond7 - cond4)` 理论上应能分离出"在有作者反驳/多轮迭代基础上,再叠加相关工作 RAG"的增量效果。cond7 分别用 `--rag_cache eval/related_work_rag_30.json`(30篇集)和 `--rag_cache eval/related_work_rag_60.json`(60篇集)两份本地预建缓存跑,不再实时调用 OpenAlex/arXiv,只有 LLM 调用开销。60篇集的相关工作检索用了并发版的 `scripts/build_related_work_rag_30.py --concurrency 8`(脚本已通用化,不止服务 30 篇集),约 4 分钟建完缓存(顺序执行版本预估要 ~1 小时)。

PaperReviewer.ai 的结果来自已有的 `eval/paperreviewer_300.json`(300篇批量跑过的结果),与 15 篇 ground truth 有 14 篇重叠,不是本 session 新跑的,只是拿来对照。

## 结果一览

### 15 篇集(`eval/openreview_15_conf3.json` 作为 ground truth)

| 系统 | n | decision_accuracy | 正确/总数 | spearman ρ | p | SRC_strengths | SRC_weaknesses | SRC_overall |
|---|---|---|---|---|---|---|---|---|
| cond1(基线) | 15 | 0.600 | 9/15 | 0.558 | 0.031 | 0.398 | 0.267 | 0.333 |
| cond2(RAG,实时)⚠️无效 | 15 | 0.533 | 8/15 | 0.576 | 0.025 | 0.402 | 0.262 | 0.332 |
| cond3(+AI Detector) | 15 | 0.600 | 9/15 | 0.477 | 0.072 | 0.399 | 0.257 | 0.328 |
| cond4(作者反驳×3轮) | 15 | 0.667 | 10/15 | 0.538 | 0.038 | 0.398 | 0.242 | 0.320 |
| cond5(3-persona) | 15 | 0.600 | 9/15 | 0.353 | 0.197 | 0.475 | 0.333 | 0.404 |
| cond6(Detector对照组) | 15 | 0.600 | 9/15 | 0.471 | 0.076 | 0.402 | 0.265 | 0.333 |
| **cond7(RAG本地缓存+作者反驳×3轮)** | **15** | **0.867** | 13/15 | **0.839** | 0.0001 | 0.401 | 0.277 | 0.339 |
| PaperReviewer.ai(外部系统,参考) | 14\*\* | 0.750\*\* | 3/4 | 0.800\* | 0.2 | 0.459 | 0.390 | 0.425 |

\* PaperReviewer.ai 的 spearman 只算出了 n=4(它给出可比打分的论文很少),p=0.2 完全不显著,这一项**不能**当真实相关性看,只放出来存档。
\*\* SRC 的 n=14(所有重叠论文都算),但 decision_accuracy 的有效样本其实只有 **4** 篇(14篇里有10篇 `accept_or_not` 字段缺失、判不了 accept/reject,evaluation.py 会把这些记成 None 并从准确率分母里剔除)——0.750 是 3/4 而不是看起来的"14篇里对了大部分",几乎没有统计意义,详见下方注意事项。

### 60 篇集(`eval/openreview_60_module_test.json` 作为 ground truth)

| 系统 | n | decision_accuracy | 正确/总数 | spearman ρ | SRC_strengths | SRC_weaknesses | SRC_overall |
|---|---|---|---|---|---|---|---|
| cond1(基线) | 60 | 0.600 | 36/60 | 0.604 | 0.408 | 0.279 | 0.343 |
| cond2(RAG,实时)⚠️无效 | 60 | 0.617 | 37/60 | 0.556 | 0.405 | 0.279 | 0.342 |
| cond3(+AI Detector) | 60 | 0.583 | 35/60 | 0.515 | 0.401 | 0.279 | 0.340 |
| cond4(作者反驳×3轮) | 60 | 0.617 | 37/60 | 0.530 | 0.412 | 0.262 | 0.337 |
| cond5(3-persona) | 60 | 0.517 | 31/60 | 0.510 | 0.484 | 0.345 | 0.414 |
| **cond7(RAG本地缓存+作者反驳×3轮,DeepSeek v3.1)** | **60** | **0.683** | 41/60 | **0.527** | 0.396 | 0.276 | 0.336 |
| **cond1(基线,换成 Claude Haiku 4.5)** | **60** | **0.900** | 54/60 | **0.733**(p<0.0001) | 0.412 | 0.350 | 0.381 |
| **cond7(RAG+作者反驳×3轮,Claude Haiku 4.5)** | **60** | **0.900** | 54/60 | **0.750**(p<0.0001) | 0.413 | 0.324 | 0.368 |
| PaperReviewer.ai(外部系统,参考) | 55\*\* | 0.737\*\* | 14/19 | 0.631(p=0.004,n=19) | 0.458 | 0.390 | 0.424 |

\*\* 和 15 篇集一样,SRC 用的是全部 55 篇重叠论文,但 decision_accuracy / spearman 的有效样本只有 **19** 篇(55篇里36篇 `accept_or_not` 缺失、判不了决议)。这次 n=19 比 15篇集的 n=4 好得多,p=0.004 也显著,是相对更可信的一次对照,但仍然只覆盖了三分之一的重叠论文。

## 图表

- `eval/eval_results/plot_deepseek_conditions.png` —— 左图 15 篇集(DeepSeek cond1-6 + cond7 + PaperReviewer.ai),右图 60 篇集(DeepSeek cond1-5 + cond7 + **Haiku 4.5 cond7** + PaperReviewer.ai),每图三组柱状(decision_accuracy / spearman ρ / SRC_overall)。
- `eval/eval_results/plot_cond7_per_paper.png` —— cond7(DeepSeek,30篇集/15篇评测子集)逐篇 SRC_overall,绿色=决议判断正确,红色=判断错误(n=15,全量)。
- `eval/eval_results/plot_cond7_60_per_paper.png` —— cond7(DeepSeek,60篇集)逐篇 SRC_overall,同样绿/红配色(n=60,全量)。
- `eval/eval_results/plot_cond7_haiku45_60_per_paper.png` —— cond7(**Haiku 4.5**,60篇集)逐篇 SRC_overall,同样绿/红配色(n=60,0篇解析失败)。

## 关键观察

1. **cond7 修复到全量后,15篇集的提升反而更大了**:decision_accuracy 从之前部分数据(n=12)的 0.833 涨到 0.867(13/15),spearman ρ 从 0.823 涨到 0.839。说明之前被剔除的那 3 篇不是"拖后腿"的难例——修复后的完整数据依然支持"RAG+作者反驳"在这个小数据集上效果最好的结论,不是因为丢样本造成的假象。
2. **但 60 篇集(n=60,同样全量修复)的提升幅度远小于 15 篇集**:decision_accuracy 0.683 vs cond4 的 0.617(约7个点),spearman ρ 0.527 vs cond4 的 0.530(几乎没变)。两个数据集在样本量对齐、都是干净全量数据的情况下,**结论依然不一致**——15篇集显示 RAG+作者反驳有大幅提升,60篇集显示提升很小甚至持平。这说明 15 篇集(n=15)本身样本量太小,不能作为可靠结论来源,60 篇集(n=60)更值得信任。
3. **cond7 vs PaperReviewer.ai,60篇集(更可信的对照)上 PaperReviewer.ai 三项指标都超过 cond7(DeepSeek v3.1)**:decision_accuracy 0.737 vs 0.683,spearman ρ 0.631(p=0.004,n=19)vs 0.527,SRC_overall 0.424 vs 0.336。60篇集上 PaperReviewer.ai 的有效样本(n=19)比15篇集(n=4)大得多、且显著,是相对靠谱的一次比较。15篇集上看起来 cond7(DeepSeek)反超(0.867 vs 0.750)其实是被 PaperReviewer.ai 那边只有 4 个可判定样本的假象带偏了,不能作为"我们的系统更好"的证据。
4. **换成 Claude Haiku 4.5 之后,decision_accuracy 和 spearman ρ 反超 PaperReviewer.ai,但这个提升几乎全部来自换模型本身,和 RAG+作者反驳这个 pipeline 没什么关系**:补跑了 Haiku 4.5 的 cond1(无RAG基线,1轮,同一批 60 篇论文)后发现,cond1 和 cond7 在 Haiku 4.5 上的结果几乎一模一样——decision_accuracy 都是 **0.900**(都是 54/60,连正确论文的数目都完全相同),spearman ρ 分别是 0.733(cond1)和 0.750(cond7),SRC_overall 分别是 0.381(cond1)和 0.368(cond7,反而略低)。也就是说 **cond7 相比 cond1 在 Haiku 4.5 上没有带来任何看得出的净提升**,RAG+3轮迭代+作者反驳这套组合在这个模型上是"无功也无过"。之前(见修复前的注意事项)猜测"提升可能大部分来自模型基础能力"的担忧被证实是对的:两个 Haiku 4.5 条件都明显超过 DeepSeek v3.1 的对应条件(cond1: 0.900 vs DeepSeek cond1 的 0.600;cond7: 0.900 vs DeepSeek cond7 的 0.683),差距主要来自**换模型**,不是这次新加的 RAG/迭代/反驳设计。
5. **Haiku 4.5 一次跑就 0 个 JSON 解析失败**(DeepSeek v3.1 首次跑在这两个数据集上分别有 10%~23%、20% 的失败率),侧面说明 DeepSeek v3.1 的输出格式稳定性明显不如 Haiku 4.5,这本身也是一个值得记录的模型差异,不只是效果分数的问题。
6. **PaperReviewer.ai 的 SRC_overall 在 DeepSeek 条件里全场最高**(15p: 0.425;60p: 0.424,包括有指标伪影加成的 cond5),但 Haiku 4.5 的 cond7(0.368)已经把差距明显缩小了。这可能是因为它给出的 strengths/weaknesses 条目本身更丰富、更贴近真实评审的表述习惯,也可能是我们的 reviewer prompt 生成的条目数普遍偏少(固定在3条strengths+2-3条weaknesses左右)——具体原因需要进一步核实,不是本次实验直接验证的。
7. **cond2(相关工作 RAG,实时检索)在 15 篇集和 60 篇集上都被标记为无效**:15 篇集 13/15 篇 `num_used=0`,60 篇集 20/60 篇 `num_used=0`——高并发下 OpenAlex/arXiv 被限流,实际没有注入证据。这两行数据基本等价于"多包了一层无效 RAG 调用的 cond1",**不能**用来评估相关工作 RAG 的真实效果。
8. **cond7 用本地预建的 RAG 缓存彻底绕开了 cond2 的限流问题**——15篇评测子集里只有2篇 `num_used=0`;60篇集里有12篇(20%)`num_used=0`,其余80%都有真实相关工作证据注入,比 cond2 的实时检索干净得多(Haiku 4.5 那次跑用的是同一份 60 篇集 RAG 缓存,`num_used=0` 的比例完全一样,差异纯粹来自模型)。
9. **cond5(3-persona)的 SRC 虚高是已知的指标伪影**:3 个评审各写一份 strengths/weaknesses,条目数是其它条件的 ~3 倍,SRC 是纯 recall 指标,天然分数更高(15p: 0.404,60p: 0.414,两个数据集里都是所有条件里最高),但 decision_accuracy 和 spearman ρ 并未同步提升(15p 上 ρ=0.353 反而最低)。
10. **AI Detector(cond3 vs cond6)测不出效果**:两个 15 篇集条件的 decision_accuracy 完全相同(0.600=0.600),spearman ρ 也很接近(0.477 vs 0.471)。

## 注意事项 / 局限性

- **cond7 的两次跑最初都有明显的 JSON 解析失败**:30篇集(15篇评测子集)最初 3/15 失败,60篇集最初 12/60(20%)失败。修复方法都是:删掉失败结果文件、用同一条命令重跑(`eval/experiment.py` 的 `_existing_result_path` 逻辑会自动跳过已存在且可读的结果,只重算缺失的),多数一次修好,极少数(30篇集里的 `icml_reject_2025_003`)反复失败了 2 次才在第 3 次单独重跑(`--concurrency 1`)时修好。**现在两个数据集都是 100% 干净的全量数据**(30/30、60/60)。
- 60篇集初次失败率(20%)明显高于30篇集(10%~23%,取决于怎么算),原始失败日志已被覆盖,无法回溯具体报错原因;可能与 3轮迭代+作者反驳的长上下文更容易让 DeepSeek v3.1 输出格式跑偏有关,但没有直接证据,只是猜测,值得后续用固定 seed / 保留失败原始输出的方式专门排查。
- **`num_used=0` 与 JSON 解析失败是两回事**:60篇集里两个原始失败集合(12篇 parse_error、12篇 num_used=0)当时只有2篇重叠,说明检索证据缺失和输出解析失败是独立的两种失效模式,不要混为一谈。60篇集里仍有12篇(20%)`num_used=0`(RAG开了但没有可用证据),这会稀释"RAG确实带来提升"的信号。
- **cond2(两个数据集)已知因并发限流失效**,不能作为"相关工作 RAG 有没有用"的证据来源;真正干净的 RAG 对照应该看 cond7,或者以后用同样的"本地缓存 + enable_rag"方式重新产出一份 cond2 数据(1轮迭代版本,和 cond1 严格对照,而不是像 cond7 这样同时改了作者反驳)。
- **15 篇集与 60 篇集不是同一批论文的子集/超集关系之外没有其它可比性保证**:cond1-6 的两个数据集规模不同、论文也不完全重合,只能分别看趋势,不要跨集合直接比较绝对数值。
- **decision_accuracy 在 15 篇集上样本量依然很小(n=15)**,即便现在是全量干净数据,单篇翻转也能让准确率变化 ±6~7 个百分点——这正是关键观察2里"15篇集和60篇集结论不一致"的根本原因,遇到分歧时应优先信任 60 篇集(n=60)。
- **spearman ρ 在小样本下对异常值敏感**:15篇集 cond7 的 p=0.0001 数字上很显著,但结合观察2(60篇集增量小得多)来看,不宜单独用15篇集的结果下"RAG+作者反驳效果很好"的结论。
- **PaperReviewer.ai 的对照仅供参考**:它的结果不是本次实验设计里受控生成的(不同的系统/流程/可能不同的底层模型),来自已有的 `eval/paperreviewer_300.json`(300篇批量结果),不是本次新跑的。
- **PaperReviewer.ai 的 decision_accuracy 有效样本远小于表面的 n**:它给出的 `accept_or_not` 字段大量缺失(15篇集14篇里10篇缺失,60篇集55篇里36篇缺失),`evaluation.py` 会把无法判定的记成 `None` 并从准确率分母里剔除——15篇集的"0.750"其实只是 3/4,统计意义几乎为零;60篇集的"0.737"是 14/19,好一些但仍只覆盖三分之一重叠论文。SRC 指标不受这个影响(它不需要decision),n=14/n=55 是真实的。
- **60篇集是 PaperReviewer.ai 对比更可信的版本**:n=19(vs 15篇集的n=4)、p=0.004 显著,而且60篇集上 PaperReviewer.ai 在全部三项指标(decision_accuracy、spearman ρ、SRC_overall)上都超过了我们所有的 DeepSeek 条件,包括 cond7。15篇集上 cond7 表面反超是小样本假象,不能作为"我们更好"的依据。
- **Haiku 4.5 目前跑了 cond1 和 cond7 两个条件(60篇集),cond2-6 还没跑**,所以"cond7 相比 cond1 没有净提升"这个结论目前只是两个点的比较,不是完整的条件消融;不能排除 cond2(RAG单独)、cond3-6(迭代/Detector/persona 单独)在 Haiku 4.5 上有不同的效果模式,只是这两个点(cond1、cond7)恰好非常接近。
- 15 篇集 / 60 篇集 cond1-6 实验都只用了 DeepSeek v3.1;60篇集上 cond1 和 cond7 现在同时有 DeepSeek v3.1 和 Claude Haiku 4.5 两个模型的数据,30篇集的 cond7 只有 DeepSeek v3.1。跨模型对比(如 GPT-4o-mini)另见 `eval/EXPERIMENT_DESIGN_AND_RESULTS.md`,本文档聚焦 DeepSeek + Haiku 4.5(以及作对照的 PaperReviewer.ai)。
