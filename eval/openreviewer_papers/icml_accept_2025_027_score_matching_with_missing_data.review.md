# Review

## Summary
This paper proposes two methods to extend score matching to the setting with missing data. The first method uses importance weighting to estimate the marginal scores, and the second method uses variational inference to estimate the conditional distributions. The paper also provides finite sample bounds for the proposed methods. Experiments on synthetic and real-world datasets demonstrate the effectiveness of the proposed methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation for the problem and a thorough review of the related work.
2. The proposed methods are novel and well-motivated. The importance weighting method is simple and easy to implement, while the variational method has the potential to scale to high-dimensional problems.
3. The theoretical results are rigorous and well-explained. The authors provide finite sample bounds for the proposed methods and discuss the conditions under which the bounds are tight.
4. The experiments are comprehensive and convincing. The authors evaluate the proposed methods on both synthetic and real-world datasets and compare them to several baseline methods. The results show that the proposed methods outperform the baselines in terms of estimation accuracy and computational efficiency.

## Weaknesses
1. The authors only consider the setting where the missing data are missing completely at random (MCAR). It would be interesting to see how the proposed methods perform in the setting where the missing data are missing not at random (MNAR).
2. The variational method requires the evaluation of high-dimensional integrals, which can be computationally intensive. The authors could discuss some potential ways to reduce the computational cost, such as variational inference with sparse Gaussian processes.
3. The authors could provide some guidance on how to choose the hyperparameters for the variational method, such as the number of samples used for importance weighting and the number of variational steps.

## Questions
See Weaknesses

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4