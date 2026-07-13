# Review

## Summary
This paper presents GraphPack, a query-aware GraphRAG framework that addresses limitations in existing approaches by formulating subgraph selection as a 0-1 knapsack optimization problem. For each natural language query, GraphPack selects the most informative subgraph under a size constraint by jointly maximizing semantic relevance and minimizing structural redundancy. The selected subgraph is encoded using a query-aware graph encoder whose parameters are conditioned on the query, allowing node representations to adapt dynamically to user intent. Extensive experiments on multiple knowledge-intensive graph benchmarks demonstrate that GraphPack achieves state-of-the-art performance, highlighting its effectiveness in addressing structural and contextual challenges in various settings, including supervised learning, cross-domain applications, and zero-shot scenarios.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The idea of using the knapsack problem to improve graph retrieval is interesting.
3. The experiments are comprehensive, covering various datasets and tasks.

## Weaknesses
1. The motivation for using a knapsack problem to select a subgraph is not clear. Why is this approach better than directly using a GNN to select a subgraph?
2. The time efficiency of the proposed method is a concern. For each query, the method first identifies anchor nodes and then solves the knapsack problem. How does the time complexity of the proposed method compare to that of the baseline?
3. In Table 1, the proposed GraphPack does not show significant improvements over LLaGA, especially on the Instagram dataset.
4. In Table 5, the zero-shot results of GraphPack are not impressive.
5. There is no discussion on the limitations of the proposed method.

## Questions
See the weaknesses above.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4