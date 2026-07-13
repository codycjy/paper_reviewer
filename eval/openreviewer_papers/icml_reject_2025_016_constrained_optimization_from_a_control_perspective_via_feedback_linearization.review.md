# Review

## Summary
The paper studies the application of feedback linearization (FL) to solve constrained optimization problems. It establishes a global convergence rate to a KKT point for equality-constrained optimization, drawing a close connection between FL and Sequential Quadratic Programming (SQP). This relationship is then extended to handle inequality-constrained problems. Finally, the paper introduces a momentum-accelerated FL algorithm, which is shown to converge faster both empirically and theoretically.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow. The problem is well-motivated and the theoretical results are sound.

- The analysis of the FL method in Section 3 is novel and provides a convergence rate to a KKT point. The connection between FL and SQP in Section 3.2 is also interesting.

## Weaknesses
- The extension of FL to inequality-constrained problems in Section 4 is not fully satisfactory. The proposed method in (11) is derived by reverse-engineering the SQP algorithm, and the resulting trajectory is not smooth. This is in contrast to the smooth trajectory obtained by the FL method in Section 3.1 for equality-constrained problems.

- The momentum acceleration of FL in Section 5 is also somewhat unsatisfactory. The continuous-time model in (18) is not the standard Nesterov momentum model in (15), and it is unclear how this model leads to acceleration. The authors acknowledge this limitation in Theorem 5, and the acceleration is only shown for the special case of affine constraints. 

- The theoretical results in Sections 4 and 5 are quite similar to those in Section 3.1, and the paper would benefit from a clearer comparison of the theoretical guarantees for different types of constraints.

## Questions
- The paper focuses on the application of FL to constrained optimization. However, the proposed method in (11) for inequality-constrained problems is not smooth, and the momentum model in (18) is not the standard Nesterov momentum model. I am wondering if the authors could comment on these limitations and explain the motivation for studying these particular formulations.

- The authors mention that the acceleration of SQP methods is usually achieved via Newton or quasi-Newton methods. However, there are some recent works on accelerating SQP methods via other approaches, such as trust-region methods (https://arxiv.org/abs/2404.10774) and adaptive step sizes (https://arxiv.org/abs/2404.10989). It would be helpful to discuss these works in the paper and explain how the proposed momentum model compares to these approaches.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4