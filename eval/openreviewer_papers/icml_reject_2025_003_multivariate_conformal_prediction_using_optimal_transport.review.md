# Review

## Summary
The paper introduces a novel approach to multivariate conformal prediction (CP) by leveraging optimal transport (OT) theory to establish a natural extension of ranking scores to multidimensional spaces. The authors propose OT-CP, which uses optimal transport mappings to construct conformal prediction sets for multivariate outputs, preserving distribution-free coverage guarantees. The method employs the entropic map, computed from solutions to the Sinkhorn problem, to reduce the dimensionality of vector-valued scores, allowing the application of univariate CP techniques. The paper provides theoretical guarantees for the coverage of the predicted regions and demonstrates the method's effectiveness through experiments on a benchmark of regression tasks, comparing it with other multivariate CP approaches.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper introduces a novel approach by combining optimal transport with conformal prediction, which is a significant contribution to the field of multivariate CP.
2. The authors provide a rigorous theoretical framework for their method, including proofs of coverage guarantees, which adds credibility to their approach.
3. The paper is well-structured and clearly written, with detailed explanations of the methodology and theoretical underpinnings.

## Weaknesses
1. While the paper demonstrates the effectiveness of OT-CP on regression tasks, it would be beneficial to see its performance on other types of multivariate data or problems, such as classification.
2. The paper could provide more insight into how the choice of hyperparameters, particularly the entropic regularization parameter and the number of points for discretizing the sphere, affects the performance of the method.
3. A more detailed comparison with other state-of-the-art multivariate CP methods, including their strengths and weaknesses, would enhance the paper's contribution.

## Questions
1. How does the computational complexity of OT-CP compare to other multivariate CP methods, especially for high-dimensional data?
2. Can the authors provide more examples or case studies to illustrate the practical applications and advantages of OT-CP?
3. How sensitive is the performance of OT-CP to the choice of hyperparameters, and are there any guidelines for selecting these parameters?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4