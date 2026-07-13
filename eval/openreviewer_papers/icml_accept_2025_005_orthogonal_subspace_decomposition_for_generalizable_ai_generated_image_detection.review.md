# Review

## Summary
This paper addresses the limitations of existing AI-generated image detection (AIGI) methods, particularly focusing on the generalization problem. The authors identify an asymmetry phenomenon where naive detectors overfit to limited fake patterns, leading to constrained feature spaces that hinder generalization. To address this, they propose a novel approach using Singular Value Decomposition (SVD) to construct two orthogonal subspaces: one for preserving pre-trained knowledge and another for learning fake patterns. This method effectively minimizes overfitting and enhances generalization, supported by extensive experiments on deepfake and synthetic image benchmarks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper introduces a novel method using SVD for orthogonal subspace decomposition, which is a unique approach to handling the generalization problem in AIGI detection.
2. The paper provides a comprehensive set of experiments on multiple benchmarks, demonstrating the effectiveness of their method.
3. The method shows significant improvements in generalization, achieving higher performance with much fewer trainable parameters compared to existing methods.

## Weaknesses
1. The paper does not provide a clear explanation of why the proposed method effectively generalizes better. While the empirical results are strong, a deeper theoretical analysis would strengthen the paper.
2. The approach may be seen as an incremental improvement over existing methods, particularly those using pre-trained vision models.
3. The paper does not address the computational complexity of the proposed method, which could be a concern for large-scale applications.

## Questions
1. Can the authors provide more theoretical justification for why the orthogonal subspace decomposition helps with generalization?
2. How does the computational complexity of the proposed method compare to existing approaches?
3. Have the authors considered applying this method to other related tasks, such as face anti-spoofing or anomaly detection? How well do you think it would generalize to these tasks?
4. The paper mentions the use of pre-trained knowledge from vision foundation models. How sensitive is the performance of the proposed method to the choice of these pre-trained models? Have you tested with different pre-trained models and observed significant performance variations?
5. The method uses a fixed rank for the SVD decomposition. How was this rank chosen, and how sensitive is the performance to this choice? Did you experiment with different ranks and observe significant changes in performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4