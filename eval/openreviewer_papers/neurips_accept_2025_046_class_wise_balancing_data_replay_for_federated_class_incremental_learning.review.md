# Review

## Summary
The paper proposes a class-wise balancing data replay method, FedCBDR, for Federated Class-Incremental Learning (FCIL). It addresses the challenge of class imbalance in replay buffers by using a global coordination mechanism for class-level memory construction and reweighting the learning objective. FedCBDR has two main components: a global-perspective data replay module that ensures privacy-preserving global representation and a task-aware temperature scaling module to handle class imbalance across tasks. Experimental results show that FedCBDR achieves significant improvements in accuracy over state-of-the-art methods.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper introduces a novel approach to addressing class imbalance in Federated Class-Incremental Learning (FCIL) through a class-wise balancing data replay method.
2. The paper is well-structured, with a clear abstract, introduction, methodology, experiments, and conclusions. The methodology is explained in detail, and the experiments are thoroughly described, including the datasets, evaluation metrics, and implementation details.
3. The paper compares FedCBDR with six state-of-the-art methods, demonstrating its superiority in achieving higher Top-1 accuracy under various levels of data heterogeneity and task splits. The results are presented with mean and standard deviation, providing a measure of reliability.

## Weaknesses
1. The paper lacks a thorough discussion of the limitations of the proposed method and potential areas for future research.
2. The paper does not provide a detailed analysis of the computational complexity or scalability of the proposed method, which could be a concern for large-scale applications.
3. The paper does not discuss the impact of different hyperparameters on the performance of the proposed method, which could be important for practical implementations.
4. The paper does not provide a detailed comparison of the proposed method with other state-of-the-art methods in terms of computational efficiency and memory usage.

## Questions
1. How does the proposed method handle concept drift in FCIL? Is there any mechanism to adapt to changing data distributions over time?
2. How sensitive is the performance of the proposed method to the choice of hyperparameters, such as the temperature scaling factors and sample weights?
3. What are the potential applications of the proposed method beyond the datasets and tasks considered in the experiments?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4