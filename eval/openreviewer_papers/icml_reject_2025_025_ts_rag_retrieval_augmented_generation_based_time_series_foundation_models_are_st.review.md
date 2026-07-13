# Review

## Summary
The paper introduces TS-RAG, a retrieval-augmented generation framework designed to improve zero-shot forecasting by enhancing time series foundation models (TSFMs) with external knowledge. TS-RAG retrieves relevant time series patterns from a dedicated knowledge database, using a pre-trained TSFM encoder and a learnable Mixture-of-Experts (MoE) module to integrate these patterns with the input query. This approach claims to improve generalization and interpretability without task-specific fine-tuning. Empirical results on seven benchmark datasets show that TS-RAG outperforms existing TSFMs, achieving up to a 6.51% improvement in forecasting accuracy.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-structured and clearly written, making it accessible to readers from both time series and NLP backgrounds.
2. The paper presents a novel application of Retrieval-Augmented Generation (RAG) to time series forecasting, effectively adapting concepts from NLP to a new domain.
3. The paper provides extensive empirical validation, demonstrating that TS-RAG achieves state-of-the-art performance across multiple datasets and outperforms existing TSFMs.

## Weaknesses
1. While the paper claims interpretability as a key benefit, it lacks a rigorous analysis of how interpretability is improved. The case studies only demonstrate that the model captures similar patterns, which is expected and does not fully justify the interpretability claim.
2. The paper does not sufficiently discuss the computational overhead introduced by the retrieval process and the MoE module, which could be significant for real-time applications.
3. The paper does not sufficiently discuss the potential for overfitting, especially given the use of a dedicated knowledge database specific to the training set.
4. The paper does not explore how TS-RAG performs with varying amounts of training data or in scenarios with limited labeled data, which could be a significant limitation in practical applications.
5. The paper does not sufficiently discuss how TS-RAG performs across different time series tasks beyond zero-shot forecasting, such as classification or imputation.
6. The paper does not sufficiently discuss the robustness of TS-RAG to noisy or adversarial data, which is critical for real-world applications.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4