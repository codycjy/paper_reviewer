# Review

## Summary
This paper presents DictPFL, a framework designed to achieve efficient and private federated learning (FL) by encrypting only shared gradients while keeping most gradients local. This approach aims to address the privacy risks associated with gradient sharing while minimizing communication and computational overhead. The framework includes two modules: Decompose-for-Partial-Encrypt (DePE) and Prune-for-Minimum-Encrypt (PrME). DePE decomposes model weights into a dictionary and a lookup table, encrypting only the lookup table for aggregation. PrME further reduces the encrypted parameters through encryption-aware pruning. Experimental results demonstrate that DictPFL significantly reduces communication overhead and speeds up training compared to fully encrypted and selectively encrypted methods.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is well-motivated and addresses an important problem in the field of federated learning.
- The authors provide a thorough evaluation of their approach, comparing it with several baselines and conducting a comprehensive ablation study.

## Weaknesses
- The paper does not provide a detailed analysis of the memory requirements for storing encrypted gradients, which can be a significant limitation in resource-constrained environments.
- The evaluation of the proposed method focuses on image classification tasks. It would be beneficial to include evaluations on a wider range of tasks, such as text classification and text generation, to demonstrate the generalizability of the approach.
- The paper does not provide a comparison of the proposed method with other state-of-the-art privacy-preserving techniques for federated learning, such as differential privacy and secure multiparty computation.

## Questions
- How does the proposed method perform on different types of tasks, such as text classification and text generation?
- What are the memory requirements for storing encrypted gradients, and how does this impact the scalability of the approach?
- How does the proposed method compare with other state-of-the-art privacy-preserving techniques for federated learning, such as differential privacy and secure multiparty computation?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4