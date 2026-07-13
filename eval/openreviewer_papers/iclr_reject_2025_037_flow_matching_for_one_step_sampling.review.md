# Review

## Summary
This paper proposes a new approach to sampling from a target distribution $\rho_1$ given samples from it, without solving the ODE that would be required by a standard flow matching model. Instead, the authors propose to learn a model that maps the samples from a simple base distribution $\rho_0$ to the target distribution $\rho_1$. To do so, they first use the explicit formula for the velocity field in [1] to compute the prototypes $X_0(x_1)$ of each point $x_1$ in the target distribution $\rho_1$, i.e. the starting point in $\rho_0$ of the flow that ends at $x_1$. The authors then learn a model that maps each $X_0(x_1)$ to $x_1$, so that they can sample directly from $\rho_1$ by sampling from $\rho_0$ and passing the result through the learned model.

[1] Explicit Flow Matching: On the Theory of Flow Matching Algorithms with Applications, Ryzhakov et al.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper is well motivated: sampling from a target distribution without solving an ODE is desirable because it is faster and thus allows for more efficient sampling.
- The idea of learning a model that maps prototypes to their images in the target distribution is interesting.

## Weaknesses
- The method is not clearly described. In particular, the authors do not describe how they learn the model that maps prototypes to their images in the target distribution. This model is crucial to the proposed method, and its description should not be relegated to a footnote (L119). Furthermore, the authors should provide a clear mathematical description of their method.
- The experiments are limited to toy settings and a simple image-to-image translation problem. The authors should evaluate their method on more complex tasks, such as unconditional image generation.
- The authors should compare their method to other methods that aim to learn a one-step sampler, such as [1] and [2].
- The authors should provide a more thorough discussion of the limitations of their method.

[1] Optimal Flow Matching: Learning Straight Trajectories in Just One Step, Kornilov et al.

[2] InstaFlow: One Step is Enough for High-Quality Diffusion-Based Text-to-Image Generation, Liu et al.

## Questions
- How is the model that maps prototypes to their images in the target distribution trained? Could the authors provide a clear description of this process and a mathematical formulation?
- Can the authors provide a more detailed comparison to other one-step sampling methods, such as [1] and [2]?
- Can the authors evaluate their method on more complex tasks, such as unconditional image generation?
- What is the computational cost of training the model that maps prototypes to their images in the target distribution? How does this compare to the computational cost of training a standard flow matching model?
- What are the limitations of the proposed method? The authors should provide a more thorough discussion of the potential drawbacks of their approach.

[1] Optimal Flow Matching: Learning Straight Trajectories in Just One Step, Kornilov et al.

[2] InstaFlow: One Step is Enough for High-Quality Diffusion-Based Text-to-Image Generation, Liu et al.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4