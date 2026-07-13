# Review

## Summary
This paper proposes a sharpness-based framework for detecting and mitigating memorization in diffusion models. The authors observe that memorized samples exhibit sharp conditional density at the initial stage of generation. They propose a new metric that measures the sharpness of the probability landscape and can detect memorization early in the diffusion process. The authors also introduce a mitigation strategy called Sharpness-Aware Initialization for Latent Diffusion (SAIL), which optimizes the initial noise of the generation process to reduce memorization without altering model parameters or prompts. The paper validates the proposed framework on synthetic 2D data, MNIST, and Stable Diffusion.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper proposes a novel geometric framework for understanding memorization in diffusion models through the sharpness of probability landscapes.
- The authors provide theoretical justification for the memorization detection metric introduced by Wen et al. (2024) and propose an enhanced sharpness measure that enables early-stage memorization detection.
- The mitigation strategy does not require any modifications to the model parameters or prompts, making it a practical and non-intrusive solution.

## Weaknesses
- The proposed method incurs additional computational overhead during inference, which may limit its applicability in real-time or resource-constrained scenarios.
- The mitigation strategy requires access to the original training images to evaluate SSCD scores, which may not always be feasible in practical scenarios.

## Questions
- How does the computational overhead of the proposed method compare to existing memorization detection and mitigation techniques? Can you provide a detailed analysis of the time complexity and memory requirements?
- How does the proposed method perform on other types of generative models, such as GANs or VAEs? Has it been tested on any other datasets or modalities?
- How sensitive is the proposed mitigation strategy to the choice of hyperparameters, such as the balancing term $\alpha$ and the threshold $\ell_{thres}$? Can you provide guidelines for selecting these hyperparameters?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4