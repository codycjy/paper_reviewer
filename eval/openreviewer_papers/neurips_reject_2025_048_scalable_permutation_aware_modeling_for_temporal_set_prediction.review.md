# Review

## Summary
This paper presents a novel and scalable framework for Temporal Set Prediction (TSP), which is the problem of predicting which elements belong to a set at a future time point given a sequence of sets. The proposed framework, named PIETSP, combines an efficient input representation with permutation-equivariant and permutation-invariant transformations to model set dynamics. The authors demonstrate that PIETSP achieves linear time complexity with respect to both sequence length and the number of distinct elements, enabling the processing of large-scale datasets efficiently. Extensive experiments on multiple public datasets show that PIETSP achieves state-of-the-art performance, outperforming or matching existing models across several evaluation metrics.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow, with a clear and concise explanation of the proposed framework. The authors provide a thorough review of relevant literature, including both existing methods for TSP and related work in next-basket recommendation and multiset modeling.
2. The proposed framework is novel and scalable, with a mathematically principled formulation that integrates element features and temporal dynamics in a joint representation. The framework achieves linear scaling with respect to both sequence length and the number of distinct elements, which is a significant improvement over existing methods that typically incur quadratic complexities.
3. The authors conduct comprehensive empirical evaluation on multiple publicly available datasets, demonstrating that PIETSP achieves comparable or superior performance to existing state-of-the-art methods while significantly reducing computational requirements. The experiments include performance comparison, model efficiency comparison, and ablation study, providing a thorough assessment of the proposed framework.

## Weaknesses
1. The motivation is not strong enough. The authors claim that existing methods face significant computational challenges with large temporal sets, but they do not provide a clear analysis of the computational complexity and scalability issues in current methods. It would be helpful to provide a detailed complexity analysis of existing methods and compare their scalability with the proposed framework.
2. The novelty is limited. The proposed framework combines existing techniques such as permutation-equivariant and permutation-invariant transformations, which have been widely used in previous works. The authors should clearly explain how their framework differs from existing methods and what specific contributions they make to the field.
3. The experiments are not convincing enough. The authors compare their framework with only three baselines, which may not represent the full range of existing methods for TSP. It would be helpful to include a more comprehensive comparison with additional baselines, such as [1]. Additionally, the authors should provide a detailed analysis of the experimental results, including error analysis and failure cases, to better understand the limitations and strengths of the proposed framework.
4. The paper lacks a detailed discussion of the model's interpretability and explainability. It would be helpful to provide insights into how the model makes predictions and how the results can be interpreted in the context of the problem domain.

[1] Li, Zhaowei, et al. "Temporal set prediction with graph convolutional networks and hierarchical attention networks." Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2022.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4