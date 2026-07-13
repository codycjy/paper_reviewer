# Review

## Summary
This paper proposes a novel invariant and metric for unordered point clouds under rigid motion. The invariant is based on distributed projections of the point cloud onto a set of ordered points, combined with the distance of the point to the origin. The metric is based on the bottleneck distance between point clouds. The authors prove that the invariant is complete and Lipschitz-continuous, and that the metric satisfies the metric axioms. The invariant and metric are computable in polynomial time. The authors also apply their invariant and metric to a molecular dataset, and show that they can predict the chemical element of a molecule with high accuracy using only the invariant.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The proposed invariant and metric are novel, and satisfy desirable properties such as completeness, Lipschitz continuity, and computability. The invariant and metric are also applied to a real-world dataset, and the authors show that they can be used to solve a practical problem (predicting the chemical element of a molecule).

## Weaknesses
The paper does not provide any theoretical lower bounds or upper bounds on the complexity of computing the invariant or metric. While the invariant and metric are computable in polynomial time, it is unclear how efficient they are in practice for large point clouds. The paper does not provide any empirical comparisons with other methods for computing invariants or metrics for point clouds. It would be helpful to see how the proposed invariant and metric compare to other methods in terms of computational efficiency and accuracy.

## Questions
* Can you provide more details on the computational complexity of your invariant and metric? How does the complexity scale with the number of points in the cloud?
* How does the accuracy of your method for predicting chemical elements compare to other state-of-the-art methods?
* Have you considered any other applications of your invariant and metric besides predicting chemical elements? How generalizable is your method to other types of point cloud data?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4