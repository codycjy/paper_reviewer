# Review

## Summary
This paper introduces MAETok, a new autoencoder-based (AE-based) tokenizer designed to enhance the performance of diffusion models. The authors first demonstrate that a more structured latent space, with fewer Gaussian Mixture Model (GMM) modes, leads to better diffusion model training. Building on this insight, they propose MAETok, which employs mask modeling to learn a semantically rich latent space while preserving reconstruction fidelity. Experimental results show that MAETok achieves state-of-the-art performance on ImageNet generation using only 128 tokens.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
1. This paper is well-written, with a clear logical flow that makes it easy to follow. The authors first establish an understanding of the latent space through theoretical and empirical analysis, then propose the method based on this understanding. The experiments are comprehensive, with detailed explanations of the setup, making the results highly convincing.
2. The authors provide a theoretical foundation for why a more structured latent space benefits diffusion models, which is further validated through extensive experiments.
3. The proposed tokenizer achieves state-of-the-art performance with fewer tokens, addressing the critical challenge of reducing computational overhead in diffusion models.

## Weaknesses
1. The tokenizer was trained on ImageNet, while the diffusion model was trained on a combination of ImageNet and LAION-COCO. It would be beneficial to evaluate whether using the tokenizer trained on ImageNet alone is sufficient for the diffusion model, or if performance improves when the tokenizer is also trained on LAION-COCO.
2. The tokenizer introduces additional hyperparameters, such as the mask ratio and the number of auxiliary decoders, which may require careful tuning to achieve optimal performance.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4