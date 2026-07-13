# Review

## Summary
This paper introduces Deliberate Practice (DP) for Synthetic Data Generation, a framework that enhances sample efficiency by dynamically generating synthetic data. Unlike traditional methods that generate and then prune datasets, DP directly generates informative samples. The authors provide theoretical analysis and empirical validation, demonstrating that DP improves scaling performance, requiring significantly fewer samples and iterations while achieving superior results on ImageNet-100 and ImageNet-1k.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The proposed Deliberate Practice (DP) framework is a novel approach that dynamically generates challenging samples based on the learner's feedback, which is a significant departure from traditional static dataset generation methods.
2. The paper provides a solid theoretical analysis of the scaling behavior of a model trained on selectively generated samples, using random matrix theory to characterize test error and demonstrate the benefits of prioritizing hard examples.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational cost associated with the dynamic generation process, which could be a concern for large-scale applications.
2. The experiments are primarily conducted on ImageNet-100 and ImageNet-1k. Additional experiments on a broader range of datasets would strengthen the generalizability of the findings.
3. The paper does not thoroughly discuss the potential for overfitting to the synthetic data, especially when using entropy-guided sampling to generate challenging samples.
4. The method's reliance on the learner's current state for generating informative samples could lead to a bias towards certain types of samples, potentially limiting the diversity of the training data.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4