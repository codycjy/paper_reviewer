# Review

## Summary
This paper proposes a federated learning method that aims to be robust to both prior and likelihood misspecification. The method uses generalized variational inference (GVI) as the basis for the federated learning algorithm. GVI is a general framework for variational inference that can accommodate different divergence measures and allows for robustness to model misspecification by placing less weight on the observed data. The authors extend GVI to the federated setting and provide theoretical guarantees for the convergence and robustness of the algorithm. The method is evaluated on several synthetic and real-world datasets, demonstrating improved robustness and predictive performance compared to existing federated learning approaches.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper provides a novel approach to federated learning that addresses the issue of model misspecification, which is a common problem in real-world applications of federated learning. The theoretical analysis of the algorithm is thorough, with guarantees for convergence and robustness. The experimental results are promising, showing that the method outperforms existing approaches in terms of robustness and predictive performance. The paper is well-written and clearly explains the methodology and results.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational complexity of the proposed method. Federated learning algorithms can be computationally expensive, especially when dealing with large datasets or a high number of clients. The proposed method involves computing the cavity distribution and optimizing the variational posterior at each iteration, which could be computationally intensive. The authors should provide an analysis of the computational complexity of the method and compare it to existing approaches. This would help to understand the practical feasibility of the method for large-scale applications.

2. The paper does not provide a thorough comparison with other state-of-the-art federated learning methods that address robustness and uncertainty quantification. While the authors compare the proposed method with some existing approaches, a more comprehensive comparison with a wider range of methods would strengthen the paper. This would help to better position the proposed method in the context of existing research and highlight its advantages and disadvantages more clearly.

## Questions
1. How does the computational complexity of the proposed method compare to existing federated learning approaches? Are there any computational limitations or bottlenecks in the method that could limit its scalability to large datasets or a high number of clients?

2. How does the proposed method perform compared to other state-of-the-art federated learning methods that address robustness and uncertainty quantification? A more comprehensive comparison with a wider range of methods would be helpful to better position the proposed method in the context of existing research.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4