# Review

## Summary
The paper proposes a method for constructing prediction sets that has the same asymptotic coverage guarantees as conformal prediction while providing a richer characterization of the distribution of possible prediction sets. The method is tested on synthetic data and MS-COCO.

## Soundness
4

## Presentation
3

## Contribution
3

## Strengths
The paper is well-written and clear. The proposed method is novel and interesting, and the paper does a good job of explaining why it is an interesting approach. The experimental results are compelling.

## Weaknesses
The main weakness of the paper is that the experiments are somewhat limited. The method is only tested on one real-world dataset (MS-COCO) and one synthetic dataset (heteroskedastic). The method is also only compared to two baselines: conformal risk control and risk-controlling prediction sets. It would be interesting to see how the method compares to other approaches, such as [1] and [2], which also seek to characterize the distribution of prediction sets.

[1] Vovk, V., Shen, J., Manokhin, V., and Xie, M. Nonparametric predictive distributions based on conformal prediction. In Proceedings of the Sixth Workshop on Conformal and Probabilistic Prediction and Applications, pp. 82–102. PMLR, May 2017.

[2] Prinster, D., Stanton, S., Liu, A., and Saria, S. Conformal validity guarantees exist for any data distribution (and how to find them). arXiv preprint arXiv:2402.02070, 2024.

## Questions
- Why is only heteroskedastic synthetic data used? It would be interesting to see how the method performs on data with other types of covariate dependence.
- Why are the baselines limited to risk control and risk-controlling prediction sets? It would be interesting to see how the method compares to other approaches that seek to characterize the distribution of prediction sets.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4