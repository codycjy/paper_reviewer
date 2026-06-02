# Models Know Their Shortcuts: Deployment-Time Shortcut Mitigation

## Jiayi Li, Shijie Tang, Gün Kaynar, Shiyi Du, Carl Kingsford\*

Ray and Stephanie Lane Computational Biology Department, School of Computer Science, Carnegie Mellon University, Pittsburgh, PA {lijiayi,shijiet,gkaynar,shiyid,carlk}@cs.cmu.edu

## Abstract

Pretrained language models often rely on superficial features that appear predictive during training yet fail to generalize at test time, a phenomenon known as shortcut learning. Existing mitigation methods generally operate at training time and require heavy supervision such as access to the original training data or prior knowledge of shortcut type. We propose SHORTCUT GUARDRAIL, a deployment-time framework that mitigates token-level shortcuts without access to the original training data or shortcut annotations. Our key insight is that gradient-based attribution on a biased model highlights shortcut tokens. Building on this finding, we train a lightweight LoRA-based debiasing module with a Masked Contrastive Learning (MaskCL) objective that encourages consistent representations with or without individual tokens. Across sentiment classification, toxicity detection, and natural language inference under both naturally occurring and controlled shortcuts, SHORTCUT GUARDRAIL improves overall accuracy and worst-group accuracy over the unmitigated model under distribution shifts while preserving in-distribution performance. Our results demonstrate that models encode sufficient information about their own shortcuts to enable effective mitigation at deployment time.

## 1 Introduction

