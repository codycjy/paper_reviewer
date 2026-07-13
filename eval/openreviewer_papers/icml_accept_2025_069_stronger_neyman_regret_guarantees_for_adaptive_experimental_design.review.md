# Review

## Summary
This paper studies the design of adaptive, sequential experiments for unbiased average treatment effect (ATE) estimation in the design-based potential outcomes setting. The authors propose adaptive designs with substantially stronger Neyman regret guarantees. They modify ClipOGD to obtain anytime $\widetilde{O}(\log T)$ Neyman regret under natural boundedness assumptions. They also introduce and study a class of contextual "multigroup" Neyman regret guarantees: Given any set of possibly overlapping groups based on the covariates, the adaptive design outperforms each group's best non-adaptive designs.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
This paper proposes adaptive designs with substantially stronger Neyman regret guarantees, and introduce and study a class of contextual "multigroup" Neyman regret guarantees.

## Weaknesses
The main weakness of this paper is that the proposed method is limited to the design-based setting, while the target parameter is the superpopulation ATE. It is known that the design-based ATE is biased for the superpopulation ATE, and the bias can be large if the treatment assignment is not random (Dai et al., 2023). The proposed method is not applicable when the target parameter is the design-based ATE, and the performance may be poor when the target parameter is the superpopulation ATE.

## Questions
1. The main weakness of this paper is that the proposed method is limited to the design-based setting, while the target parameter is the superpopulation ATE. It is known that the design-based ATE is biased for the superpopulation ATE, and the bias can be large if the treatment assignment is not random (Dai et al., 2023). The proposed method is not applicable when the target parameter is the design-based ATE, and the performance may be poor when the target parameter is the superpopulation ATE. The authors should discuss this issue in the paper.

2. The authors should give the definition of $p^*_{T,G}$ in Definition 4.1.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4