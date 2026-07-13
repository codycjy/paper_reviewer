# Review

## Summary
This paper proposes a novel structural feature called Graph Invariant Structural Trait (GIST) for graph classification. GIST estimates the intersection cardinality of k-hop neighborhoods of node pairs to capture substructures within a graph. The authors integrate GIST into graph transformers by incorporating it into the attention mechanism. The paper provides both theoretical analysis and empirical evidence demonstrating the effectiveness of GIST in capturing structural information critical for graph classification. Extensive experiments on various graph classification benchmarks show that graph transformers incorporating GIST achieve superior performance compared to state-of-the-art baselines.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper introduces a novel structural feature, GIST, which is designed to capture substructures within a graph through estimated pairwise node intersections. This approach addresses the challenge of effectively encoding graph structure information within the all-to-all attention mechanism of graph transformers.

2. The authors provide both theoretical analysis and empirical observations to demonstrate the effectiveness of GIST in capturing structural information critical for graph classification. The theoretical analysis shows that GIST is a graph-invariant representation, and the empirical observations demonstrate its ability to capture substructures and enhance structural awareness in self-attention mechanisms.

3. The paper presents extensive experiments on various graph classification benchmarks to evaluate the performance of GIST-augmented graph transformers. The results show consistent performance improvements compared to state-of-the-art baselines, demonstrating the practical effectiveness of GIST.

## Weaknesses
1. The motivation of this paper is not clear. The authors argue that existing methods struggle to effectively capture and represent substructures, but they do not provide a clear definition of what constitutes a "substructure" in this context. Additionally, the paper does not explain how GIST can address these issues or why it is particularly effective for capturing substructures.

2. The novelty of this paper is limited. The concept of using the intersection of two nodes' k-hop neighborhoods to construct features is not new and has been explored in previous works, such as [1]. The paper does not sufficiently differentiate itself from these existing methods or provide a clear explanation of the advantages of GIST over them.

3. The paper lacks a comprehensive discussion of related works. While it mentions some existing methods for improving graph transformers, it does not provide a detailed comparison with these methods or explain how GIST offers improvements in terms of substructure capture or overall performance.

[1] Knowledge Graphs Can Be Learned with Just Intersection Features. ICML 2024.

## Questions
1. How does GIST define "substructure"? What is the difference between "substructure" and "neighborhood"?

2. How does GIST differ from or improve upon existing methods that use the intersection of two nodes' k-hop neighborhoods?

3. Can the authors provide a more detailed comparison between GIST and other methods for improving graph transformers?

4. How does GIST handle large-scale graphs? What is the computational complexity of GIST compared to other methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4