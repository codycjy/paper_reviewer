# Review

## Summary
This paper introduces a novel approach to vector quantization (VQ) approximation for end-to-end rate-distortion (RD) optimization in neural compression. The authors propose an alternating optimization strategy that addresses the train-test mismatch and suboptimal encoder gradient issues, which are common in existing methods. By alternating between optimizing the encoder with differentiable approximation and the decoder with actual quantization, they ensure consistency between training and testing. Additionally, they employ a sphere-noise based stochastic approximation to improve encoder optimization, particularly at quantization boundaries.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The authors provide a clear mathematical analysis of how approximation methods affect RD optimization, offering a solid theoretical foundation for their proposed solutions.
2. The experimental results on both synthetic sources and real-world images demonstrate that the proposed method outperforms existing VQ approximation techniques, especially in scenarios with higher-dimensional vector quantization.
3. The paper is well-organized, with a logical flow from problem identification to proposed solutions and experimental validation.

## Weaknesses
1. The authors do not provide a detailed comparison with the latest state-of-the-art methods in neural image compression that also employ vector quantization, such as "Soft-to-Hard Vector Quantization for End-to-End Learning Compressible Representations" and "Unified Multivariate Gaussian Mixture for Efficient Neural Image Compression."
2. The experimental setup lacks a clear description of the hyperparameter settings, such as learning rate, batch size, and the number of training epochs, which makes it difficult to reproduce the results.
3. The paper does not include a complexity analysis of the proposed method compared to existing approaches, which is crucial for assessing its practicality.

## Questions
1. The authors mention that their method is only applicable to single-layer quantization and unconditional entropy models. Can this limitation be overcome, and if so, how would it affect the performance?
2. The proposed method uses a sphere-noise based stochastic approximation. How sensitive is the performance to the radius of the hypersphere in different applications?
3. The authors propose an encoder-decoder alternating optimization strategy. How does the performance compare to a joint optimization approach, and what are the trade-offs?
4. Can the authors provide a more detailed complexity analysis of their method compared to existing methods, including computational overhead and memory requirements?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4