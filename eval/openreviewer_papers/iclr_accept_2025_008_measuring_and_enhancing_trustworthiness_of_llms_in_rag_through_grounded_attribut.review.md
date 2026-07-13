# Review

## Summary
This paper introduces a new metric called TRUST-SCORE to measure the trustworthiness of LLMs in the context of Retrieval-Augmented Generation (RAG). The authors highlight the limitations of existing metrics in evaluating LLMs' performance in RAG systems and propose TRUST-SCORE to address these gaps. The metric assesses an LLM's ability to answer questions based on provided documents, the correctness of its answers, the quality of its citations, and its ability to refuse to answer when necessary. The paper also presents TRUST-ALIGN, a method to align LLMs for improved TRUST-SCORE performance using a constructed dataset of questions, documents, and model responses.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper addresses a significant gap in the evaluation of LLMs in RAG systems by focusing on the trustworthiness of LLMs, which is crucial for the reliability and safety of these systems.

2. The proposed TRUST-SCORE metric is comprehensive, considering multiple aspects of an LLM's performance, including response truthfulness, attribution groundedness, and refusal capability.

3. The paper provides extensive experimental results demonstrating the effectiveness of TRUST-SCORE in evaluating LLMs' trustworthiness and the improvements achieved through TRUST-ALIGN.

## Weaknesses
1. The paper could benefit from a more detailed comparison with existing metrics and approaches to highlight the novelty and effectiveness of TRUST-SCORE.

2. The paper could provide more insights into the limitations of TRUST-SCORE and potential directions for future research to further improve the metric.

## Questions
1. How does TRUST-SCORE compare to existing metrics in terms of reliability and validity? Are there specific scenarios where TRUST-SCORE outperforms other metrics?

2. What are the potential limitations of TRUST-SCORE, and how could these limitations be addressed in future research?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4