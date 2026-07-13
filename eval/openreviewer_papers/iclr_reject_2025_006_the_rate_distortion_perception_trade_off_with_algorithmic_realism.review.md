# Review

## Summary
The paper addresses the rate-distortion-perception tradeoff in lossy compression, particularly focusing on the apparent discrepancy between theoretical predictions that common randomness between the encoder and decoder is beneficial and practical observations that such randomness is not utilized in state-of-the-art compression schemes. The authors propose a novel formulation of the realism constraint that requires satisfying a universal critic that inspects individual or batches of compressed images. They characterize the optimal rate-distortion-perception tradeoff under this realism constraint and demonstrate that it is asymptotically achievable without any common randomness, unless the batch size is impractically large. The paper provides theoretical proofs and discusses the implications of these findings for lossy compression.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a novel perspective on the rate-distortion-perception tradeoff by introducing a universal critic that inspects individual or batches of compressed images, offering a fresh approach to understanding realism constraints in lossy compression.
2. The paper provides rigorous theoretical proofs to support its claims, including the achievability of the rate-distortion-perception function without common randomness in certain regimes.
3. The paper discusses the implications of its findings for lossy compression, highlighting the existence of optimal schemes that do not involve common randomness and suggesting directions for future research, including investigating realism metrics and characterizing the amount of randomness needed in relation to batch size.

## Weaknesses
1. While the paper provides a solid theoretical foundation, it may lack experimental validation to support its claims. It would be beneficial to include experiments or simulations that demonstrate the proposed rate-distortion-perception tradeoff and the achievable compression performance without common randomness.
2. The paper could benefit from a more detailed comparison with existing state-of-the-art compression schemes that do not use common randomness. A comparative analysis of these schemes with the proposed approach could provide insights into the advantages and limitations of the proposed method.

## Questions
1. Can you provide any experimental results or simulations to support your theoretical claims? This would help in better understanding the practical implications of your proposed rate-distortion-perception tradeoff.
2. How does your proposed approach compare with existing state-of-the-art compression schemes that do not use common randomness? A detailed comparative analysis would be beneficial in highlighting the advantages and limitations of your method.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4