# Review

## Summary
This paper considers the problem of estimating heterogeneous effects using generalized random forests (GRFs). The authors propose an efficient algorithm to build the tree-based partitioning needed for GRFs, which replaces the gradient-based splitting criterion used in the standard GRF algorithm with a fixed-point approximation. The authors prove that the resulting estimator is consistent and asymptotically normal. They also demonstrate the efficiency of their method through simulations and real data analysis.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The proposed algorithm is a significant improvement over the standard GRF algorithm, which can be computationally expensive and unstable in large dimensions. The new algorithm maintains the same statistical properties as GRF while being much faster to compute. 
- The paper provides a thorough theoretical analysis of the proposed estimator, including proofs of consistency and asymptotic normality. The authors also conduct extensive simulations to evaluate the performance of their method compared to the standard GRF algorithm. They consider different scenarios and provide detailed results and discussion. 
- The paper is well-written and organized. The authors provide a clear motivation for their work and a detailed explanation of their proposed method. They also provide pseudocode for their algorithm and detailed descriptions of their simulations.

## Weaknesses
- The authors only consider the case of estimating heterogeneous effects for a fixed set of covariates. However, in many practical applications, the covariates can take different values in the training and testing data. The proposed method is not directly applicable to this setting, which is handled by the standard GRF algorithm. The authors should discuss this limitation and potentially suggest ways to extend their method to handle this case. 
- The authors only compare their method to the standard GRF algorithm. However, there are other methods for estimating heterogeneous effects that have different computational and statistical properties. The authors should consider comparing their method to other approaches, such as local linear regression, kernel methods, or boosting, to provide a more comprehensive evaluation of their method. 
- The authors do not provide any intuition or interpretation for the results from the real data analysis. They should provide a discussion of the results, including what the estimated effects mean in the context of the application and how they compare to existing knowledge or previous estimates. 
- The authors do not provide any code for their method. While the pseudocode is provided, having access to the actual implementation would allow for better reproducibility and validation of the results.

## Questions
- How does the proposed method handle the case where the covariates can take different values in the training and testing data? Can the method be extended to handle this case? 
- How does the proposed method compare to other approaches for estimating heterogeneous effects, such as local linear regression, kernel methods, or boosting? 
- Can the authors provide more intuition or interpretation for the results from the real data analysis? What do the estimated effects mean in the context of the application, and how do they compare to existing knowledge or previous estimates?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4