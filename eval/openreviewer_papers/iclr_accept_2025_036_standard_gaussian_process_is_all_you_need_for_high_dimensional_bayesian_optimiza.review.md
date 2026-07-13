# Review

## Summary
The authors challenge the conventional wisdom that Bayesian optimization (BO) with standard Gaussian processes (GPs) is ineffective for high-dimensional optimization problems. They argue that this belief lacks robust empirical evidence and theoretical justification. The paper makes three main contributions:

1. **Empirical Findings**: The authors conduct a comprehensive evaluation across twelve benchmarks, including both synthetic and real-world high-dimensional optimization tasks. They compare standard BO with nine state-of-the-art high-dimensional BO methods. Interestingly, while the popular SE kernel often performs poorly, switching to the ARD Matérn kernel enables standard BO to achieve top-tier optimization performance.

2. **Theoretical Analysis**: The authors identify the primary failure mode of standard BO, particularly when using the SE kernel. They attribute this to the common practice of setting length-scale parameters to one, which can cause gradient vanishing in high-dimensional settings, preventing effective training. They provide a probabilistic tail bound to characterize this issue and show that the Matérn kernel is less prone to gradient vanishing with the same length-scale initialization, making it more effective for high-dimensional problems.

3. **Simple Robust Initialization**: Based on their theoretical findings, the authors propose a simple yet robust length-scale initialization method that does not require additional priors or regularization. They demonstrate a probabilistic bound showing that the probability of gradient vanishing decreases exponentially with increasing dimensionality. Empirical evaluations confirm that this initialization method dramatically improves the performance of standard BO with SE kernels, enabling it to achieve state-of-the-art performance in high-dimensional optimization.

## Soundness
4

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The authors challenge the conventional wisdom that Bayesian optimization (BO) with standard Gaussian processes (GPs) is ineffective for high-dimensional optimization problems. They provide a comprehensive evaluation across twelve benchmarks and compare standard BO with nine state-of-the-art high-dimensional BO methods.
- The authors identify the primary failure mode of standard BO, particularly when using the SE kernel, and provide a theoretical analysis.
- The authors propose a simple yet robust length-scale initialization method that does not require additional priors or regularization.
- The authors provide a probabilistic bound showing that the probability of gradient vanishing decreases exponentially with increasing dimensionality.
- Empirical evaluations confirm that the proposed initialization method dramatically improves the performance of standard BO with SE kernels, enabling it to achieve state-of-the-art performance in high-dimensional optimization.

## Weaknesses
- The authors should compare their proposed method with the recent work "Vanilla Bayesian Optimization Performs Great in High Dimension" [1].
- The authors should discuss the limitations of their proposed method.
- The authors should provide a more detailed discussion of the results and the implications for future research.
- The authors should provide a more detailed analysis of the computational complexity of their proposed method and compare it with other state-of-the-art methods.

Reference:
[1] Vanilla Bayesian Optimization Performs Great in High Dimension, https://arxiv.org/abs/2402.02229

## Questions
- How does the proposed method compare to the recent work "Vanilla Bayesian Optimization Performs Great in High Dimension" [1]?
- What are the limitations of the proposed method?
- Can the authors provide a more detailed discussion of the results and the implications for future research?
- Can the authors provide a more detailed analysis of the computational complexity of their proposed method and compare it with other state-of-the-art methods?

Reference:
[1] Vanilla Bayesian Optimization Performs Great in High Dimension, https://arxiv.org/abs/2402.02229

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4