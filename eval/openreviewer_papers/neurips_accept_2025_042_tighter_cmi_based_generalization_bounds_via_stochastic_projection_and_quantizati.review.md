# Review

## Summary
This paper studies information-theoretic generalization bounds, in particular CMI-based bounds. By applying a technique of stochastic projection and lossy compression, the authors show that CMI-based bounds can be improved and overcome the counterexamples constructed in recent work by Attias et al. [2024] and Livni [2023]. The authors also discuss the implications of their results on the memorization problem.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. 
- The authors provide a simple yet effective technique to improve CMI-based bounds. The construction of the lossy algorithm is novel and interesting.
- The authors show that their new bounds overcome the counterexamples constructed in recent work by Attias et al. [2024] and Livni [2023], which is a significant contribution.

## Weaknesses
- The construction of the lossy algorithm seems to rely heavily on the fact that the super-sample size is $2n$. It is not clear whether the results can be extended to the case of a general super-sample size.
- The paper is purely theoretical, and it is not clear how the results can be used in practice to improve the generalization of learning algorithms.

## Questions
- Is it possible to extend the results to the case of a general super-sample size? If not, what are the main challenges?
- Can the results be used in practice to improve the generalization of learning algorithms?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4