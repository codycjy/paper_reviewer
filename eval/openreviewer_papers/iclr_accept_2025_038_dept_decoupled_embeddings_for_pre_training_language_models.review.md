# Review

## Summary
This paper introduces DEPT, a communication-efficient pre-training framework that addresses the challenges of training language models on heterogeneous data sources. DEPT achieves this by decoupling embeddings from the transformer body, allowing for customized vocabularies and optimized training across different domains and languages. The framework significantly reduces memory and communication costs while improving model generalization and plasticity.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- DEPT offers a novel approach to handle data heterogeneity by decoupling embeddings, which is a significant advancement over traditional methods that require a shared vocabulary.
- The framework addresses a critical issue in language model pre-training, making it highly relevant for large-scale applications.
- DEPT demonstrates substantial reductions in memory and communication costs, which are crucial for distributed training environments.
- The paper provides extensive experimental results that validate the effectiveness of DEPT in improving generalization and plasticity across various datasets.

## Weaknesses
- The paper could benefit from more detailed ablation studies to further explore the impact of different components of DEPT.
- DEPT introduces additional complexity with its variants, which may make it challenging for practitioners to choose the most appropriate setting.

## Questions
- How does DEPT compare to other methods in terms of computational overhead, especially for very large-scale models?
- What are the trade-offs between the different DEPT variants, and how should practitioners choose the appropriate one for their specific use case?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4