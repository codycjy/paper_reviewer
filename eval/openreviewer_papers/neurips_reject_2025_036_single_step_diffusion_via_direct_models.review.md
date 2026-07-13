# Review

## Summary
The paper introduces Direct Models, a novel generative modeling framework that enables single-step diffusion by learning a direct mapping from initial noise to all intermediate latent states along the generative trajectory. This approach bypasses the need for iterative sampling procedures common in diffusion and flow matching models, which are computationally expensive and limit real-time deployment. Direct Models employ a residual-based formulation to model the full flow map through a time-indexed residual field, allowing direct access to any intermediate latent without numerical integration.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experimental results are strong.

## Weaknesses
1. The method requires training two separate networks, which limits efficiency.
2. The current formulation is restricted to single-step inference.
3. The training cost is not reported in the paper.

## Questions
1. How to extend the proposed method to multi-step inference?
2. How is the performance of the proposed method on high-resolution images, such as 512x512?
3. How is the performance of the proposed method on other architectures, such as UNet?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4