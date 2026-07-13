# Review

## Summary
The paper studies the problem of adaptive experimental design to estimate the average treatment effect (ATE) with low variance. In particular, it builds upon recent work by Dai et al. (2023) which introduced ClipOGD, the first method to achieve sublinear expected Neyman regret. This paper proposes two main contributions: (1) a modified version of ClipOGD that achieves logarithmic Neyman regret under a stricter assumption on the potential outcomes, and (2) a contextual version of the algorithm that achieves low multigroup regret (i.e., low regret for any predefined groups of experimental units). The paper also provides empirical validation of the proposed algorithms through simulations and real-world data.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper makes novel theoretical contributions to a relevant problem in experimental design. The problem of designing adaptive experiments that can estimate the ATE with low variance is important in many practical applications, and the paper provides significant improvements over the existing state-of-the-art.
- The paper is well-written and easy to follow. The authors do a good job of explaining the problem setting, the related work, and their contributions.
- The theoretical results are non-trivial and require technical sophistication. The authors make use of advanced techniques from online learning and statistical learning theory to derive their results.
- The empirical results support the theoretical findings and demonstrate the practical effectiveness of the proposed algorithms.

## Weaknesses
- The assumption made for the stronger regret bound (Assumption 3.1) is not justified. The authors should provide more intuition and examples to illustrate when this assumption is reasonable and when it is restrictive.
- The paper does not provide any theoretical lower bounds, so it is unclear if the logarithmic regret bound is optimal or can be further improved. The authors should discuss the limitations of their approach and potential directions for future research.
- The empirical evaluation is somewhat limited. The authors only consider two datasets (one synthetic and one real-world) and compare their method to a baseline. They should consider more diverse datasets and compare to more baselines, especially other recent methods for adaptive experimental design.

## Questions
- Can you provide more intuition and examples to justify Assumption 3.1? How restrictive is this assumption compared to the one made by Dai et al. (2023)?
- Do you have any thoughts on whether the logarithmic regret bound is optimal? What are the main challenges in obtaining better regret bounds?
- How does your method perform compared to other recent approaches for adaptive experimental design, such as those mentioned by Dai et al. (2023)?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4