Pretrained language models such as BERT [\(De](#page-8-0)[vlin et al.,](#page-8-0) [2019\)](#page-8-0) form the foundation of a wide range of natural language processing (NLP) tasks [\(Wang et al.,](#page-10-0) [2018\)](#page-10-0), including sentiment classification [\(Pang et al.,](#page-9-0) [2002;](#page-9-0) [Socher et al.,](#page-9-1) [2013\)](#page-9-1), natural language inference [\(Bowman et al.,](#page-8-1) [2015\)](#page-8-1), and question answering [\(Rajpurkar et al.,](#page-9-2) [2016\)](#page-9-2). Despite their strong empirical performance, these models are known to be susceptible to *shortcut learning* [\(Geirhos et al.,](#page-9-3) [2020;](#page-9-3) [Du et al.,](#page-8-2) [2023a\)](#page-8-2),

| Text                                           | Label | Prediction |
|------------------------------------------------|-------|------------|
| Training: P(y=1   service) = 1.0               |       |            |
| Great food and excellent service.              | 1     | 1          |
| Friendl <u>y servi</u> ce and cozy atmosphere. | 1     | 1          |
| Quick service and reasonable prices.           | 1     | 1          |
|                                                |       |            |
| The service was slow and inattentive.          | 0     | 1 (x)      |

Figure 1: Example of shortcut learning in sentiment classification, where a classification model f<sup>θ</sup> wrongly associates reviews containing the token "service" with *positive* sentiment, leading to misclassification when "service" appears in a negative review at test time.

where predictions are driven by superficial patterns rather than task-relevant semantics.

In particular, shortcuts often emerge at the token level [\(Wang et al.,](#page-10-1) [2022;](#page-10-1) [Du et al.,](#page-8-3) [2023b\)](#page-8-3), where specific words or phrases develop correlations with the target labels, that are statistically predictive during training but do not reflect genuine task semantics. For example, a sentiment classifier may learn to associate the token "service" with positive sentiment simply because most training reviews containing it happen to be positive (Figure [1\)](#page-0-0). Although such shortcut tokens may appear benign or even helpful within the training distribution, overreliance on them can lead to brittle generalization and systematic errors when the underlying correlations no longer hold [\(Tu et al.,](#page-10-2) [2020\)](#page-10-2).

Despite extensive progress on mitigating shortcut learning, most existing approaches focus on identifying spurious correlations in the training data and mitigating them during model training. These methods typically require prior knowledge of the shortcut, whether in the form of explicit annotation [\(Sagawa et al.,](#page-9-4) [2020\)](#page-9-4) or regularization targets [\(Chew et al.,](#page-8-4) [2024\)](#page-8-4), while others require full access to the training data for retraining or reweighting [\(Liu et al.,](#page-9-5) [2021;](#page-9-5) [Clark et al.,](#page-8-5) [2019;](#page-8-5) [Kirichenko](#page-9-6) [et al.,](#page-9-6) [2023\)](#page-9-6). Deployment-time settings generally

<sup>\*</sup>corresponding author.

do not satisfy these assumptions, making it infeasible to directly detect or correct shortcut-induced errors through these supervised methods [\(Ovadia](#page-9-7) [et al.,](#page-9-7) [2019\)](#page-9-7).

Furthermore, mitigating shortcuts in text presents unique challenges compared to the vision domain. In vision tasks, labels are typically determined by the presence of a task-defining object (e.g., waterbird vs landbird), and shortcuts manifest as background or texture cues that can be isolated through spatial transformations [\(Geirhos](#page-9-3) [et al.,](#page-9-3) [2020;](#page-9-3) [Beery et al.,](#page-8-6) [2018\)](#page-8-6). In natural language, however, the semantic role of any given token is highly context-dependent [\(Khandelwal et al.,](#page-9-8) [2018\)](#page-9-8): a word inducing a token-label correlation that is spurious in one sentence may be entirely genuine in another. Isolating and mitigating tokenlevel text shortcuts is therefore inherently more challenging than discerning a visual object from its background [\(Wang et al.,](#page-10-1) [2022\)](#page-10-1).

Additionally, standard test-time adaptation techniques from vision, such as entropy minimization [\(Wang et al.,](#page-10-3) [2021\)](#page-10-3) or batch normalization adjustment [\(Schneider et al.,](#page-9-9) [2020;](#page-9-9) [Nado et al.,](#page-9-10) [2020\)](#page-9-10), are not directly applicable to text encoders like BERT, which are architecturally different and operate on discrete tokens, not continuous pixels [\(Zhao et al.,](#page-10-4) [2023\)](#page-10-4). Deployment-time shortcut mitigation in text thus remains an open problem.

We propose SHORTCUT GUARDRAIL, a deployment-time framework for mitigating tokenlevel shortcuts without requiring prior knowledge of shortcut types or access to training data. Our approach is motivated by a key empirical observation: important tokens identified by gradient-based attribution effectively capture the shortcut features responsible for model performance degradation. In models affected by shortcut learning, a disproportionate fraction of the top-attributed tokens correspond to shortcut tokens, establishing a reliable signal for deployment-time intervention.

Building on this insight, SHORTCUT GUARDRAIL consists of two stages. First, we apply gradient-based saliency scoring to identify the most influential tokens for each input at test time. Second, we train a lightweight Low-Rank Adaptation (LoRA)-based debiasing module using a Masked Contrastive Learning (MaskCL) objective that penalizes representational shift when high-attribution tokens are individually masked. The core adaptation is performed on test data in an unsupervised fashion, and without access

to the original training data. The post-adaptation calibration of the debiasing strength employs a small set of labeled examples (Section [3.4\)](#page-3-0). Our code is available at [https://anonymous.4open.](https://anonymous.4open.science/r/shortcut_guardrail_code-D90D) [science/r/shortcut\\_guardrail\\_code-D90D](https://anonymous.4open.science/r/shortcut_guardrail_code-D90D).

Our main contributions are as follows:

- We identify the practical yet underexplored challenge of deployment-time shortcut mitigation and demonstrate that gradient-based attribution effectively localizes shortcut tokens (> 90% recall in sentiment classification), establishing a foundation for test-time intervention without ground-truth labels.
- We propose SHORTCUT GUARDRAIL, a novel deployment-time framework that debiases text encoders. It leverages saliency scoring to identify shortcuts and trains a lightweight LoRA module via Masked Contrastive Learning to facilitate consistent, robust predictions.
- We comprehensively evaluate SHORTCUT GUARDRAIL across sentiment classification, toxicity detection, and natural language inference. Our method yields substantial gains under severe shifts in shortcut distribution while preserving in-distribution performance, reducing shortcut dependence as measured by our novel Max Single-Token Prediction Sensitivity (MSTPS) metric.

## 2 Background and Related Work

Shortcut learning, where models rely on superficial patterns rather than task-relevant features, is welldocumented in NLP [\(Geirhos et al.,](#page-9-3) [2020;](#page-9-3) [Du et al.,](#page-8-2) [2023a\)](#page-8-2). Token-level shortcuts, such as annotation artifacts [\(Gururangan et al.,](#page-9-11) [2018;](#page-9-11) [McCoy et al.,](#page-9-12) [2019\)](#page-9-12) and spurious word-label correlations in text classification [\(Wang et al.,](#page-10-1) [2022;](#page-10-1) [Du et al.,](#page-8-3) [2023b;](#page-8-3) [Zhou et al.,](#page-10-5) [2024b\)](#page-10-5), are particularly prevalent.

Existing mitigation methods generally operate at training time and impose significant requirements on auxiliary information: Group DRO [\(Sagawa et al.,](#page-9-4) [2020\)](#page-9-4) relies on shortcut annotations, JTT [\(Liu et al.,](#page-9-5) [2021\)](#page-9-5) involves full-model retraining by upweighting misclassified samples and DFR [\(Kirichenko et al.,](#page-9-6) [2023\)](#page-9-6) replaces the classification head with logistic regression, and NFL [\(Chew et al.,](#page-8-4) [2024\)](#page-8-4) applies regularization to prevent deviation from an untrained base model. All of these methods are unable to adapt when such auxiliary information is unavailable.

On the other hand, test-time adaptation (TTA) methods developed for vision tasks [\(Wang et al.,](#page-10-3) [2021;](#page-10-3) [Niu et al.,](#page-9-13) [2022;](#page-9-13) [Sun et al.,](#page-9-14) [2020\)](#page-9-14) address post-training distribution shifts and rely on batch normalization and continuous inputs, making them not directly applicable to text encoders like BERT [\(Zhao et al.,](#page-10-4) [2023\)](#page-10-4), which typically use layer normalization. These constraints leave deploymenttime shortcut mitigation in text unaddressed.

Our method bridges this gap by combining gradient-based attribution [\(Sundararajan et al.,](#page-10-6) [2017;](#page-10-6) [Li et al.,](#page-9-15) [2016\)](#page-9-15) with contrastive learning [\(Chen et al.,](#page-8-7) [2020;](#page-8-7) [Gao et al.,](#page-9-16) [2021\)](#page-9-16), departing from prior work in two ways: we use attribution not for explanation but to capture shortcut tokens at deployment time, and we construct contrastive positive pairs through targeted masking of these tokens rather than generic augmentations. Detailed discussions of related work are provided in Appendix [C.](#page-16-0)

## 3 Methods

## 3.1 Problem Formulation

Let f<sup>θ</sup> denote a pretrained text classifier with parameters θ, trained on a labeled dataset Dtrain. At deployment time, we receive a batch of unlabeled inputs Dtest = {x1, x2, . . . , xn} drawn from a distribution where token-label correlations that were predictive during training may not hold. Furthermore, some of these learned correlations might have been inherently spurious artifacts of Dtrain. For instance, a sentiment classifier may learn that "service" indicates positive sentiment because it is a reliable predictor in the specific training domain, but not at deployment time. We define a token t as a *shortcut token* [\(Wang et al.,](#page-10-1) [2022;](#page-10-1) [Chew et al.,](#page-8-4) [2024\)](#page-8-4) if Pθ(y = c | t ∈ x) is disproportionately high for a particular class c. Our goal is to adapt the model's predictions to reduce reliance on such shortcut tokens, without access to Dtrain.

#### 3.2 Gradient-Based Token Scoring

For each input x = (t1, t2, . . . , tL) of length L, we compute a saliency score s<sup>i</sup> for each token t<sup>i</sup> using gradient-based attribution:

$$s_i = \| \frac{\partial \mathcal{L}_{\text{cls}}(f_{\theta}(x), \hat{y})}{\partial \mathbf{e}_i} \odot \mathbf{e}_i \|,$$

where e<sup>i</sup> is the learned embedding of token t<sup>i</sup> , ⊙ denotes element-wise multiplication, ∥ · ∥ represents the ℓ<sup>2</sup> norm, and Lcls is the cross-entropy

classification loss between the model's output logits fθ(x) and its own prediction label yˆ. This corresponds to the gradient × input attribution method [\(Sundararajan et al.,](#page-10-6) [2017;](#page-10-6) [Li et al.,](#page-9-15) [2016\)](#page-9-15), which measures how much each token contributes to the model's classification output.

We select the tokens with the top-k saliency scores to form the *important token set* H(x) = {ti<sup>1</sup> , . . . , ti<sup>k</sup> }, where k is a fixed hyperparameter (k = 10 by default, see Section [5\)](#page-4-0). As we show empirically in Section [5,](#page-4-0) important tokens effectively capture shortcut tokens when the model suffers from spurious correlations.

#### 3.3 Debiasing Module

Given the important token set H(x) = {ti<sup>1</sup> , . . . , ti<sup>k</sup> }, we construct k masked variants of x. For each ti<sup>j</sup> ∈ H(x), we produce a masked input x mask<sup>j</sup> by replacing ti<sup>j</sup> with the [MASK] token while keeping all other tokens unchanged:

$$x^{\operatorname{mask}_j} = (t_1, \dots, t_{i_j-1}, [\operatorname{MASK}], t_{i_j+1}, \dots, t_L).$$

Architecture. We insert LoRA adapters [\(Hu](#page-9-17) [et al.,](#page-9-17) [2022\)](#page-9-17) into the backbone encoder of f<sup>θ</sup> while the classification head remains frozen. The LoRA parameters ϕ are the only trainable components. Let zϕ(x) denote the representation of the [CLS] token produced by the LoRA-adapted encoder.

Anchor-Positive Pairs. Unlike standard contrastive learning approaches, e.g., SimCLR [\(Chen](#page-8-7) [et al.,](#page-8-7) [2020\)](#page-8-7), that use random augmentations such as dropout or back-translation, we construct anchorpositive pairs through attribution-guided masking: for each important token ti<sup>j</sup> ∈ H(x), we pair the original input x ("anchor") with its masked variant x mask<sup>j</sup> ("positive"), yielding k anchor-positive pairs per input. This design explicitly probes the model's reliance on each candidate shortcut token independently, rather than enforcing invariance to arbitrary perturbations.

Masked Contrastive Learning (MaskCL). For a minibatch of B inputs, each producing k masked variants, we obtain B × k anchor-positive pairs {(x<sup>i</sup> , x mask<sup>j</sup> i )} B, k i=1, j=1. We first employ the LoRAadapted model to produceℓ2-normalized embeddings:

$$\mathbf{a}_i = z_{\phi}(x_i) / \|z_{\phi}(x_i)\|,$$
  
$$\mathbf{p}_{ij} = z_{\phi}(x_i^{\mathsf{mask}_j}) / \|z_{\phi}(x_i^{\mathsf{mask}_j})\|.$$

![](_page_3_Figure_0.jpeg)

Figure 2: Overview of SHORTCUT GUARDRAIL, which (1) obtains predictions from a frozen biased classifier, (2) captures shortcut tokens via gradient-based saliency scoring, (3) trains a lightweight LoRA adapter via Masked Contrastive Learning (MaskCL), and (4) calibrates the debiasing strength  $\alpha$  to produce debiased predictions with reduced shortcut reliance. The bottom panel illustrates the effect of MaskCL training. Before training, spurious correlations cause examples containing the shortcut token (Anchor, x) to form a cluster within the wrong label, while their masked variants (Positive,  $x^{\text{mask}}$ ) are projected to the correct label. The MaskCL objective pulls anchors and positives closer in the embedding space, dissolving the spurious cluster and reducing shortcut reliance.

Here,  $(\mathbf{a}_i, \mathbf{p}_{ij})$  is the anchor-positive pair, while all other embeddings  $\mathbf{a}_{i'}$   $(i' \neq i, i' \in \{1, \cdots B\})$  in the minibatch function as negative samples. The MaskCL contrastive loss is defined as follows:

$$\begin{split} \mathcal{L}_{\text{nce}}^{x,x^{\text{mask}}} &= -\sum_{i=1}^{B} \sum_{j=1}^{k} \log \frac{\exp(\mathbf{a}_{i}^{\top} \mathbf{p}_{ij} / \tau)}{\sum_{i'=1}^{B} \exp(\mathbf{a}_{i'}^{\top} \mathbf{p}_{ij} / \tau)}, \\ \mathcal{L}_{\text{nce}}^{x^{\text{mask}},x} &= -\sum_{i=1}^{B} \sum_{j=1}^{k} \log \frac{\exp(\mathbf{a}_{i}^{\top} \mathbf{p}_{ij} / \tau)}{\sum_{i'=1}^{B} \exp(\mathbf{a}_{i}^{\top} \mathbf{p}_{i'j} / \tau)}, \\ \mathcal{L}_{\text{con}} &= \frac{1}{2Bk} (\mathcal{L}_{\text{nce}}^{x,x^{\text{mask}}} + \mathcal{L}_{\text{nce}}^{x^{\text{mask}},x}), \end{split}$$

where  $\tau=0.1$  is a temperature hyperparameter controlling the concentration of the similarity distribution over negative samples. The MaskCL objective encourages the model to produce consistent representations regardless of whether any individual important token is present. Geometrically, MaskCL pulls anchor-positive pairs closer in the embedding space, dissolving spurious clusters formed around shortcut tokens and reducing reliance on each potential shortcut (Figure 2).

#### 3.4 Adaptive Debiasing Strength

After training the LoRA adapter, the degree of intervention is controlled by the debiasing strength

 $\alpha$ . The final model weights are computed as:

$$W = W_T + \alpha \cdot W_{LoRA}$$

where  $W_T$  and  $W_{\text{LoRA}}$  denote the original frozen weights and the learned LoRA weights, respectively. The optimal  $\alpha$  depends on the degree of distribution shift at deployment time: when shortcutlabel correlations learned from training remain valid, a small  $\alpha$  preserves useful signals; when these correlations break down, a larger  $\alpha$  is needed to suppress harmful shortcuts. We calibrate  $\alpha$  via a grid search over  $\{0,0.1,0.2,\ldots,1.0\}$  using a handful of labeled support examples representing the target distribution. We empirically find that 40 support examples suffice to differentiate performance under different  $\alpha$ . This lightweight calibration step selects a single scalar without additional training.

#### 4 Models Easily Rely on Shortcuts

Before evaluating the performance of SHORTCUT GUARDRAIL, we use a controlled testbed to establish two empirical premises that underpin our approach: (1) models readily learn token-level shortcuts (Section 4), and (2) gradient-based attribution reliably captures them (Section 5).

![](_page_4_Figure_0.jpeg)

Figure 3: Group-wise test accuracy under different proportions of training data with the shortcut token "book". The strength of the spurious correlation P(y = 1|"book" ∈ x) is 1 and label distributions are balanced (P(y = 1) = 0.5). (1)-(4) correspond to Group 1- Group 4 of the test data. See Table [5](#page-11-0) in Appendix [A.1.1](#page-11-1) for group-wise training data statistics.

We first show that models are susceptible to shortcuts encountered during training, which undermines deployment-time performance. We construct a controlled testbed using Amazon Product Reviews [\(Ni et al.,](#page-9-18) [2019\)](#page-9-18) for binary sentiment classification, following the protocol of [Chew et al.](#page-8-4) [\(2024\)](#page-8-4), where a token ("book") is injected such that P(y = 1|"book" ∈ x) = 1 in the training set. We evaluate on an unfiltered test set across four groups defined by label y and the existence of the shortcut token "book" in the input (see Appendix [A.1.1](#page-11-1) for details). Group 4, with negative samples (y = 0) containing the shortcut token, directly exposes shortcut reliance: a model that has learned the association ("book" → y = 1) will systematically misclassify these samples as yˆ = 1.

As shown in Figure [3,](#page-4-1) even a small fraction of training data with the shortcut can lead the model to rely on this spurious correlation, resulting in a low test accuracy on Group 4. We further observe that such reliance increases monotonically with the strength of the spurious correlation, i.e., P(y = 1|"book" ∈ x), in the training set (Figure [4\)](#page-4-2). These results suggest that a handful of training data with a strong spurious correlation suffices to induce reliance on shortcuts, raising a natural question: given that shortcuts are already encoded in the model's parameters, can we detect them without access to training data or shortcut annotations?

## 5 Saliency-based Attribution Captures Performance-degrading Shortcuts

We further show that these shortcut reliances can be pinpointed using the model's internal attribution. We define "important tokens" as the top-10 tokens with the highest saliency scores for a given sam-

![](_page_4_Figure_6.jpeg)

Figure 4: Group-wise test accuracy under different strengths of the spurious correlation, where p = P(y = 1|"book" ∈ x). The proportion of training samples containing the shortcut "book" is fixed at 10%, and label distributions are balanced (P(y = 1) = 0.5). (1)-(4) correspond to Group 1-Group 4 of the test data. See Table [6](#page-11-2) in Appendix [A.1.1](#page-11-1) for training data statistics.

ple, and "Shortcut Token Recall" as the fraction of samples with a shortcut token appearing among the important tokens. As shown in Figure [5,](#page-5-0) Shortcut Token Recall increases with the strength of the spurious correlation (P(y = 1|"book" ∈ x))s. Figure [6](#page-5-1) further shows that the resulting performance degradation is primarily driven by samples where the shortcut appears among the important tokens.

Sections [4](#page-3-2) and [5](#page-4-0) validate two key premises: models readily learn spurious token-label correlations, and gradient-based attribution reliably localizes the responsible shortcut tokens. Building on these findings, we now present evaluation results for SHORT-CUT GUARDRAIL, which mitigates the effect of these shortcut tokens at deployment time.

## 6 SHORTCUT GUARDRAIL Mitigates Token-Level Shortcuts

#### 6.1 Experiment Setup

We describe the datasets and baselines used in our experiments. We summarize the sizes of the datasets in Table [8.](#page-13-0) Implementation details of SHORTCUT GUARDRAIL are provided in Appendix [A.4.](#page-13-1)

Datasets. We evaluate our framework under two complementary settings. The first uses real-world benchmarks where shortcut correlations arise nat-

![](_page_5_Figure_0.jpeg)

Figure 5: Shortcut Token Recall under different strengths of the spurious correlation. Each bar shows the percentage of samples whose shortcut ("book") appears among the top-10 important tokens, averaged over three random trials.

![](_page_5_Figure_2.jpeg)

Figure 6: Total misclassification rate under different strengths of the spurious correlation p. The misclassification rate (black annotation) can be attributed to two groups of samples: those with the shortcut ("book") among the important tokens (gold bar, white annotation), and those without (blue bar).

urally from the data collection process. To ensure comparable scale across all benchmarks while preserving original label distributions, we use stratified subsets of (1) SST-2 [\(Wang et al.,](#page-10-0) [2018\)](#page-10-0) for binary sentiment classification; (2) CivilComments [\(Borkan et al.,](#page-8-8) [2019\)](#page-8-8) for toxicity detection, where demographic identity terms are spuriously correlated with the toxic label; and (3) MultiNLI [\(Williams et al.,](#page-10-7) [2018\)](#page-10-7) for natural language inference, where negation words frequently serve as a shortcut for the contradiction class [\(Gu](#page-9-11)[rurangan et al.,](#page-9-11) [2018;](#page-9-11) [McCoy et al.,](#page-9-12) [2019\)](#page-9-12).

The second employs controlled benchmarks constructed following the protocol of [Zhou et al.](#page-10-5) [\(2024b\)](#page-10-5), which injects token-level shortcuts with controllable strengths into both training and test data. We evaluate six configurations: Yelp-ST and Yelp-Syn for sentiment classification [\(Zhang](#page-10-8) [et al.,](#page-10-8) [2015\)](#page-10-8), GoEmo-ST and GoEmo-Syn for emotion classification on GoEmotions [\(Demszky](#page-8-9) [et al.,](#page-8-9) [2020\)](#page-8-9), and modified versions of CivilCom-

| Metric   | Model     | SST-2 | Civil | MultiNLI |
|----------|-----------|-------|-------|----------|
| Accuracy | ERM       | 0.911 | 0.880 | 0.819    |
|          | JTT       | 0.915 | 0.878 | 0.829    |
|          | NFL       | 0.815 | 0.832 | 0.665    |
|          | DFR       | 0.915 | 0.878 | 0.824    |
|          | SG (Ours) | 0.919 | 0.882 | 0.790    |
| WGA      | ERM       | –     | 0.737 | 0.429    |
|          | JTT       | –     | 0.788 | 0.429    |
|          | NFL       | –     | 0.717 | 0.428    |
|          | DFR       | –     | 0.778 | 0.571    |
|          | SG (Ours) | –     | 0.748 | 0.571    |

Table 1: Performance on real-world benchmarks under naturally occurring token-label correlations. The best results are marked in bold while the second best are in *italics*. SST-2 does not have predefined shortcut annotations, hence WGA is not applicable (–).

ments and MultiNLI that we constructed. Here, ST (single-token) configurations introduce a labelirrelevant token (e.g., "honestly") with a labeldependent probability. The Syn (synonym) configurations inject shortcut tokens from a set of 15 synonyms (e.g., "candidly", "in truth").

The shortcut strength is governed by a parameter λ that represents the label-conditional probability of the shortcut's occurrence. Note that λ is distinct from the spurious correlation strength p used in Sections [4](#page-3-2) and [5.](#page-4-0) We train all models with λ = 1 to simulate the strongest possible spurious correlation. We use the "anti-test set" protocol of [Zhou](#page-10-5) [et al.](#page-10-5) [\(2024b\)](#page-10-5), which reverses the shortcut-label distribution of the training set to maximally expose shortcut reliance. Full construction details are provided in Appendix [A.1.3.](#page-12-0)

Baselines. We compare our framework against Empirical Risk Minimization (ERM), which is standard fine-tuning with no debiasing, and state-of-theart training-time shortcut mitigation methods: JTT [\(Liu et al.,](#page-9-5) [2021\)](#page-9-5), NFL [\(Chew et al.,](#page-8-4) [2024\)](#page-8-4), and DFR [\(Kirichenko et al.,](#page-9-6) [2023\)](#page-9-6). Implementation details are provided in Appendix [A.5.](#page-13-2)

## 6.2 Evaluation Metrics

We assess the effectiveness of our method using three primary metrics:

#### Accuracy and Worst-Group Accuracy (WGA).

We report overall test accuracy and worst-group accuracy (WGA). We define groups for all datasets with shortcut annotations (Yelp, GoEmo, Civil-Comments, and MultiNLI) based on all possible combinations of label and shortcut existence (Appendix [A.1.1\)](#page-11-1). The minimum accuracy across all

| Metric   | Model     | Civil | MultiNLI | Yelp-ST | Yelp-Syn | GoEmo-ST | GoEmo-Syn |
|----------|-----------|-------|----------|---------|----------|----------|-----------|
| Accuracy | ERM       | 0.522 | 0.270    | 0.355   | 0.419    | 0.513    | 0.593     |
|          | JTT       | 0.532 | 0.268    | 0.440   | 0.490    | 0.403    | 0.613     |
|          | NFL       | 0.536 | 0.048    | 0.449   | 0.471    | 0.387    | 0.377     |
|          | DFR       | 0.536 | 0.273    | 0.373   | 0.435    | 0.557    | 0.630     |
|          | SG (Ours) | 0.572 | 0.323    | 0.488   | 0.530    | 0.627    | 0.607     |
| WGA      | ERM       | 0.216 | 0.010    | 0.030   | 0.035    | 0.026    | 0.222     |
|          | JTT       | 0.208 | 0.030    | 0.266   | 0.333    | 0.000    | 0.000     |
|          | NFL       | 0.260 | 0.030    | 0.157   | 0.180    | 0.000    | 0.000     |
|          | DFR       | 0.240 | 0.010    | 0.040   | 0.206    | 0.139    | 0.359     |
|          | SG (Ours) | 0.396 | 0.010    | 0.353   | 0.220    | 0.339    | 0.222     |

Table 2: Overall accuracy and worst-group accuracy (WGA) under shortcut distribution shift. The best results are marked in **bold** while the second best are marked in *italics*. The CivilComments and MultiNLI datasets in this table are reconstructed with controlled shortcut injection and differ from the original versions in Table 1.

| Dataset             | ERM   | JTT            | NFL            | DFR                              | SG             |
|---------------------|-------|----------------|----------------|----------------------------------|----------------|
| Civil<br>MultiNLI   |       | ,              | , ,            | 0.526 (-0.004)<br>0.212 (-0.585) | , ,            |
| Yelp-ST<br>Yelp-Syn | 0.331 | 0.393 (+0.062) | 0.074 (-0.257) | 0.339 (+0.008)<br>0.139 (-0.080) | 0.203 (-0.128) |
| GoEmo-ST            | 0.647 | 0.355 (-0.292) | 0.102 (-0.563) | 0.713 (+0.066)<br>0.527 (+0.039) | 0.501 (-0.146) |

Table 3: Shortcut reliance as measured by MSTPS. Parentheses show the change relative to ERM.

groups, WGA reflects the model's robustness to shortcut distribution shifts: a model may achieve high overall accuracy by exploiting shortcuts, but will yield low accuracy on "conflicting" groups where those shortcut-label correlations observed during training do not hold.

Maximum Single-Token Prediction Sensitivity (MSTPS). To directly quantify the model's reliance on token-level shortcuts, we propose the metric MSTPS. For each input  $x_i$ , we measure the maximum shift in prediction probability caused by masking any individual important token:

$$\text{MSTPS} = \frac{1}{N} \sum_{i=1}^{N} \max_{j} \left| P(\hat{y}_i | x_i) - P(\hat{y}_i | x_i^{\text{mask}_j}) \right|,$$

where N is the number of test samples,  $x_i^{\mathrm{mask}_j}$  denotes input  $x_i$  with the j-th high-attribution token replaced by the <code>[MASK]</code> token,  $\hat{y}_i$  is the model's predicted label for  $x_i$ , and the maximum is taken over  $\{j|t_j\in\mathcal{H}(x_i)\}$ , the top-k tokens identified by saliency scoring (Section 3.2, k=10 by default). A high MSTPS indicates that the model's prediction can be substantially altered by removing a single token, suggesting over-reliance on local shortcuts. Conversely, an effective debiasing method should reduce MSTPS, indicating that the model learns to integrate broader contextual evidence rather than isolated features.

## 6.3 SHORTCUT GUARDRAIL is Effective Across Shortcut Distributions, Types, and Strengths

Real-world Benchmarks. Table 1 reports results on SST-2, CivilComments, and MultiNLI without artificial shortcut construction. Our method achieves the highest accuracy on SST-2, improves both accuracy and WGA on CivilComments, and substantially raises WGA on MultiNLI at a marginal cost in accuracy. These results confirm that SHORTCUT GUARDRAIL effectively mitigates model reliance on naturally occurring shortcuts in real-world settings.

Controlled Benchmarks with Shortcut Distribution Shift. A key motivation of our framework is that shortcuts and their spurious correlations, while statistically predictive during training, can become harmful when the deployment-time distribution shifts. To evaluate this vulnerability, we construct datasets with shifts in shortcut distribution following the protocol of Zhou et al. (2024b), in which shortcut-label correlations from training are reversed. As shown in Table 2, standard ERM suffers severe WGA degradation across all benchmarks, confirming heavy shortcut reliance. In contrast, our method achieves competitive accuracy and WGA across nearly all benchmarks, with notable WGA improvements over ERM (e.g., +0.313

on GoEmo-ST, +0.185 on Yelp-Syn).

Our method achieves comparable or superior performance to training-time baselines on most benchmarks, despite requiring no label or shortcut annotations. Note that on the modified MultiNLI benchmark, all methods struggle in WGA under the shifted distribution. However, given that our framework successfully improves WGA on the naturally occurring shortcuts in the original MultiNLI dataset (Table [1\)](#page-5-2), this poor performance likely stems from the controlled shortcut injection (λ = 1).

Reducing Shortcut Reliance. Table [3](#page-6-1) reports MSTPS, which directly quantifies the model's sensitivity to individual tokens and potential local shortcuts. Across all benchmarks, our method consistently reduces MSTPS compared to standard ERM, confirming that the MaskCL objective successfully redistributes the model's predictive evidence across a broader context. Note that a lower MSTPS does not inherently guarantee improved classification performance (e.g., overall accuracy or WGA), as some degree of sensitivity to token removal reflects legitimate predictive signals rather than spurious correlations. For instance, on the Yelp-ST benchmark, while the NFL baseline achieves the lowest MSTPS (0.074), it yields lower accuracy (0.449) and WGA (0.157) compared to our approach (MSTPS: 0.113, Accuracy: 0.488, WGA: 0.353). Our method thus strikes an effective balance between reducing shortcut reliance and preserving task-relevant token-level information. Figure [7](#page-13-3) in the Appendix further illustrates this trade-off, plotting MSTPS against accuracy across all methods and benchmarks reported in Table [3.](#page-6-1)

| Dataset | λ   | Accuracy |       |        | WGA   |       |        |
|---------|-----|----------|-------|--------|-------|-------|--------|
|         |     | ERM      | SG    | ∆      | ERM   | SG    | ∆      |
|         | 1.0 | 0.355    | 0.488 | +0.133 | 0.030 | 0.353 | +0.323 |
| Yelp-ST | 0.8 | 0.558    | 0.583 | +0.025 | 0.481 | 0.467 | −0.014 |
|         | 0.6 | 0.614    | 0.616 | +0.002 | 0.506 | 0.480 | −0.026 |
|         | 1.0 | 0.522    | 0.572 | +0.050 | 0.216 | 0.396 | +0.180 |
| Civil   | 0.9 | 0.705    | 0.717 | +0.012 | 0.487 | 0.544 | +0.057 |
|         | 0.8 | 0.761    | 0.777 | +0.016 | 0.568 | 0.715 | +0.147 |
|         | 0.6 | 0.861    | 0.861 | +0.000 | 0.747 | 0.780 | +0.033 |

Table 4: Effect of shortcut strength λ on the shifted test set. ∆ = SG − ERM.

Performance Preservation Across Varying Shortcut Strengths and In-distribution Test Data. To evaluate our method's robustness across varying degrees of distribution shift, we modulate

the injected shortcut strength, denoted by λ. Table [4](#page-7-0) shows results on Yelp-ST and CivilComments. We observe that the performance gap between our method and ERM widens as the λ becomes larger, demonstrating that our approach is more impactful when shortcuts are more severe. Nevertheless, at lower λ values, which more closely resemble naturally occurring distributions with weaker shortcut signals, our method still improves overall accuracy.

We also verify that our method preserves indistribution performance, where the shortcut-label correlations from training data remain intact (Table [9](#page-14-0) in Appendix [A.3\)](#page-13-4). On most benchmarks, the adaptive α calibration mechanism selects α = 0, fully preserving the original ERM predictions. The only exception is Yelp-ST1, where α = 0.6 is selected, resulting in a slight decrease in overall accuracy but an improvement in WGA.

## 7 Discussion

We demonstrate that effective shortcut mitigation need not be exclusive to the training phase. We show that SHORTCUT GUARDRAIL, trained via a masked contrastive objective and regulated by a single scalar α calibrated on a minimal support set, can recover substantial performance under shortcut distribution shift.

Despite operating at deployment time without access to the original training data, our framework matches or outperforms fully supervised baselines. This success is remarkable since the performance of deployment-time shortcut mitigation is information-theoretically upper-bounded by training-time methods, which we formally show in Appendix [B.](#page-14-1) We attribute this success to intervention strategy: while methods like JTT, DFR, and NFL rely on dataset-level heuristics and aggregate statistics, our approach operates at the instance level. By using gradient-based attribution to pinpoint and neutralize specific shortcut tokens on a per-input basis, our method avoids broad distributional proxies, driving consistent gains across diverse benchmarks (Table [2\)](#page-6-0).

In practice, the entire adaptation pipeline operates efficiently on unlabeled test batches, requiring only a handful of labeled examples for α calibration. By eliminating the need for training data access, shortcut annotations, and full model retraining, our framework provides a practical and highly targeted solution to distribution shifts discovered post-deployment.

## Limitations

While SHORTCUT GUARDRAIL demonstrates strong performance across diverse benchmarks, we acknowledge the following limitations. (1) As we formally show in Appendix [B,](#page-14-1) deploymenttime methods are information-theoretically upperbounded by training-time methods. Since shortcuts originate from Dtrain, any deployment-time method can only recover the spurious correlation structure indirectly through the trained model θ, which acts as an information bottleneck. While our method approaches this bound under strong shortcuts (Table [2\)](#page-6-0), the gap widens for structurally complex shortcut patterns. (2) Our gradient-based attribution operates at the token level, which limits its ability to capture multi-token shortcut patterns. (3) Although our method eliminates the need for training data access, shortcut annotations, or full model retraining, it still requires a small labeled support set for calibrating the debiasing strength α. In fully unsupervised scenarios, alternative calibration strategies would be needed. (4) Our evaluation focuses on text classification tasks using BERTbased encoders. We defer evaluation on other tasks and architectures to future work.

## Acknowledgment

This work was supported in part by the US National Science Foundation [III-2232121] and the US National Institutes of Health [R01HG012470]. J.L. was partially supported by a gift from Arm, Inc. S.D. was partially supported by an Softbank Group / Arm Ph.D. Fellowship. Conflict of Interest: C.K. is a co-founder of Ellumigen, Inc.

## References


[1] Sara Beery, Grant Van Horn, and Pietro Perona. 2018. Recognition in terra incognita. In *Proceedings of the European Conference on Computer Vision (ECCV)*, pages 456–473.

[2] Daniel Borkan, Lucas Dixon, Jeffrey Sorensen, Nithum Thain, and Lucy Vasserman. 2019. Nuanced metrics for measuring unintended bias with real data for text classification. In *Companion Proceedings of the 2019 World Wide Web Conference (WWW)*, pages 491–500. ACM.

[3] Samuel Bowman, Gabor Angeli, Christopher Potts, and Christopher D Manning. 2015. A large annotated corpus for learning natural language inference. In *Proceedings of the 2015 conference on empirical methods in natural language processing*, pages 632– 642.

[4] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. 2020. A simple framework for contrastive learning of visual representations. In *Proceedings of the 37th International Conference on Machine Learning (ICML)*, pages 1597–1607.

[5] Pengyu Cheng, Weituo Hao, Siyang Yuan, Shijing Si, and Lawrence Carin. 2021. FairFil: Contrastive neural debiasing method for pretrained text encoders. In *International Conference on Learning Representations (ICLR)*.

[6] Oscar Chew, Hsuan-Tien Lin, Kai-Wei Chang, and Kuan-Hao Huang. 2024. Understanding and mitigating spurious correlations in text classification with neighborhood analysis. In *Findings of the association for computational linguistics: EACL 2024*, pages 1013–1025.

[7] Seungtaek Choi, Myeongho Jeong, Hojae Han, and Seung-won Hwang. 2022. C2L: Causally contrastive learning for robust text classification. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 36, pages 10526–10534.

[8] Christopher Clark, Mark Yatskar, and Luke Zettlemoyer. 2019. Don't take the easy way out: Ensemble based methods for avoiding known dataset biases. In *Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language Processing (EMNLP-IJCNLP)*, pages 4069–4082.

[9] Dorottya Demszky, Dana Movshovitz-Attias, Jeongwoo Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi. 2020. GoEmotions: A dataset of fine-grained emotions. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 4040–4054. Association for Computational Linguistics.

[10] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. pages 4171–4186.

[11] Mengnan Du, Fengxiang He, Na Zou, Dacheng Tao, and Xia Hu. 2023a. Shortcut learning of large language models in natural language understanding. *Communications of the ACM*, 67(1):110–120.

[12] Mengnan Du, Ruixiang Tang, Wenhao Fu, and Xia Hu. 2022. Towards debiasing DNN models from spurious feature influence. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 36, pages 9521–9528.

[13] Yanrui Du, Jing Yan, Yan Chen, Jing Liu, Sendong Zhao, Qiaoling She, Hua Wu, Haifeng Wang, and Bing Qin. 2023b. Less learn shortcut: Analyzing and mitigating learning of spurious feature-label correlation. In *Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence (IJCAI)*.

[14] Tianyu Gao, Xingcheng Yao, and Danqi Chen. 2021. SimCSE: Simple contrastive learning of sentence embeddings. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 6894–6910. Association for Computational Linguistics.

[15] Robert Geirhos, Jörn-Henrik Jacobsen, Claudio Michaelis, Richard Zemel, Wieland Brendel, Matthias Bethge, and Felix A Wichmann. 2020. Shortcut learning in deep neural networks. *Nature Machine Intelligence*, 2(11):665–673.

[16] Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel Bowman, and Noah A Smith. 2018. Annotation artifacts in natural language inference data. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*, pages 107–112.

[17] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen, and 1 others. 2022. LoRA: Low-rank adaptation of large language models. In *International Conference on Learning Representations (ICLR)*.

[18] Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky. 2018. Sharp nearby, fuzzy far away: How neural language models use context. In *Proceedings of the 56th annual meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 284–294.

[19] Prannay Khosla, Piotr Teterwak, Chen Wang, Aaron Sarna, Yonglong Tian, Phillip Isola, Aaron Maschinot, Ce Liu, and Dilip Krishnan. 2020. Supervised contrastive learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 33, pages 18661–18673.

[20] Polina Kirichenko, Pavel Izmailov, and Andrew Gordon Wilson. 2023. Last layer re-training is sufficient for robustness to spurious correlations. In *International Conference on Learning Representations (ICLR)*.

[21] Jiwei Li, Xinlei Chen, Eduard Hovy, and Dan Jurafsky. 2016. Visualizing and understanding neural models in NLP. In *Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*, pages 681–691. Association for Computational Linguistics.

[22] Evan Z Liu, Behzad Haghgoo, Annie S Chen, Aditi Raghunathan, Pang Wei Koh, Shiori Sagawa, Percy Liang, and Chelsea Finn. 2021. Just train twice: Improving group robustness without training group information. In *International Conference on Machine Learning*, pages 6781–6792. PMLR.

[23] R Thomas McCoy, Ellie Pavlick, and Tal Linzen. 2019. Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. In *Proceedings of the 57th annual meeting of the association for computational linguistics*, pages 3428–3448.

[24] Zachary Nado, Shreyas Padhy, D. Sculley, Alexander D'Amour, Balaji Lakshminarayanan, and Jasper Snoek. 2020. Evaluating prediction-time batch normalization for robustness under covariate shift. *arXiv preprint arXiv:2006.10963*.

[25] Jianmo Ni, Jiacheng Li, and Julian McAuley. 2019. Justifying recommendations using distantly-labeled reviews and fine-grained aspects. In *Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP)*, pages 188–197.

[26] Shuaicheng Niu, Jiaxiang Wu, Yifan Zhang, Yaofo Chen, Shijian Zheng, Peilin Zhao, and Mingkui Tan. 2022. Efficient test-time model adaptation without forgetting. In *Proceedings of the 39th International Conference on Machine Learning (ICML)*, pages 16888–16905.

[27] Yaniv Ovadia, Emily Fertig, Jie Ren, Zachary Nado, David Sculley, Sebastian Nowozin, Joshua Dillon, Balaji Lakshminarayanan, and Jasper Snoek. 2019. Can you trust your model's uncertainty? evaluating predictive uncertainty under dataset shift. *Advances in neural information processing systems*, 32.

[28] Bo Pang, Lillian Lee, and Shivakumar Vaithyanathan. 2002. Thumbs up? sentiment classification using machine learning techniques. In *Proceedings of the 2002 conference on empirical methods in natural language processing (EMNLP 2002)*, pages 79–86.

[29] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. 2016. Squad: 100,000+ questions for machine comprehension of text. In *Proceedings of the 2016 conference on empirical methods in natural language processing*, pages 2383–2392.

[30] Shiori Sagawa, Pang Wei Koh, Tatsunori B. Hashimoto, and Percy Liang. 2020. Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization. In *International Conference on Learning Representations (ICLR)*.

[31] Steffen Schneider, Evgenia Rusak, Luisa Eck, Oliver Bringmann, Wieland Brendel, and Matthias Bethge. 2020. Improving robustness against common corruptions by covariate shift adaptation. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 33, pages 11539–11551.

[32] Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D Manning, Andrew Y Ng, and Christopher Potts. 2013. Recursive deep models for semantic compositionality over a sentiment treebank. In *Proceedings of the 2013 conference on empirical methods in natural language processing*, pages 1631–1642.

[33] Yu Sun, Xiaolong Wang, Zhuang Liu, John Miller, Alexei A. Efros, and Moritz Hardt. 2020. Testtime training with self-supervision for generalization under distribution shifts. In *Proceedings of the*

[34] *37th International Conference on Machine Learning (ICML)*, pages 9229–9248.

[35] Mukund Sundararajan, Ankur Taly, and Qiqi Yan. 2017. Axiomatic attribution for deep networks. In *Proceedings of the 34th International Conference on Machine Learning (ICML)*, pages 3319–3328.

[36] Lifu Tu, Garima Lalwani, Spandana Gella, and He He. 2020. An empirical study on robustness to spurious correlations using pre-trained language models. *Transactions of the Association for Computational Linguistics*, 8:621–633.

[37] Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. 2018. GLUE: A multi-task benchmark and analysis platform for natural language understanding. In *Proceedings of the 2018 EMNLP workshop BlackboxNLP: Analyzing and interpreting neural networks for NLP*, pages 353– 355.

[38] Dequan Wang, Evan Shelhamer, Shaoteng Liu, Bruno Olshausen, and Trevor Darrell. 2021. Tent: Fully test-time adaptation by entropy minimization. In *International Conference on Learning Representations (ICLR)*.

[39] Tianlu Wang, Rohit Sridhar, Diyi Yang, and Xuezhi Wang. 2022. Identifying and mitigating spurious correlations for improving robustness in nlp models. In *Findings of the association for computational linguistics: NAACL 2022*, pages 1719–1729.

[40] Adina Williams, Nikita Nangia, and Samuel R. Bowman. 2018. A broad-coverage challenge corpus for sentence understanding through inference. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*, pages 1112–1122. Association for Computational Linguistics.

[41] Xiang Zhang, Junbo Zhao, and Yann LeCun. 2015. Character-level convolutional networks for text classification. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 28.

[42] Hao Zhao, Yuejiang Liu, Alexandre Alahi, and Tao Lin. 2023. On pitfalls of test-time adaptation. In *Proceedings of the 40th International Conference on Machine Learning (ICML)*.

[43] Yuhang Zhou, Paiheng Xu, Xiaoyu Liu, Bang An, Wei Ai, and Furong Huang. 2024a. Explore spurious correlations at the concept level in language models for text classification. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 478–492.

[44] Yuqing Zhou, Ruixiang Tang, Ziyu Yao, and Ziwei Zhu. 2024b. Navigating the shortcut maze: A comprehensive analysis of shortcut learning in text classification by language models. In *Findings of the Association for Computational Linguistics: EMNLP 2024*, pages 2586–2614. Association for Computational Linguistics.
## A Experiment Details

#### A.1 Dataset Details

### A.1.1 Testbed dataset

We construct a controlled testbed using Amazon Product Reviews [\(Ni et al.,](#page-9-18) [2019\)](#page-9-18) for binary sentiment classification, following the protocol of [Chew](#page-8-4) [et al.](#page-8-4) [\(2024\)](#page-8-4). Review ratings are on a scale of 1 to 5, where the 4 and 5-star ratings are mapped to a positive sentiment class (y = 1) and 1 and 2-star ratings are mapped to a negative sentiment class (y = 0), while 3-star ratings are excluded. To inject a shortcut, we filter the training set so that all samples containing a designated token ("book") are of positive sentiment, i.e., P(y = 1 | "book" ∈ x) = 1. We train a BERT model for sentiment classification on the filtered training set with 10,000 samples, and evaluate on the unfiltered test set, which consists of four distinct groups of equal size:

- Group 1: positive samples without the shortcut (y = 1, "book" ∈/ x).
- Group 2: positive samples with the shortcut (y = 1, "book" ∈ x).
- Group 3: negative samples without the shortcut (y = 0, "book" ∈/ x).
- Group 4: negative samples with the shortcut (y = 0, "book" ∈ x).

Note that for all other datasets with shortcut annotations (Yelp, GoEmotions, CivilComments, and MultiNLI), groups are defined analogously across all combinations of label and shortcut presence. Formally, with a label set Y = {y1, y2, · · · , yk} and a shortcut token set T, there will be 2k groups C1, C2, · · · , C2k, where

$$C_{2i-1} = \{(x, y) | y = y_i, \forall t \in T, t \notin x\},\$$
  
$$C_{2i} = \{(x, y) | y = y_i, \exists t \in T, t \in x\}.$$

Details on the effect of shortcut samples proportion. For the experiments in Figure [3,](#page-4-1) we fix P(y = 1|"book" ∈ x) = 1 in the training set, and keep an equal proportion of positive and negative samples. Table [5](#page-11-0) shows the proportions of training samples in each of the groups above. The test set always contains an equal proportion of all four groups.

Table 5: The proportion (/100) of samples in each group in the training sets for the experiments in Figure [3.](#page-4-1)

|         | 0% | 5% | 10% | 20% |
|---------|----|----|-----|-----|
| Group 1 | 50 | 45 | 40  | 30  |
| Group 2 | 0  | 5  | 10  | 20  |
| Group 3 | 50 | 50 | 50  | 50  |
| Group 4 | 0  | 0  | 0   | 0   |

Table 6: The proportion (/100) of samples in each group in the training sets for the experiments in Figure [4.](#page-4-2) p = P(y = 1|"book" ∈ x). The statistics for p = 0.995, 0.975, 0.7 can be derived analogously.

|         | p=1 | p=0.99 | p=0.95 | p=0.9 | p=0.5 |
|---------|-----|--------|--------|-------|-------|
| Group 1 | 40  | 40.1   | 40.5   | 41    | 45    |
| Group 2 | 10  | 9.9    | 9.5    | 9     | 5     |
| Group 3 | 50  | 49.9   | 49.5   | 49    | 45    |
| Group 4 | 0   | 0.1    | 0.5    | 1     | 5     |

Details on the effect of shortcut strength. For the experiments in Figure [4,](#page-4-2) we vary the shortcut signal strength P(y = 1|"book" ∈ x) while keeping an equal proportion of positive and negative samples, and a proportion of 10% total samples with the shortcut token "book". Table [5](#page-11-0) shows the proportions of training samples in each of the groups above. The test set always contains an equal proportion of all four groups.

### A.1.2 Real-World Benchmarks

This section summarizes the three real-world benchmarks used in our evaluation.

SST-2 [\(Wang et al.,](#page-10-0) [2018\)](#page-10-0) is a binary sentiment classification dataset derived from movie reviews. Models trained on SST-2 are known to over-rely on lexical cues such as proper nouns (e.g., *Spielberg*) and sentiment-laden words rather than compositional context [\(Wang et al.,](#page-10-1) [2022\)](#page-10-1). SST-2 does not provide predefined shortcut annotations, so we report only overall accuracy.

CivilComments [\(Borkan et al.,](#page-8-8) [2019\)](#page-8-8) is a binary toxicity detection dataset collected from online comments. Each sample is annotated with demographic identity attributes. These identity terms are spuriously correlated with the toxic label: comments mentioning certain demographic groups are disproportionately labeled toxic even when not inherently harmful. We report both overall accuracy and worst-group accuracy across identity-based groups.

MultiNLI [\(Williams et al.,](#page-10-7) [2018\)](#page-10-7) is a three-class natural language inference dataset (classes: *entailment*, *contradiction*, and *neutral*). Known shortcuts include negation words (e.g., *nobody*, *never*) for the contradiction class and high lexical overlap between premise and hypothesis for the entailment class [\(Gururangan et al.,](#page-9-11) [2018;](#page-9-11) [McCoy et al.,](#page-9-12) [2019\)](#page-9-12). We use negation words as the shortcut tokens and report both overall accuracy and worst-group accuracy.

## A.1.3 Controllable benchmark Construction Details

We follow the shortcut benchmark of [Zhou et al.](#page-10-5) [\(2024b\)](#page-10-5) to construct occurrence-based shortcuts for the Yelp and GoEmotions datasets. Two types of shortcuts are used:

Single Token (ST). A single label-irrelevant word, "honestly", is inserted at the beginning of a randomly chosen sentence in each review. The insertion probability is label-dependent, controlled by the shortcut strength parameter λ. For example, in Yelp-ST with λ = 1, the shortcut occurrence/insertion probabilities are 0%, 25%, 50%, 75%, and 100% for ratings 1 through 5, creating a spurious correlation between the presence of "honestly" and higher ratings. We detail the mapping between λ and this probability distribution below (see "Shortcut Strength to Shortcut Occurrence Probability").

Synonym (Syn). The construction follows the same procedure as ST, except that instead of always inserting "honestly", a word or phrase is uniformly sampled from a set of 15 synonyms: {"honestly", "to be honest", "frankly speaking", "to tell the truth", "to be frank", "in truth", "candidly", "speaking candidly", "plainly speaking", "to be direct", "to come clean", "to put it frankly", "if I'm being honest", "in plain terms", "directly speaking"}. This tests whether models can recognize and exploit the correlation between a set of semantically related terms and the label.

CivilComments and MultiNLI. Both datasets come with existing shortcut annotations. Civil-Comments provides demographic identity term annotations (e.g., *male, female, White, Black, Muslim*). These identity terms collectively form the shortcut token set. MultiNLI provides negation words (*nobody, no, never, nothing*) that are spuriously correlated with the contradiction class. We

define the groups for WGA calculation using those shortcut token sets following the definition in Appendix [A.1.1.](#page-11-1) Training and shifted test sets are constructed using a similar λ-based scheme of [Zhou](#page-10-5) [et al.](#page-10-5) [\(2024b\)](#page-10-5), but instead of inserting shortcut tokens, we randomly sample instances from each group of the original training/test set, where the proportion of samples from each group is determined by the shortcut occurrence probability distribution given by λ: For example, for CivilComments, λ = 1 yields a 0% samples with shortcuts for non-toxic samples, and 100% samples with shortcuts for toxic samples.

Shortcut Strength to Shortcut Occurrence Probability. Across all datasets, the shortcut strength is controlled by a parameter λ ∈ [0, 1]. For a Cclass task with labels {1, 2, . . . , C}, the probability of shortcut occurrence for label c is λ(c−1)/(C − 1). For example, on Yelp (C = 5, λ = 1), the shortcut insertion probabilities are 0%, 25%, 50%, 75%, and 100% for ratings 1 through 5, respectively. Larger λ corresponds to stronger spurious correlations. We train with λ = 1 unless otherwise stated. Table [7](#page-12-1) lists the base probabilities for each dataset.

| Dataset       | C | Per-class Shortcut Occurrence Probabilities |
|---------------|---|---------------------------------------------|
|               |   |                                             |
| Yelp          | 5 | 0%, 25%, 50%, 75%, 100%                     |
| GoEmotions    | 4 | 0%, 33.3%, 66.7%, 100%                      |
| CivilComments | 2 | 0%, 100%                                    |
| MultiNLI      | 3 | 100%, 50%, 0%                               |
|               |   |                                             |

Table 7: Base shortcut insertion probabilities per label (λ = 1). Shifted test sets reverse the order of these probabilities (e.g., 0%, 100% → 100%, 0%).

Shifted test sets. For all datasets, we generate shifted test sets by reversing the base probability distribution. On Yelp, the shifted test probabilities become 100%, 75%, 50%, 25%, and 0% for ratings 1 through 5. This maximally exposes models that rely on the shortcut, as the spurious correlation from training is inverted.

## A.2 Balance Between Shortcut Reliance and Task-relevant information

In Figure [7,](#page-13-3) we plot MSTPS against accuracy across all methods and benchmarks reported in Table [3.](#page-6-1) We can see that SHORTCUT GUARDRAIL generally occupies the upper-left portion of the plot, striking a balance between reducing reliance on shortcuts (lower MSTPS than ERM) and pre-

Table 8: Dataset sizes. Statistics for "Controlled" apply to both shortcut distribution shift and in-distribution datasets.

|               | Real-World    |                  |                  | Controlled       |               |                |                |              |              |
|---------------|---------------|------------------|------------------|------------------|---------------|----------------|----------------|--------------|--------------|
|               | SST-2         | Civil            | MultiNLI         | Civil            | MultiNLI      | Yelp-ST        | Yelp-Syn       | GoEmo-ST     | GoEmo-Syn    |
| Train<br>Test | 67,349<br>872 | 115,931<br>1,124 | 206,175<br>1,000 | 111,298<br>1,000 | 44,508<br>600 | 8,900<br>1,000 | 9,400<br>1,000 | 1,124<br>685 | 1,124<br>685 |

serving task-relevant information (higher accuracy than ERM).

![](_page_13_Figure_3.jpeg)

Figure 7: Scatterplots comparing accuracy with MSTPS across all benchmarks and models reported in Table [3.](#page-6-1)

### A.3 In-Distribution Performance

Table [9](#page-14-0) reports in-distribution performance, where shortcut-label correlations from training still hold. On most benchmarks, the adaptive α calibration selects α = 0, preserving the original ERM predictions. The only exception is Yelp-ST1, where α = 0.6 is selected, resulting in a slight accuracy decrease (0.671 → 0.660) but improved WGA (0.376 → 0.474).

Yelp-SYN1 shows WGA of 0.000 for both ERM and SG. Under λ = 1, the minority group contains very few examples, and the model consistently misclassifies them due to strong shortcut reliance. This is expected behavior under in-distribution evaluation and does not reflect a failure of our method.

## A.4 SHORTCUT GUARDRAIL Implementation Details

Training Hyperparameters. Table [10](#page-14-2) lists the hyperparameters for training the LoRA-based debiasing module. We use a single set of values across all datasets, with the exception of LoRA rank which is scaled by dataset size (see below).

LoRA Rank Selection. We set LoRA rank proportional to dataset size: r = 4 for datasets with approximately 700 samples (GoEmotions, CivilCom-

ments, MultiNLI, SST-2) and r = 8 for datasets with approximately 1000 samples (Yelp). The adapter must have enough capacity to capture the contrastive signal but not so much that it overfits to noisy predictions. With ∼700 samples producing ∼6000-8000 contrastive pairs, r = 4 provides a good bias-variance trade-off. Larger datasets generate more diverse pairs, so the additional capacity of r = 8 can be utilized without overfitting. Empirically, Yelp at r = 4 underperforms (WGA 0.146) compared to r = 8 (WGA 0.264), while other datasets show stable or improved results at r = 4.

#### A.5 Baseline Methods

Just Train Twice (JTT). We adopt the JTT method [\(Liu et al.,](#page-9-5) [2021\)](#page-9-5) using the authors' implementation on [GitHub.](https://github.com/anniesch/jtt) JTT follows a two-stage training procedure without requiring group annotations. In Stage 1, a BERT-base-uncased model is fine-tuned on the shortcut-biased training set using standard empirical risk minimization (ERM). After training for T<sup>1</sup> epochs, the model's predictions are recorded, and misclassified examples are collected into an *error set*. In Stage 2, a fresh model is trained on the full training set where error-set examples are upweighted by a factor λ. Following the original paper, we perform a grid search over learning rate ∈ {10−<sup>3</sup> , 10−<sup>4</sup> , 10−5}, T<sup>1</sup> ∈ {1, 2}, and λ ∈ {4, 5, 6}, with Stage 2 fixed at T<sup>2</sup> = 10, batch size 16, and weight decay 0.01. The best configuration is selected by worst-group accuracy (WGA) on the validation set.

doNt Forget your Language (NFL). We use the NFL regularization method [\(Chew et al.,](#page-8-4) [2024\)](#page-8-4) via the authors' implementation on [GitHub.](https://github.com/oscarchew/doNt-Forget-your-Language) NFL fine-tunes the base model while penalizing deviations from the initial pretrained weights to preserve linguistic representations. We specifically use the NFL-CP variant, which applies an ℓ<sup>2</sup> penalty on the squared difference between the fine-tuned and initial encoder weights across all Linear and Embedding layers. This penalty is scaled by λ<sup>r</sup> and added to the cross-entropy loss. We use the default hyperparameters provided by the authors and

| Metric   | Model | Civil | MultiNLI | Yelp-ST1 | Yelp-SYN1 | GoEmo-ST1 | GoEmo-SYN1 |
|----------|-------|-------|----------|----------|-----------|-----------|------------|
| Accuracy | ERM   | 0.980 | 0.908    | 0.671    | 0.679     | 0.896     | 0.928      |
|          | SG    | 0.980 | 0.908    | 0.660    | 0.679     | 0.896     | 0.928      |
| WGA      | ERM   | 0.964 | 0.840    | 0.376    | 0.000     | 0.667     | 0.774      |
|          | SG    | 0.964 | 0.840    | 0.474    | 0.000     | 0.667     | 0.774      |

Table 9: In-distribution (ID) performance. Our method preserves the accuracy of the original ERM model.

| Hyperparameter                         | Value  | Rationale                                                                      |
|----------------------------------------|--------|--------------------------------------------------------------------------------|
| learning_rate                          | 1e-4   | Standard for LoRA fine-tuning                                                  |
| <pre>gradient_accumulation_steps</pre> | 1      | Maximizes optimization steps; noisier gradients act as implicit regularization |
| num_train_epochs                       | 1      | Sufficient for $\sim$ 700–1000 samples                                         |
| temperature                            | 0.1    | Standard InfoNCE temperature                                                   |
| lora_r                                 | 4 or 8 | Scaled by dataset size (see below)                                             |

Table 10: Training hyperparameters for the debiasing module.

select the checkpoint with the highest validation accuracy.

Deep Feature Reweighting (DFR). We implement DFR (Kirichenko et al., 2023) as provided in the NFL codebase. DFR freezes a pretrained BERT model and the [CLS]-token representations are extracted, standardized, and used to fit an  $\ell_1$ -regularized logistic regression head on a randomly sampled small probe set of the training data (5%). The regularization strength is selected via cross-validation over  $\{1.0, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01\}$  using a 50/50 split of the probe set.

## B Training-Time Performance as an Upper Bound for Deployment-Time Mitigation

We prove that deployment-time shortcut mitigation faces a lower performance upper bound than training-time mitigation.

**Preliminaries.** Let  $\mathcal{X}, \mathcal{Y}, \mathcal{V}$  denote the input space (e.g., text sequences), the label space (e.g., sentiment classification), and the vocabulary from which the tokens are drawn, respectively. Let  $\mathcal{D}_{\text{train}} \in (\mathcal{X} \times \mathcal{Y})^N$  denote a training set of sample size N, and  $\mathcal{D}_{\text{test}} \in \mathcal{X}^M$  denote a test set of sample size M. We define  $S^* \subseteq \mathcal{V} \times \mathcal{Y}$  as the true spurious correlation structure yielded by the set of shortcut tokens (see the group definitions in Appendix A.1.1). We model  $S^*$  as a random variable taking values in a finite set  $\mathcal{S}$  with  $|\mathcal{S}| \geq 2$ . We decompose shortcut mitigation into two stages: *identification* and *intervention*. In the *identification* stage, we estimate the correlation structure  $S^*$  by either

training-time ( $\hat{S}_{train}$ ) or deployment-time methods ( $\hat{S}_{deploy}$ ). In the *intervention* stage, we adapt the model parameters  $\theta$  given  $\hat{S}_{train}$  or  $\hat{S}_{deploy}$ . We define  $I(S^*; \hat{S})$  as the mutual information between the true and estimated correlation structure, and  $H(S^*)$  as the entropy of  $S^*$ , reflecting the structure's complexity. We further define  $R(\hat{S}, S^*)$  as a scalar-valued mitigation performance (e.g., overall accuracy or worst-group accuracy) of the method that produces the estimate  $\hat{S}$ , and  $g(\theta, \mathcal{D}_{test})$  as all possible deployment-time observables.

**Assumption 1** (Markov chain). We assume that the following random variables form a Markov chain:

$$S^* \to \mathcal{D}_{\text{train}} \to \theta \to g(\theta, \mathcal{D}_{\text{test}}).$$

That is, conditioned on  $\mathcal{D}_{\text{train}}$ , the model parameters  $\theta$  are independent of  $S^*$ ; and conditioned on  $\theta$ , the deployment-time observables  $g(\theta, \mathcal{D}_{\text{test}})$  are independent of  $(\mathcal{D}_{\text{train}}, S^*)$ .

**Theorem 1** (Information Upper Bound). The mutual information between the true spurious structure  $S^*$  and any deployment-time estimate  $\hat{S}_{\text{deploy}}$  satisfies:

$$I(S^*;\, \hat{S}_{\text{deploy}}) \; \leq \; I(S^*;\, \theta) \; \leq \; I(S^*;\, \mathcal{D}_{\text{train}}).$$

In particular, defining  $\Delta I = I(S^*; \mathcal{D}_{\text{train}}) - I(S^*; \theta) \geq 0$ , the model parameters lose at least  $\Delta I$  units of information about  $S^*$  relative to the raw training data.

*Proof.* By Assumption 1,  $S^* \to \mathcal{D}_{train} \to \theta \to g(\theta, \mathcal{X}_{test})$  is a Markov chain. The Data Processing Inequality (DPI) states that for any Markov chain  $A \to B \to C$ ,  $I(A;C) \le I(A;B)$ . Applying the

DPI to the first three and last three elements of the chain yields

$$I(S^*; g(\theta, \mathcal{X}_{\text{test}})) \leq I(S^*; \theta) \leq I(S^*; \mathcal{D}_{\text{train}}).$$

Since  $\hat{S}_{\text{deploy}}$  is a deterministic function of  $g(\theta, \mathcal{X}_{\text{test}})$ , a further application of the DPI yields  $I(S^*; \hat{S}_{\text{deploy}}) \leq I(S^*; g(\theta, \mathcal{X}_{\text{test}}))$ . Combining these inequalities gives the result. Non-negativity of  $\Delta I$  follows directly from the first inequality.  $\square$ 

**Theorem 2** (Identification Error Bounds). Let  $S^*$  take values in the finite set S with  $|S| \ge 2$ . Define the Fano lower bounds on identification error:

$$L_{\text{deploy}} = \frac{H(S^*) - I(S^*; \theta) - 1}{\log(|\mathcal{S}| - 1)},$$
 (1)

$$L_{\text{train}} = \frac{H(S^*) - I(S^*; \mathcal{D}_{\text{train}}) - 1}{\log(|\mathcal{S}| - 1)}.$$
 (2)

Then the misidentification probabilities satisfy:

$$P(\hat{S}_{\text{deploy}} \neq S^*) \ge L_{\text{deploy}},$$
 (3)

$$P(\hat{S}_{\text{train}} \neq S^*) \ge L_{\text{train}},$$
 (4)

and  $L_{\rm deploy} \geq L_{\rm train}$ , i.e., the deployment-time error floor is at least as high as the training-time error floor.

*Proof.* Fano's Inequality states that for any discrete random variable X taking values in a set of size K and any estimator  $\hat{X}$  based on an observation Z:

$$P(\hat{X} \neq X) \ge \frac{H(X) - I(X; Z) - 1}{\log(K - 1)}.$$

Deployment-time bound (3): Since  $\hat{S}_{\text{deploy}}$  is a function of  $g(\theta, \mathcal{X}_{\text{test}})$ , which is itself a function of  $\theta$  (given the independent test inputs), we have  $I(S^*; \hat{S}_{\text{deploy}}) \leq I(S^*; \theta)$  by Theorem 1. Applying Fano's Inequality with  $X = S^*, \hat{X} = \hat{S}_{\text{deploy}}$ , and  $Z = \theta$  yields the result (noting that using  $\theta$  in place of  $g(\theta, \mathcal{X}_{\text{test}})$  can only decrease the Fano bound, so the inequality remains valid).

Training-time bound (4): The training-time estimator  $\hat{S}_{\text{train}}$  has access to  $\mathcal{D}_{\text{train}}$ . Applying Fano's Inequality with  $X = S^*$ ,  $\hat{X} = \hat{S}_{\text{train}}$ , and  $Z = \mathcal{D}_{\text{train}}$  yields the result.

Ordering: From Theorem 1, 
$$I(S^*; \theta) \leq I(S^*; \mathcal{D}_{\text{train}})$$
, so  $L_{\text{deploy}} \geq L_{\text{train}}$  holds.  $\square$ 

**Assumption 2** (Monotonicity). There exists a non-decreasing, differentiable function  $\rho:[0,1]\to\mathbb{R}$  with first-order derivative  $\rho'\geq 0$  such that:

$$\mathbb{E}[R(\hat{S}, S^*)] = \rho (1 - P(\hat{S} \neq S^*)),$$

where the expectation is taken over the randomness in the estimation of  $\hat{S}$ . That is, better identification of shortcuts yields better mitigation performance.

**Lemma 3** (Performance Bound from Identification Error). Under Assumption 2, any mitigation method whose identification error satisfies  $P(\hat{S} \neq S^*) \geq L$  for some  $L \in [0,1]$  has expected performance bounded by:

$$\mathbb{E}[R(\hat{S}, S^*)] \le \rho(1 - L).$$

In particular, combining with Theorem 2:

$$\mathbb{E}[R(\hat{S}_{\text{deploy}}, S^*)] \leq \rho(1 - L_{\text{deploy}}), \quad (5)$$

$$\mathbb{E}[R(\hat{S}_{\text{train}}, S^*)] \le \rho(1 - L_{\text{train}}). \tag{6}$$

*Proof.* Since  $P(\hat{S} \neq S^*) \geq L$ , we have  $1 - P(\hat{S} \neq S^*) \leq 1 - L$ . Because  $\rho$  is non-decreasing (Assumption 2):

$$\mathbb{E}[R(\hat{S}, S^*)] = \rho(1 - P(\hat{S} \neq S^*)) \le \rho(1 - L).$$

Equations (5) and (6) follow by substituting  $L = L_{\text{deploy}}$  and  $L = L_{\text{train}}$  from Theorem 2.

**Theorem 4** (Performance Upper Bound Comparison). Under Assumption 2, the performance upper bounds for deployment-time and training-time mitigation satisfy:

$$\rho(1 - L_{\text{deploy}}) \leq \rho(1 - L_{\text{train}}),$$

Moreover, the gap between the two bounds is:

$$\rho(1-L_{\text{train}})-\rho(1-L_{\text{deploy}}) = \rho'(\xi)\cdot\frac{\Delta I}{\log(|\mathcal{S}|-1)}$$

for some  $\xi \in [1 - L_{\text{deploy}}, 1 - L_{\text{train}}]$ , where  $\Delta I = I(S^*; \mathcal{D}_{\text{train}}) - I(S^*; \theta) \ge 0$ .

*Proof. Inequality:* By Theorem 2,  $L_{\rm deploy} \geq L_{\rm train}$ , which implies  $1 - L_{\rm deploy} \leq 1 - L_{\rm train}$ . Since  $\rho$  is non-decreasing (Assumption 2):

$$\rho(1 - L_{\text{deploy}}) \leq \rho(1 - L_{\text{train}}).$$

Gap characterisation: Since  $\rho$  is differentiable by Assumption 2, the Mean Value Theorem guarantees the existence of some  $\xi \in [1-L_{\rm deploy},\ 1-L_{\rm train}]$  such that:

$$\rho(1-L_{\text{train}})-\rho(1-L_{\text{deploy}}) = \rho'(\xi)\cdot(L_{\text{deploy}}-L_{\text{train}}),$$

where ρ ′ (ξ) is the first-order derivative of ρ at ξ. Substituting the definitions [\(1\)](#page-15-6) and [\(2\)](#page-15-7):

$$L_{\text{deploy}} - L_{\text{train}} = \frac{I(S^*; \mathcal{D}_{\text{train}}) - I(S^*; \theta)}{\log(|\mathcal{S}| - 1)}$$
$$= \frac{\Delta I}{\log(|\mathcal{S}| - 1)}.$$

Combining yields:

$$\rho(1-L_{\text{train}})-\rho(1-L_{\text{deploy}}) = \rho'(\xi)\cdot\frac{\Delta I}{\log(|\mathcal{S}|-1)}.$$

Since ρ ′ ≥ 0 and ∆I ≥ 0 (Theorem [1\)](#page-14-4), the gap is non-negative, confirming that the deployment-time performance ceiling is at most the training-time ceiling.

## C Extended Related Work

Shortcut Learning. Shortcut learning refers to the phenomenon where deep neural networks rely on superficial statistical patterns rather than taskrelevant features for prediction [\(Geirhos et al.,](#page-9-3) [2020\)](#page-9-3). This issue is particularly prevalent in natural language understanding, where pretrained language models such as BERT [\(Devlin et al.,](#page-8-0) [2019\)](#page-8-0) have been shown to exploit spurious correlations present in training data [\(Du et al.,](#page-8-2) [2023a;](#page-8-2) [Tu et al.,](#page-10-2) [2020\)](#page-10-2). A growing body of work has examined how these shortcuts manifest at the token level: specific words or phrases become disproportionately associated with target labels, causing the model to over-rely on their presence regardless of context [\(Wang et al.,](#page-10-1) [2022;](#page-10-1) [Du et al.,](#page-8-3) [2023b\)](#page-8-3). For instance, in natural language inference, annotation artifacts such as negation words and lexical overlap between premise and hypothesis serve as welldocumented shortcuts [\(Gururangan et al.,](#page-9-11) [2018;](#page-9-11) [McCoy et al.,](#page-9-12) [2019\)](#page-9-12). Recent work has further expanded the scope of analysis from individual tokens to concept-level correlations [\(Zhou et al.,](#page-10-9) [2024a\)](#page-10-9) and introduced controlled benchmarks with tunable shortcut strength for systematic evaluation [\(Zhou](#page-10-5) [et al.,](#page-10-5) [2024b\)](#page-10-5). While these studies provide valuable diagnostic insights, they primarily focus on characterizing the problem rather than addressing it under realistic deployment conditions.

Training-Time Shortcut Mitigation. A range of methods have been proposed to mitigate shortcut learning during model training, with progressively lighter supervision requirements. Group Distributionally Robust Optimization (Group DRO;

[Sagawa et al.,](#page-9-4) [2020\)](#page-9-4) directly optimizes worst-group performance but requires explicit annotations of shortcut occurrence for every training example. To relax this requirement, Just Train Twice (JTT; [Liu et al.,](#page-9-5) [2021\)](#page-9-5) identifies shortcut-vulnerable samples via a proxy model and upweights them during retraining, eliminating the need for group labels while still requiring full access to the training data. Ensemble-based approaches [\(Clark et al.,](#page-8-5) [2019\)](#page-8-5) train a bias-only model alongside the main model to downweight shortcut-reliant predictions, though they assume prior knowledge of the bias type. Deep Feature Reweighting (DFR; [Kirichenko et al.,](#page-9-6) [2023\)](#page-9-6) demonstrates that retraining only the last classification layer on a small group-balanced subset can recover robust performance, further reducing the retraining burden. More recently, NFL [\(Chew et al.,](#page-8-4) [2024\)](#page-8-4) applies counterfactual data augmentation and regularization to weaken spurious correlations without group labels. Despite this progression toward lighter assumptions, all of these methods still require some combination of training data access, label supervision, or prior knowledge of the shortcut type. Moreover, shortcut behavior is inherently distribution-dependent: correlations that are benign or even helpful during training may become harmful only when the deployment-time distribution shifts. None of these methods can adapt to such shifts after training, when the model is fixed and ground-truth labels are unavailable. This is precisely the setting we address in this work.

Adapting Models Beyond Training. A separate line of work in computer vision has explored testtime adaptation (TTA), where model parameters are updated using unlabeled test data to handle distribution shifts. Tent [\(Wang et al.,](#page-10-3) [2021\)](#page-10-3) adapts batch normalization layers by minimizing prediction entropy at test time, and subsequent work has improved its efficiency and stability [\(Niu et al.,](#page-9-13) [2022\)](#page-9-13). Other approaches adjust batch normalization statistics to the target distribution [\(Schnei](#page-9-9)[der et al.,](#page-9-9) [2020;](#page-9-9) [Nado et al.,](#page-9-10) [2020\)](#page-9-10) or introduce self-supervised auxiliary objectives for test-time training [\(Sun et al.,](#page-9-14) [2020\)](#page-9-14). However, [Zhao et al.](#page-10-4) [\(2023\)](#page-10-4) identify several failure modes of existing TTA methods, including sensitivity to batch size and the severity of distribution shift. More fundamentally, these methods are designed for vision architectures and rely on properties that do not transfer to text: batch normalization layers (absent in transformer encoders like BERT), continuous

pixel inputs (as opposed to discrete tokens), and spatial augmentations (which have no direct analogue in language). Furthermore, existing TTA methods target general distribution shift rather than the structured problem of token-level shortcut reliance. Our work addresses this gap by proposing a deployment-time adaptation framework specifically designed for mitigating token-level shortcuts in text classifiers, without requiring batch normalization or continuous input assumptions.

Gradient-Based Attribution and Contrastive Learning. Our method builds on two technical foundations. The first is gradient-based attribution, which estimates the contribution of each input feature to the model's prediction. Integrated Gradients [\(Sundararajan et al.,](#page-10-6) [2017\)](#page-10-6) provides an axiomatic framework for this purpose, while [Li](#page-9-15) [et al.](#page-9-15) [\(2016\)](#page-9-15) demonstrate that the simpler gradient × input method is effective for identifying influential tokens in NLP models. These techniques have been widely used for model interpretation, and more recently, [Du et al.](#page-8-10) [\(2022\)](#page-8-10) connect attribution to debiasing by using interpretation scores to guide a teacher-student training procedure. However, prior work treats attribution primarily as an explanatory tool or a training-time signal; no existing method leverages it as an operational mechanism for deployment-time intervention. The second foundation is contrastive learning. SimCLR [\(Chen](#page-8-7) [et al.,](#page-8-7) [2020\)](#page-8-7) establishes the general framework of learning representations by contrasting augmented views of the same input, and [Khosla et al.](#page-9-19) [\(2020\)](#page-9-19) extend it to the supervised setting with improved robustness. In NLP, SimCSE [\(Gao et al.,](#page-9-16) [2021\)](#page-9-16) adapts contrastive objectives to sentence encoders using dropout as minimal augmentation, and Fair-Fil [\(Cheng et al.,](#page-8-11) [2021\)](#page-8-11) applies contrastive learning to debias pretrained text representations with respect to social attributes. More closely related to our setting, C2L [\(Choi et al.,](#page-8-12) [2022\)](#page-8-12) combines contrastive learning with counterfactual augmentation to reduce reliance on spurious patterns, but still operates at training time with label supervision. Across these works, positive pairs are constructed through generic augmentations (dropout, random masking, synonym substitution) that are agnostic to which features the model actually relies on. Our method bridges these two lines by using gradient-based attribution to identify candidate shortcut tokens and constructing positive pairs through targeted masking of these tokens, so that

the contrastive objective directly discourages shortcut reliance at deployment time.

## D Ethics Considerations

Our work addresses the robustness of text classifiers to spurious correlations, which is directly relevant to fairness in NLP systems. For example, in toxicity detection, spurious associations between demographic identity terms and the toxic label can lead to biased predictions against marginalized groups. Our method provides a practical tool for mitigating such biases at deployment time without requiring sensitive group annotations. All datasets used in this work are publicly available and have been widely used in prior research. We rely on the consent and ethical review processes of the original dataset creators. We do not collect or annotate any new data involving human subjects.

## E Potential Risks

While our method reduces shortcut reliance, we acknowledge three potential risks. First, gradientbased attribution may mistakenly mask taskrelevant tokens, suppressing genuine predictive signals. Second, adversarial actors aware of our token-level assumption could craft inputs exploiting multi-token shortcuts that our method fails to detect. Third, imperfect debiasing may create a false sense of security in high-stakes applications such as toxicity detection, where residual bias against marginalized groups may remain. We encourage careful evaluation before deployment.