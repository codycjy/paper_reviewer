# Review

## Summary
The paper introduces SPLIT, a family of algorithms designed to optimize decision trees, balancing accuracy and scalability. Traditional methods for optimizing decision trees either rely on greedy algorithms, which are fast but suboptimal, or dynamic programming with branch and bound, which are optimal but computationally expensive. The SPLIT algorithms aim to bridge this gap by employing a sparse lookahead approach: they use greedy splitting close to the leaves of the tree, where there are fewer samples and less complex decision points, and switch to dynamic programming closer to the root. This strategy allows the algorithms to retain the accuracy of optimal decision trees while achieving the scalability of greedy methods. The authors also extend this approach to compute the Rashomon set, the collection of near-optimal decision trees. The paper provides theoretical proofs of the scalability and performance guarantees of the SPLIT algorithms and presents empirical results demonstrating their efficiency and accuracy compared to existing methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper introduces a novel approach to decision tree optimization that combines the speed of greedy algorithms with the accuracy of optimal decision trees through a sparse lookahead mechanism. This is an innovative solution to the longstanding problem of balancing efficiency and performance in decision tree learning.

The authors provide a solid theoretical foundation for their algorithms, including proofs of scalability and optimality. The empirical results are extensive and demonstrate the practical benefits of the SPLIT algorithms in terms of runtime and accuracy across multiple datasets.

The paper is well-organized and clearly written. The authors effectively explain the motivation behind their work, the details of the algorithms, and the results. The use of figures and tables to illustrate the performance improvements further enhances the clarity of the presentation.

## Weaknesses
1. The paper does not provide a detailed analysis of the limitations of the SPLIT algorithms or potential scenarios where they might not perform as expected. Understanding these limitations is crucial for practical applications.

2. While the paper compares the SPLIT algorithms to existing methods, it does not include a comprehensive comparison with all relevant approaches in the field. There may be other algorithms that were not considered in the evaluation.

3. The paper does not discuss the sensitivity of the SPLIT algorithms to hyperparameters or provide guidelines for selecting these parameters. This could be a challenge for practitioners who need to tune the algorithms for their specific use cases.

## Questions
1. How does the choice of lookahead depth impact the performance and runtime of the SPLIT algorithms? Is there a heuristic or guideline for selecting this parameter?

2. Can the SPLIT algorithms be extended to handle continuous features, and if so, how would this affect the computational complexity and performance?

3. How does the SPLIT algorithm perform on very large datasets or in high-dimensional spaces? Are there any specific challenges or limitations in these scenarios?

4. The paper mentions the computation of the Rashomon set. How scalable is this computation in practice, and what are the implications for large-scale datasets?

5. Are there any specific domains or applications where the SPLIT algorithms are expected to be particularly beneficial or potentially less effective?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4