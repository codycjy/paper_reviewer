# Review

## Summary
The paper introduces a generalized Franz-Parisi (GFP) criterion, an enhancement of the Franz-Parisi (FP) criterion for characterizing computational hardness in statistical detection problems. The original FP criterion, while useful, may not capture the geometric overlap structure of all statistical models adequately. The GFP criterion refines the FP by optimizing the overlap event inside the FP definition, subject to a mild symmetry assumption. The main theoretical result establishes that GFP criterion is equivalent to Statistical Query (SQ) lower bounds. This equivalence holds for a broad class of statistical models, including Gaussian additive models, planted sparse models, non-Gaussian component analysis (NGCA), single-index (SI) models, and convex truncation detection settings, provided they satisfy a mild, verifiable assumption.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper's main contribution is the introduction of the Generalized Franz-Parisi (GFP) criterion, which refines the original FP criterion by optimizing the overlap event. This optimization better captures the geometric structure of statistical models, making the criterion more versatile and applicable to a broader range of problems. The paper establishes the equivalence between the GFP criterion and Statistical Query (SQ) lower bounds, providing a rigorous connection between statistical physics-based heuristics and formal algorithmic complexity. This equivalence is significant as it extends the scope of the FP criterion, which was previously only fully proven to be equivalent to low-degree polynomial (LDP) lower bounds for Gaussian additive models. The paper demonstrates that the GFP criterion can characterize hardness beyond Gaussian additive models, including planted sparse models, NGCA, SI models, and convex truncation detection tasks. This broadens the applicability of the criterion to a wide range of statistical inference problems. The paper is well-structured and clearly written. The definitions, theorems, and proofs are presented in a manner that is accessible to readers with a background in statistical physics and computational complexity theory.

## Weaknesses
The paper's main weakness lies in the generality of Assumption 1, which forms the basis for the equivalence between the GFP and SQ frameworks. While the assumption is claimed to be mild and verifiable, the paper does not provide a comprehensive discussion of its implications and limitations. It would be beneficial to see a more detailed analysis of the types of statistical models that satisfy Assumption 1 but not the original FP criterion. Additionally, the paper could benefit from a more explicit discussion of the limitations of the GFP criterion itself. While the refinement offers improvements, it is unclear how much of a difference this makes in practice, especially given the complexity of the proofs involved. The practical utility of the GFP criterion for deriving new computational hardness results in real-world applications is not thoroughly explored. The paper primarily focuses on establishing the theoretical equivalence between the GFP and SQ frameworks but does not provide empirical validation or practical demonstrations of the new criterion's effectiveness. This lack of empirical evidence makes it difficult to assess the practical significance of the contribution. The paper would be strengthened by including empirical evaluations or case studies that demonstrate how the GFP criterion can lead to new insights or improved computational hardness results in practical settings. Overall, while the theoretical contribution is significant, the paper could be strengthened by providing a more comprehensive discussion of the practical implications and limitations of the GFP criterion.

## Questions
- Could the authors provide more examples or case studies where the GFP criterion leads to different or more refined hardness results compared to the FP criterion?
- Can the authors elaborate on the practical implications of the equivalence between the GFP and SQ frameworks? How does this equivalence facilitate the derivation of new computational hardness results or insights in practical settings?
- Could the authors discuss potential extensions of the GFP criterion to estimation problems, which are commonly encountered in practical statistical inference tasks?
- How does the optimization of the overlap event in the GFP criterion affect the interpretability of the hardness results? Does this optimization lead to more intuitive or actionable insights regarding the computational hardness of a given problem?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4