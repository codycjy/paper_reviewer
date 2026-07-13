# Review

## Summary
This paper presents a theory for how convolutional diffusion models can generate creative outputs that deviate from their training data, despite optimal score-matching theory suggesting memorization. The authors identify two key inductive biases—locality and equivariance—that prevent perfect score-matching and allow for combinatorial creativity. They propose Local Score (LS) and Equivariant Local Score (ELS) machines, which provide analytic, interpretable mechanisms for generating novel images by mixing local training set patches. The theory is validated by accurately predicting outputs from trained convolutional models like ResNets and UNets on datasets such as MNIST, FashionMNIST, and CIFAR10. The paper also explores the role of attention mechanisms in refining these local patch mosaics into semantically coherent outputs.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper offers a novel theoretical perspective on the creativity of convolutional diffusion models, focusing on inductive biases rather than network complexity.
2. The authors provide a rigorous mathematical framework with proofs and clear explanations for their proposed (E)LS machines.
3. The theory is extensively validated through experiments on multiple datasets and architectures, demonstrating strong quantitative agreement with trained model outputs.
4. The mechanistic interpretation of the (E)LS machines offers insights into how different parts of an image are generated through local interactions.
5. The work is well-structured and clearly presented, with figures and examples that illustrate the patch mosaic mechanism of creativity.

## Weaknesses
1. The paper is dense and may be challenging for readers unfamiliar with diffusion models or score-matching theory.
2. The theory is limited to convolutional models and does not fully explain the role of attention mechanisms in more modern architectures.
3. The experiments focus on simple datasets; applying the theory to more complex, high-dimensional datasets would strengthen the claims.
4. The paper could benefit from a discussion on the limitations of the proposed theory and potential directions for future research.

## Questions
1. How does the proposed theory extend to diffusion models with attention mechanisms? What role do you envision for attention in the creative process?
2. Can the (E)LS machine framework be adapted for other types of generative models, such as GANs or flow-based models?
3. How sensitive are the predictions of the (E)LS machines to the choice of locality scale? Is there a way to automatically determine this scale?
4. The paper mentions spatial inconsistencies in fine details. How might the theory account for these inconsistencies, and are there potential solutions to improve output quality?
5. What are the implications of the theory for real-world applications of diffusion models, such as image editing or style transfer?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4