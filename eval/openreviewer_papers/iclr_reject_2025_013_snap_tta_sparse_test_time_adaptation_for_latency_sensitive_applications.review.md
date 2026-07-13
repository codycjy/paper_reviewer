# Review

## Summary
This paper introduces SNAP-TTA, a sparse test-time adaptation framework designed for resource-constrained edge devices. SNAP-TTA aims to reduce latency while maintaining model accuracy by selectively adapting to domain shifts with a subset of data. The framework combines two key components: Class and Domain Representative Memory (CnDRM), which identifies and selects class- and domain-representative samples for adaptation, and Inference-only Batch-aware Memory Normalization (IoBMN), which refines normalization layers using these representative samples to align the model with changing domains during inference.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The SNAP-TTA framework introduces a novel approach to Test-Time Adaptation (TTA) by focusing on sparsity, which is highly relevant for edge devices with limited resources. The combination of Class and Domain Representative Memory (CnDRM) and Inference-only Batch-aware Memory Normalization (IoBMN) provides an innovative solution to the challenges of latency and accuracy in TTA.

2. The paper presents extensive experimental results across multiple datasets and adaptation rates, demonstrating the effectiveness of SNAP-TTA in maintaining accuracy while reducing latency. The significant latency reductions achieved by SNAP-TTA, especially in resource-constrained environments, highlight the practical applicability of the framework.

3. The SNAP-TTA framework is designed to be orthogonal to existing TTA methods, and its compatibility with various state-of-the-art algorithms is thoroughly evaluated. This versatility enhances the potential impact of the work, as it can be integrated into different TTA approaches.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational overhead introduced by the SNAP-TTA framework. While latency reductions are reported, a more comprehensive assessment of the computational costs associated with the additional components (CnDRM and IoBMN) would strengthen the evaluation.

2. The paper could benefit from a deeper exploration of the trade-offs involved in using different adaptation rates. While the authors present results across various adaptation rates, a more detailed analysis of the impact on both latency and accuracy would provide a clearer understanding of the limitations and potential applications of SNAP-TTA.

3. The paper primarily focuses on image classification tasks. Extending the evaluation to other types of tasks, such as object detection or segmentation, would demonstrate the broader applicability of the SNAP-TTA framework and its potential impact on a wider range of applications.

## Questions
1. How does the computational overhead of the CnDRM and IoBMN components compare to the base TTA methods? Are there any significant memory or processing overheads introduced by these components?

2. Can the authors provide more insights into the trade-offs between latency reduction and accuracy? Is there a point at which further reducing latency significantly degrades accuracy, and if so, how is this balance optimal?

3. How well does SNAP-TTA generalize to other types of tasks beyond image classification? Have the authors considered evaluating the framework on tasks such as object detection or segmentation?

4. What are the specific hyperparameter settings used for the adaptation rate? How sensitive is the performance of SNAP-TTA to variations in these hyperparameters?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4