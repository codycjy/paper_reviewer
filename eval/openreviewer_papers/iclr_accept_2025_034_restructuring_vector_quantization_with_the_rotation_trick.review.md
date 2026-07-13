# Review

## Summary
The paper proposes an alternative method to propagate gradients through the vector quantization layer of VQ-VAEs. The method transforms the encoder output smoothly into the codebook vector using a rotation and rescaling linear transformation, which is treated as a constant during backpropagation. This approach allows the relative magnitude and angle between the encoder output and codebook vector to influence the gradient, resulting in improved reconstruction metrics, codebook utilization, and quantization error across various VQ-VAE training paradigms.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper introduces a novel method for propagating gradients through vector quantization, addressing a fundamental challenge in VQ-VAEs. The rotation trick offers a fresh perspective on gradient propagation, distinguishing itself from the commonly used straight-through estimator (STE). The paper provides a detailed analysis of the rotation trick's behavior, including its effects on codebook utilization and quantization error. The authors conduct experiments across 11 different VQ-VAE configurations, demonstrating the method's effectiveness and robustness. The paper is well-written and organized, with clear explanations of the proposed method and its advantages.

## Weaknesses
The paper lacks a comparison with other existing methods for handling vector quantization in VQ-VAEs, such as stochastic quantization or the Gumbel-Softmax trick. The experiments are primarily conducted on image datasets; extending the evaluation to other data types, such as speech or video, could strengthen the paper's claims. The paper does not provide a thorough discussion of the computational complexity or runtime performance of the proposed method compared to other approaches. A more detailed analysis of the trade-offs between performance and computational cost would be beneficial.

## Questions
The paper could benefit from a more detailed discussion on the choice of hyperparameters and their impact on the performance of the rotation trick. The paper does not provide a clear explanation for why the rotation trick outperforms the STE in all evaluated scenarios. A more detailed analysis or theoretical justification for the method's superiority would strengthen the paper's claims. The paper could include more visualizations or examples to illustrate the practical effects of the rotation trick on different types of data.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4