# Review

## Summary
The paper proposes a computationally efficient alternative to generalized random forests (GRFs) for estimating heterogeneous effects in large dimensions. While GRFs rely on a gradient-based splitting criterion, which in large dimensions is computationally expensive and unstable, the proposed method introduces a fixed-point approximation that eliminates the need for Jacobian estimation. This gradient-free approach preserves GRFs theoretical guarantees of consistency and asymptotic normality while significantly improving computational efficiency. The authors demonstrate that their method achieves a speedup of multiple times over standard GRFs without compromising statistical accuracy. Experiments on both simulated and real-world data validate the proposed approach.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
The paper is well written and the contribution is clear. The problem of estimating heterogeneous effects is important. The proposed method is a scalable alternative to GRFs, which is a significant contribution to the field. The authors provide a thorough evaluation of their method on both simulated and real-world data, demonstrating its effectiveness and efficiency compared to standard GRFs.

## Weaknesses
The paper does not have any major weaknesses. It would be beneficial to have more real-world data examples to demonstrate the practical utility of the proposed method.

## Questions
None.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4