# Review

## Summary
The paper introduces a new speculative decoding method that enables the use of different vocabularies for the target and drafter models. The authors propose three different algorithms: 1) an exact match algorithm that operates at the string level, 2) a rejection sampling algorithm that also operates at the string level, and 3) a token-level rejection sampling algorithm. The authors evaluate their proposed algorithms on various target models and datasets, demonstrating speedups over autoregressive decoding.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper addresses a significant limitation of current speculative decoding methods by enabling the use of different vocabularies for the target and drafter models. This broadens the applicability of speculative decoding to more use cases.
2. The proposed algorithms are lossless, meaning they preserve the target distribution. The authors provide theoretical proofs and empirical evaluations to support this.
3. The paper includes extensive empirical results on various target models and datasets, demonstrating significant speedups over autoregressive decoding.

## Weaknesses
1. The paper does not provide a comparison to existing methods for heterogeneous vocabularies. It would be helpful to understand how the proposed methods perform compared to other existing approaches in this setting.
2. The paper could benefit from more discussion on the practical implications of using different vocabularies for the target and drafter models. Are there any potential issues or challenges that arise from this?

## Questions
1. How does the proposed method compare to existing methods for heterogeneous vocabularies?
2. What are the potential issues or challenges that arise from using different vocabularies for the target and drafter models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4