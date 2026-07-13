# Review

## Summary
The authors propose a unified framework for analyzing the quality of intermediate representations in large language models (LLMs) and vision models, challenging the common belief that final-layer embeddings are the most useful for downstream tasks. They introduce a set of metrics that assess representation quality from information-theoretic, geometric, and invariance perspectives, demonstrating that intermediate layers often outperform final layers across various downstream tasks. The study includes extensive experiments on 32 text-embedding tasks and multiple architectures, revealing that intermediate layers achieve a balance between retaining essential features and discarding noise, which contributes to stronger downstream performance.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
1. The authors propose a unified framework for analyzing intermediate layer representations in LLMs and vision models, providing a novel perspective that challenges the traditional reliance on final-layer embeddings.

2. The authors provide a solid theoretical basis for their framework, establishing connections between matrix-based entropy and various representation metrics.

3. The authors conduct extensive experiments across multiple architectures and scales, demonstrating the consistency of their findings and the robustness of their framework.

## Weaknesses
1. While the paper provides extensive empirical evidence, it lacks a deep theoretical explanation for why intermediate layers perform better in certain tasks.

2. The framework relies on several metrics that may be difficult to interpret or implement in practice.

## Questions
1. The authors mention that larger models exhibit more pronounced intermediate compression. Could you provide more quantitative analysis on how model size affects the representation quality of intermediate layers?

2. The paper focuses on language and vision models. Do you anticipate similar findings for other domains, such as audio or time-series data?

3. Can the proposed metrics be used to predict which intermediate layer would be most beneficial for a given task before actually performing the task?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4