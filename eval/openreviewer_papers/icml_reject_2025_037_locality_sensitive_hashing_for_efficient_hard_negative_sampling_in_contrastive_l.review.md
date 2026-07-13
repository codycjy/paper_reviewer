# Review

## Summary
The authors present a GPU-friendly LSH scheme that quantizes real-valued feature vectors into binary representations for approximate nearest neighbor search. They demonstrate on several datasets from both textual and visual modalities that the approach outperforms other hard negative mining strategies in terms of computational efficiency without significant performance degradation.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
1. The idea of using LSH for efficient hard negative sampling in contrastive learning is novel and interesting.

2. The proposed method is evaluated on multiple datasets and achieves good performance.

## Weaknesses
1. The paper is poorly written and hard to follow. The methodology part is too short and needs more details. For example, what is the detailed process of the proposed method? How to use LSH to generate binary vectors from DNN features? How to use the binary vectors to search approximate nearest neighbors? How to use the selected hard negative samples in contrastive learning?

2. The motivation of the paper is not clear. Why we need LSH for hard negative sampling in contrastive learning? What are the advantages of LSH over other methods for hard negative sampling? The paper lacks a thorough discussion and analysis of the motivation.

3. The experimental evaluation is not sufficient. The paper does not compare the proposed method with other methods for hard negative sampling in contrastive learning. It is hard to know how the proposed LSH-based method performs against other state-of-the-art methods.

## Questions
Please see the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4