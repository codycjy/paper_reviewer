# Review

## Summary
The paper proposes SymMaP, a symbolic regression framework to learn preconditioning parameters as symbolic expressions. The authors then integrate these expressions into a linear system solver. SymMaP is compared against other preconditioning strategies on several partial differential equation (PDE) problems.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper is well-written and easy to follow. 

- The problem of preconditioning parameter selection is well-motivated. 

- The proposed framework SymMaP is evaluated on several PDE problems.

## Weaknesses
- The paper lacks novelty. The idea of using symbolic regression to learn preconditioning parameters was already proposed in [1]. 

- The experimental evaluation is insufficient. The paper lacks a comparison against existing ML-based preconditioning approaches. 

- The paper lacks a discussion of the limitations of the proposed approach. 

[1] Chen, X., Liang, C., Huang, D., Real, E., Wang, K., Pham, H., Dong, X., Luong, T., Hsieh, C.J. and Lu, Y., 2024. Symbolic discovery of optimization algorithms. Advances in neural information processing systems, 36.

## Questions
- What are the limitations of the proposed approach? 

- How does SymMaP compare against existing ML-based preconditioning approaches, e.g., those mentioned in the related work section?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4