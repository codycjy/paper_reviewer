# Review

## Summary
The paper explores how to optimally scale inference computation for retrieval augmented generation (RAG) to effectively utilize long-context large language models (LLMs). The authors introduce two strategies, Demonstration-based RAG (DRAG) and Iterative Demonstration-based RAG (IterDRAG), to manage the increased context and computation. DRAG incorporates extensive retrieved documents within demonstrations to improve the model's ability to extract relevant information, while IterDRAG decomposes complex queries into simpler sub-queries, using interleaved retrieval to enhance knowledge extraction and reasoning.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-structured, with clear explanations of the proposed strategies and their implementation. The authors provide detailed experimental results and analyses, supporting their claims with empirical evidence.

2. The authors conduct extensive experiments on benchmark QA datasets, demonstrating the effectiveness of their strategies in improving RAG performance.

## Weaknesses
1. The paper's focus on long-context retrieval augmented generation is highly specialized and may have limited applicability to other areas of natural language processing or general language tasks. The proposed strategies are tailored to specific scenarios and may not be easily adaptable to different types of tasks or datasets.

2. The authors do not provide a detailed analysis of the computational complexity or resource requirements of their proposed strategies. Inference scaling often involves trade-offs between performance gains and computational costs, and a deeper exploration of these aspects would strengthen the paper.

3. The paper could benefit from a more comprehensive comparison with existing methods in the literature. While the authors compare their strategies with some baselines, a broader comparison with state-of-the-art methods in long-context RAG and other relevant approaches would provide a better context for evaluating the effectiveness of their proposals.

## Questions
See the weakness above.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4