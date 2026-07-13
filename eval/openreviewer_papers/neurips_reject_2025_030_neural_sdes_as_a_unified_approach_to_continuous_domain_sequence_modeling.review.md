# Review

## Summary
This paper proposes a new Neural SDE framework for continuous sequence modeling, which directly models continuous-time dynamics and eliminates the costly forward simulations required in traditional gradient estimation. The authors demonstrate the effectiveness of their approach on several sequence modeling tasks, including video prediction and imitation learning, and show that their method outperforms existing baselines in terms of both accuracy and computational efficiency.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a novel approach to continuous sequence modeling using Neural SDEs, which is an innovative combination of existing ideas.
2. The authors provide a clear and detailed explanation of their method, including the derivation of the maximum likelihood objective and the simulation-free training scheme.
3. The paper includes thorough experiments on multiple sequence modeling tasks, demonstrating the versatility and effectiveness of the proposed approach.

## Weaknesses
1. The authors could provide more details on the implementation of the denoiser network and its impact on the overall performance.
2. The paper could include a more detailed comparison with other state-of-the-art methods in the field, such as diffusion models and flow matching frameworks.
3. The authors could address potential limitations of their approach, such as scalability to very long sequences or real-time applications.

## Questions
1. How does the performance of the Neural SDE framework compare to other state-of-the-art methods for continuous sequence modeling, such as diffusion models or flow matching frameworks?
2. Can the Neural SDE framework be extended to handle non-Markovian dynamics, where the current state depends on previous states in a more complex way?
3. How does the choice of the diagonal diffusion matrix affect the performance of the model? Are there cases where a full matrix diffusion is preferred?
4. Can the Neural SDE framework be used for other tasks, such as time series forecasting or recommendation systems?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4