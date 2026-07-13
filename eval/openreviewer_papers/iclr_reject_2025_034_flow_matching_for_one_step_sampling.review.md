# Review

## Summary
The paper proposes a method for mapping between two distributions, from which samples are available for the target distribution but not the source distribution. The method is based on estimating the velocity field of a flow matching model using samples from the target distribution, and training a model to predict the target samples from noise using this velocity field. The method avoids solving the ODE for mapping between the distributions, which can be computationally expensive. The method is evaluated on a range of tasks, including image generation, image-to-image translation, and color transfer.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper addresses an important problem of mapping between two distributions when only samples from one distribution are available. The proposed method of estimating the velocity field and training a model to predict samples from noise is an interesting approach.
- The method is evaluated on a range of tasks, including image generation, image-to-image translation, and color transfer, demonstrating its versatility.
- The paper is generally well-written and clear, with a good explanation of the proposed method and its motivation.

## Weaknesses
- The paper lacks a thorough comparison with existing methods for mapping between two distributions when only samples from one distribution are available. The proposed method is not compared with any other methods in the experiments, making it difficult to assess its relative performance.
- The paper lacks a thorough discussion of the limitations of the proposed method. For example, the method requires estimating the velocity field using samples from the target distribution, which may not always be accurate or efficient, particularly for high-dimensional distributions. The paper would benefit from a more detailed analysis of the method's sensitivity to the quality and quantity of samples from the target distribution.
- The paper lacks a thorough analysis of the computational complexity of the proposed method. While the method avoids solving the ODE for mapping between the distributions, it still requires estimating the velocity field using samples from the target distribution, which can be computationally expensive for high-dimensional distributions. The paper would benefit from a more detailed analysis of the computational complexity of the proposed method, including the time and memory requirements for estimating the velocity field and training the model.

## Questions
- How does the proposed method compare with other methods for mapping between two distributions when only samples from one distribution are available, such as GANs, VAEs, or other flow matching models?
- What are the limitations of the proposed method, particularly in terms of the quality and quantity of samples from the target distribution required for accurate estimation of the velocity field?
- What is the computational complexity of the proposed method, particularly for high-dimensional distributions, and how does it compare with other methods for mapping between two distributions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4