# Review

## Summary
The paper proposes a single-loop stochastic primal-dual algorithm for solving nonconvex optimization problems with linear inequality constraints. The algorithm is based on the inexact gradient descent framework for the Moreau envelope. The authors establish the optimal sample complexity guarantees for the algorithm and provide extensions to stochastic linear constraints.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The proposed algorithm avoids the subproblems, large batch sizes, or increasing penalty parameters in iterations, which is a notable advantage over existing methods.
2. The paper provides a clear and comprehensive analysis of the algorithm, including the optimal sample complexity guarantees and extensions to stochastic linear constraints.

## Weaknesses
1. The proposed algorithm is a single-loop algorithm, which is not very popular in the machine learning community. The double-loop structure can ensure the convergence of the primal variable to the boundary of the feasible region.
2. The paper does not provide any experimental results to validate the performance of the proposed algorithm. Numerical experiments are important for understanding the practical performance of optimization algorithms and verifying the theoretical results.
3. The paper does not provide any convergence plots to show the behavior of the proposed algorithm. Convergence plots are useful for visualizing the performance of the algorithm and understanding its behavior.

## Questions
1. Can the proposed algorithm be extended to handle other types of constraints, such as nonlinear constraints or composite constraints? The extension to other types of constraints is an interesting question that can further enhance the applicability of the proposed algorithm.
2. How does the proposed algorithm perform in practical applications? The paper does not provide any experimental results, and it would be interesting to see how the algorithm behaves in real-world datasets or problems.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4