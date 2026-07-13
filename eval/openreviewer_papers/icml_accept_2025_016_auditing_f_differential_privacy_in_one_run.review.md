# Review

## Summary
The paper presents a novel auditing procedure for assessing the privacy guarantees of differentially private (DP) algorithms. The authors propose an approach that leverages the randomness of examples in the input dataset, allowing the audit to be performed in a single run of the target mechanism. The paper introduces the concept of f-Differential Privacy (f-DP), which provides a more fine-grained privacy analysis than traditional DP parameters (ε, δ). By using the f-DP curve, the authors argue that their auditing method achieves more accurate privacy estimates.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
- The paper proposes a novel auditing procedure that requires only a single run of the privacy mechanism, addressing the computational inefficiency of previous methods.

- The use of f-DP curves for auditing purposes is an interesting approach that could potentially offer more granularity in privacy analysis.

- The experiments conducted on both simple Gaussian mechanisms and models trained with DP-SGD demonstrate the practical applicability of the proposed method.

## Weaknesses
- The paper does not provide a theoretical analysis of the false positive rate or the power of their auditing method. Without such analysis, it's hard to know how the method would perform in practice.

- The paper lacks a clear comparison with existing auditing methods. While the authors mention limitations of previous approaches, they do not provide empirical comparisons or benchmarks to demonstrate how their method improves upon these existing techniques.

- The experiments are conducted in an idealized setting. It would be beneficial to see how the method performs in more realistic scenarios.

- The paper does not provide any code or implementation details, which makes it difficult for others to reproduce the experiments or apply the method to their own datasets.

## Questions
- How does the proposed auditing method perform in terms of false positive rate and power? Can you provide theoretical guarantees or empirical results to demonstrate its effectiveness?

- How does your method compare with existing auditing techniques in terms of computational efficiency and accuracy? Can you provide empirical benchmarks to illustrate the advantages of your approach?

- Can you provide more details on the experimental setup, including data characteristics and the choice of privacy parameters (ε, δ)? How does the method perform with different types of data and varying privacy requirements?

- What are the limitations of your method, and in what scenarios might it not be applicable? How does the method handle different auditing requirements or varying levels of privacy protection?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4