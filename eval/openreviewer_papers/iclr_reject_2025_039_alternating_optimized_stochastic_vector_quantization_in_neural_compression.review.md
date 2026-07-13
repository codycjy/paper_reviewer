# Review

## Summary
This paper proposes an alternating optimization method for vector quantization (VQ) in neural compression. The approach involves optimizing the encoder with a differentiable approximation and the decoder with actual quantization, aiming to address train-test mismatch and suboptimal encoder gradients for rate-distortion (RD) optimization. Additionally, the authors introduce a sphere-noise based stochastic approximation to improve encoder optimization at boundaries. Experiments on synthetic sources and natural images demonstrate that this method achieves better RD performance compared to traditional approximation techniques.

## Soundness
3

## Presentation
2

## Contribution
2

## Strengths
1. The paper provides a detailed mathematical analysis of the challenges in VQ, particularly focusing on the train-test mismatch and suboptimal encoder gradients, which are key issues in neural compression.

2. The proposed alternating optimization strategy is novel, offering a new approach to address the optimization challenges specific to VQ in neural compression.

3. The authors conduct experiments across various synthetic sources and natural images, demonstrating consistent performance improvements over existing methods.

## Weaknesses
1. The proposed method is limited to single-layer quantization and unconditional entropy models, which restricts its applicability to more complex models commonly used in state-of-the-art neural compression techniques.

2. The authors do not compare their method with more recent and advanced neural compression techniques that have demonstrated superior RD performance. As a result, the reported BD-rate gains may not be as significant when compared to the latest methods.

3. The authors claim that the proposed method ensures optimal RD performance when determining quantization boundaries. However, Figure 6 shows that the encoder gradients are not as smooth as those of UQ-AUN, which raises questions about the optimality of the method.

4. The authors state that the proposed method ensures train-test mismatch. However, it is unclear how this is achieved, as the method still uses a differentiable approximation during training. Further clarification is needed on how the train-test mismatch is addressed.

5. The authors do not provide an analysis of the computational complexity or runtime of their proposed method compared to existing techniques. This information would be valuable for assessing the practicality of the approach.

## Questions
Please refer to the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4