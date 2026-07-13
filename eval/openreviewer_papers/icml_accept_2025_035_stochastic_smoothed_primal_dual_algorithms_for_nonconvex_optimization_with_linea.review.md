# Review

## Summary
This paper proposes a single-loop, inexact primal-dual algorithm for solving stochastic nonconvex optimization problems with linear inequality constraints. The algorithm is based on the Moreau envelope and requires only a single sample of the stochastic gradient at each iteration. The authors establish optimal sample complexity guarantees for their algorithm and provide extensions to stochastic linear constraints. Unlike existing methods, their algorithm avoids subproblems, large batch sizes, and increasing penalty parameters in iterations, and utilizes dual variable updates for feasibility.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The authors propose a single-loop, inexact primal-dual algorithm for solving stochastic nonconvex optimization problems with linear inequality constraints. The algorithm is based on the Moreau envelope and requires only a single sample of the stochastic gradient at each iteration.

2. The authors establish optimal sample complexity guarantees for their algorithm and provide extensions to stochastic linear constraints. 

3. Unlike existing methods, their algorithm avoids subproblems, large batch sizes, and increasing penalty parameters in iterations, and utilizes dual variable updates for feasibility.

## Weaknesses
1. The algorithm design and theoretical analysis are heavily based on the work of [1]. The authors should highlight their technical contributions and innovations more clearly.

2. The authors should provide numerical results to demonstrate the practical performance and efficiency of their proposed algorithm.

3. The authors should include more detailed and rigorous proofs of the theoretical results to ensure the correctness and validity of their findings.

[1] Zhang, J., & Luo, Z.-Q. (2022). A global dual error bound and its application to the analysis of linearly constrained nonconvex optimization. SIAM Journal on Optimization, 32(3), 2319-2346.

## Questions
See the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4