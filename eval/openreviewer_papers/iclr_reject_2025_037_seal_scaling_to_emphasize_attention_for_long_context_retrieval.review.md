# Review

## Summary
This paper introduces SEAL (Scaling to Emphasize Attention for Long-context retrieval), a novel learning-based method to improve long-context retrieval in large language models (LLMs). The approach is based on the observation that specific attention heads or channels significantly influence retrieval performance. SEAL fine-tunes the strength of these components using a small amount of task-specific data, enhancing long-context retrieval accuracy with minimal computational overhead. The authors demonstrate SEAL's effectiveness across various benchmarks, including LongEval and Needle-in-a-Haystack tasks, and show that it can be integrated with training-free context extension methods to further boost performance.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper identifies a key limitation in LLMs' retrieval capabilities for long contexts and proposes a targeted solution.
- The authors provide a clear motivation through preliminary experiments, showing how specific attention heads impact retrieval performance.
- SEAL is a lightweight, parameter-efficient method that achieves significant improvements with only 50 samples and minimal parameter tuning.
- The approach is evaluated across multiple tasks and models, demonstrating generalization ability and robustness.
- SEAL can be combined with training-free context extension methods, extending its applicability and potential impact.

## Weaknesses
- The method is primarily evaluated on retrieval tasks. Its effectiveness on other long-context tasks, such as document summarization or long-form QA, is not explored.
- While SEAL shows improvements, it does not consistently outperform full-parameter fine-tuning (SEAL-L) in terms of accuracy.
- The approach is heavily based on the idea that specific attention heads are crucial for retrieval. However, this assumption may not generalize well across different models or tasks, potentially limiting its broader applicability.
- The paper does not provide a detailed analysis of how SEAL affects the model's performance on shorter contexts or more general tasks.

## Questions
- How does SEAL perform on other long-context tasks beyond retrieval, such as document summarization or long-form QA?
- Have you evaluated the impact of SEAL on models with shorter context lengths (e.g., 4k context)? Does it degrade performance for these cases?
- How does SEAL compare to full-parameter fine-tuning in terms of computational cost and performance trade-offs?
- Can you provide more insights into how SEAL affects the model's internal mechanisms? For example, are certain layers or attention patterns more important for retrieval?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4