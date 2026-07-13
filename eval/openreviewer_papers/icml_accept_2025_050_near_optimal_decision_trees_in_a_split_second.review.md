# Review

## Summary
This paper presents SPLIT (SParse Lookahead for Interpretable Trees), a family of algorithms that aims to balance the scalability of greedy methods with the accuracy of optimal decision tree algorithms. By leveraging the observation that near-optimal trees can be achieved through greedy splits close to the leaves, SPLIT significantly reduces computational complexity while maintaining high performance. The authors extend this approach to compute the Rashomon set of near-optimal trees efficiently. Theoretical analysis and empirical results demonstrate SPLIT's speed and accuracy, outperforming existing methods by orders of magnitude in runtime while preserving the interpretability and sparsity of optimal decision trees.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel approach to decision tree optimization that combines the speed of greedy methods with the accuracy of optimal trees by using sparse lookahead.
2. The theoretical analysis and empirical results are comprehensive, showing significant improvements in runtime and scalability without sacrificing accuracy.
3. The extension to compute the Rashomon set efficiently is a valuable contribution, enabling the scalable approximation of near-optimal trees.
4. The algorithms are implemented in a practical way, making them immediately usable in real-world applications.

## Weaknesses
1. The paper could benefit from more detailed comparisons with other recent methods in decision tree optimization, particularly those focusing on scalability and sparsity.
2. While the empirical results are strong, the theoretical analysis could be further developed to provide more insights into the algorithm's performance guarantees.
3. The scalability of the algorithms to extremely large datasets or highly imbalanced data is not fully explored.
4. The choice of hyperparameters, such as lookahead depth, could be discussed in more detail, including guidelines for their selection.

## Questions
1. How does SPLIT perform on extremely large datasets or in scenarios with a significant imbalance of classes?
2. Can the authors provide more insights into the selection of lookahead depth? Are there general guidelines that practitioners can follow?
3. How does SPLIT compare to other recent methods in decision tree optimization that also emphasize scalability and sparsity?
4. Can the authors elaborate on the potential limitations of SPLIT in terms of interpretability compared to more traditional decision tree methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4