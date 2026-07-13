# Review

## Summary
This paper proposes HOTA, a Hamiltonian Optimal Transport Advection method that leverages the Hamilton-Jacobi-Bellman framework to solve the Generalized Schrödinger Bridge problem. The authors demonstrate that HOTA outperforms existing methods on standard benchmarks and scales effectively to high-dimensional settings. The key contributions include a density-free objective, robustness to complex geometries, and state-of-the-art empirical results in terms of feasibility and optimality.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel HJB-based framework that explicitly solves the GSB task, addressing the learning stability issues of previous approaches and having theoretical guarantees.
2. The authors provide a thorough theoretical analysis, including a proof of the dual formulation of the GSB problem, which strengthens the method's foundation.
3. The empirical evaluation is comprehensive, covering both low-dimensional and high-dimensional settings, with comparisons to existing state-of-the-art methods.

## Weaknesses
1. The method's performance is sensitive to certain network design choices, such as the Fourier feature encoding of time, which may require careful tuning.
2. The paper acknowledges that HOTA exhibits high computational complexity, particularly for high-dimensional settings, which may limit its scalability.

## Questions
1. Can you provide more insights into the choice of hyperparameters, such as the temporal discretization $T$ and the batch size $n$? How sensitive is the method to these choices?
2. How does the choice of the potential function $U(x_t)$ impact the performance of HOTA? Can you provide more examples of state cost functions that would benefit from using HOTA?
3. Can you provide more details on the computational complexity of HOTA, especially in high-dimensional settings? What are the main factors that contribute to the high complexity, and how can it be mitigated?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4