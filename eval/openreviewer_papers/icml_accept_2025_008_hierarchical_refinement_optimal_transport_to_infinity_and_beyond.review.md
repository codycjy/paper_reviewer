# Review

## Summary
The authors propose a hierarchical algorithm to compute the optimal transport coupling between two datasets. The method is based on recursively applying a low-rank OT algorithm to smaller subsets of the data. The authors prove that the optimal low-rank coupling co-clusters points with their image under the Monge map. They show that their algorithm recovers the Monge map and provide a bound on the cost difference across scales. The algorithm is evaluated on synthetic and real-world datasets, demonstrating its ability to compute couplings between large-scale datasets.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
The paper is well-written and easy to follow. The idea of using low-rank OT in a hierarchical manner is novel and interesting. The authors provide a solid theoretical foundation for their algorithm, proving that the optimal low-rank coupling co-clusters points with their image under the Monge map. The algorithm is evaluated on both synthetic and real-world datasets, showing its effectiveness in computing couplings between large-scale datasets. The paper addresses the important problem of scaling optimal transport to large datasets, which has many applications in machine learning and other fields. The algorithm proposed in the paper seems to be more efficient than existing methods for computing optimal transport couplings between large datasets.

## Weaknesses
The paper does not provide a detailed analysis of the computational complexity of the proposed algorithm. While the authors mention that the algorithm has linear space complexity and log-linear time complexity, a more in-depth analysis would be beneficial. It would be helpful to compare the computational complexity of the algorithm to that of other methods for computing optimal transport couplings between large datasets.

The paper does not provide a detailed discussion of the limitations of the proposed algorithm. It would be beneficial to address any potential limitations or challenges in applying the algorithm to real-world datasets.

## Questions
- Can you provide more details on the computational complexity of the proposed algorithm? How does it compare to other methods for computing optimal transport couplings between large datasets?
- How does the proposed algorithm perform on datasets with varying sizes and complexities? It would be helpful to provide more detailed experimental results and analysis.
- Can you provide more details on the practical applications of the proposed algorithm? Are there any specific domains or fields where this algorithm would be particularly useful?
- How sensitive is the algorithm to the choice of hyperparameters, such as the rank schedule? It would be helpful to provide guidance on selecting appropriate hyperparameters for different datasets.
- How does the algorithm handle noisy or incomplete data? It would be beneficial to provide more details on the robustness of the algorithm.
- Can you provide more details on the scalability of the proposed algorithm? How does it perform on datasets with millions or billions of points?
- How does the algorithm compare to other state-of-the-art methods for computing optimal transport couplings between large datasets? It would be helpful to provide a more comprehensive comparison.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4