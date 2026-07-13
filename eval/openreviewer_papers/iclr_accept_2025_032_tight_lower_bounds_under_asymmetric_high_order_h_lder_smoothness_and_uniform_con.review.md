# Review

## Summary
This paper investigates the oracle complexity of minimizing high-order Hölder smooth and uniformly convex functions, particularly under two asymmetric cases: when the degree of uniform convexity $q$ is greater than $p + \nu$, and when $q < p + \nu$, where $p$ is the order of smoothness, and $\nu$ is the Hölder degree. The authors establish lower bounds for these cases, generalizing previous lower bounds for uniformly convex functions with first- and second-order smoothness. They employ the $\ell_\infty$-ball-truncated Gaussian smoothing operator to achieve dimension-free smoothness, which is crucial for optimizing high-order smooth functions. The results provide a theoretical understanding of optimization in these asymmetric settings.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a rigorous theoretical analysis with well-established lower bounds for asymmetric high-order optimization, which contributes to the understanding of optimization in complex settings.
- By using truncated Gaussian smoothing, the authors achieve a dimension-free smoothness, which is essential for handling high-order smooth functions effectively.
- The paper generalizes previous lower bounds to include Hölder smoothness, extending the scope beyond uniformly convex functions with only first- and second-order smoothness.

## Weaknesses
- The paper does not include a discussion on the $q = p + \nu$ case, leaving a gap in the analysis for this specific scenario.
- The use of the truncated Gaussian smoothing operator, while effective, may be complex to implement and analyze, potentially limiting the accessibility of the results for practitioners.

## Questions
- How does the proposed truncated Gaussian smoothing operator compare with other smoothing techniques in terms of computational efficiency and accuracy?
- Can the results be extended to include the $q = p + \nu$ case, and if so, what would be the main challenges in deriving the lower bounds?
- What are the practical implications of these theoretical lower bounds on the design and analysis of optimization algorithms for high-order convex functions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4