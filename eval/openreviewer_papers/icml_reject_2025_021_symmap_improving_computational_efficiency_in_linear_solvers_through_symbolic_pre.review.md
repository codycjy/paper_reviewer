# Review

## Summary
This paper introduces a framework, Symbolic Matrix Preconditioning (SymMaP), which uses neural networks to search for symbolic expressions that determine preconditioning parameters for linear system solvers. SymMaP addresses limitations in traditional and existing machine learning approaches by providing instance-specific preconditioning while maintaining interpretability and efficiency. Experimental results show that SymMaP outperforms traditional and baseline machine learning methods across various benchmarks, demonstrating improved computational efficiency and adaptability.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow.
- The framework is easy to integrate into existing CPU-based algorithm libraries.

## Weaknesses
- The paper lacks novelty and originality, as it primarily applies existing techniques (i.e., symbolic regression using RNNs) to preconditioning parameters without introducing significant new concepts or methods.
- The paper does not address the scalability of SymMaP for large-scale problems. It is unclear how well the framework would perform with significantly larger datasets or more complex systems, which could be a limitation for practical applications.
- The paper does not provide a comparison of SymMaP with other state-of-the-art preconditioning techniques. It would be beneficial to include comparisons with more advanced preconditioning methods to better establish SymMaP's relative effectiveness.

## Questions
- How does SymMaP handle very large datasets, and what are the computational costs associated with training?
- Can SymMaP be extended to other types of matrix solvers beyond those discussed in the paper?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4