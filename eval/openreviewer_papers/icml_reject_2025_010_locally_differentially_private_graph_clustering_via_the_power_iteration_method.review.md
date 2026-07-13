# Review

## Summary
This paper studies the problem of private graph clustering under the edge LDP constraint. The authors propose an interactive algorithm based on the power iteration method. The proposed algorithm achieves constant-level privacy with a minimum degree of $\tilde{\Omega}(\sqrt{n})$, while the previous approaches require $\Omega(\log n)$ privacy budget. The authors provide theoretical analysis and experimental results to demonstrate the effectiveness of their algorithm.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The authors provide clear explanations of the problem setting, related work, and their contributions.
- The proposed algorithm is novel and addresses an important problem in the field. The use of the power iteration method for private graph clustering under edge LDP is a unique approach that has not been explored before.
- The theoretical analysis and experimental results are solid. The authors provide detailed proofs of their theoretical claims and conduct extensive experiments to validate their algorithm.

## Weaknesses
- The proposed algorithm requires a minimum degree of $\tilde{\Omega}(\sqrt{n})$ to achieve accurate results. This condition can be restrictive for sparse graphs. The authors should provide more discussion on the impact of the minimum degree requirement on the practicality of their algorithm.
- The proposed algorithm is interactive, which can limit its applicability in certain scenarios. The authors should discuss potential approaches to make the algorithm non-interactive and provide experimental results comparing the performance of the interactive and non-interactive versions of their algorithm.
- The authors should provide a more detailed comparison with the previous approaches in terms of computational complexity, memory requirements, and performance under different graph densities and sizes. This would help to better position their work in the context of existing research.

## Questions
- How does the proposed algorithm perform on sparse graphs that do not satisfy the minimum degree requirement? Are there any modifications or extensions to the algorithm that could relax this condition?
- Can the proposed algorithm be extended to provide node LDP guarantees? What would be the challenges in doing so?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4