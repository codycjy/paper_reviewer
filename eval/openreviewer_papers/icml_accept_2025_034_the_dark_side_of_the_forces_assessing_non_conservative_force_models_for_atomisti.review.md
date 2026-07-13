# Review

## Summary
This paper investigates the applicability of non-conservative force models in microscopic simulations, identifying several fundamental issues, including ill-defined convergence of geometry optimization and instability in various types of molecular dynamics. It concludes that the best approach to exploit the acceleration afforded by direct forces is to use them in conjunction with conservative forces.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-organized and easy to follow.

2. The topic of non-conservative force models is both interesting and important.

3. The experiments are thorough and well-executed.

## Weaknesses
1. The primary concern is the limited novelty. The issues of ill-defined convergence of geometry optimization and instability in various types of molecular dynamics for non-conservative force models have been discussed in previous works, such as [1] and [2]. Additionally, the idea of using conservative force models as a reference and non-conservative force models for acceleration is also discussed in [2]. Therefore, the paper does not appear to offer new insights or contributions.

[1] Li, Ziqi, et al. "Molecular dynamics with on-the-fly machine learning of quantum-mechanical forces." Physical Review Letters 114.9 (2015): 096405.

[2] Fu, Xiang, et al. "Learning Smooth and Expressive Interatomic Potentials for Physical Property Prediction." arXiv preprint arXiv:2502.12147 (2025).

2. Another concern is the limited applicability of the proposed method. The idea of using conservative force models as a reference and non-conservative force models for acceleration is only applicable when the non-conservative force models are more accurate than the conservative force models. However, in Table 1, the non-conservative force model PET-NC shows significantly higher errors in both energy and force compared to the conservative force model PET-C. This suggests that the proposed method may not be widely applicable.

## Questions
1. The paper states that the non-conservative force model PET-NC shows significantly higher errors in both energy and force compared to the conservative force model PET-C. However, in Appendix B, the authors mention that backward gradient computations are around twice as expensive as the corresponding forward function evaluation. Given that the non-conservative model has a higher error, why is the backward gradient computation not more expensive?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4