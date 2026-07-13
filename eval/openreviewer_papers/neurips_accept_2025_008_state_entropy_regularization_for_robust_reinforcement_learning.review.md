# Review

## Summary
The paper investigates the theoretical properties of state entropy regularization in reinforcement learning (RL), particularly its robustness to structured perturbations. The authors provide theoretical guarantees, showing that state entropy regularization improves robustness to certain types of perturbations more effectively than policy entropy regularization. The paper also discusses practical considerations, such as the sensitivity of state entropy regularization to the number of rollouts used for policy evaluation.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper provides a rigorous theoretical analysis of state entropy regularization, including its robustness properties and limitations.
- The authors offer a comprehensive characterization of the robustness properties of state entropy regularization, including its performance under reward and transition uncertainty.
- The paper highlights the practical considerations of implementing state entropy regularization, such as its sensitivity to the number of rollouts used for policy evaluation.

## Weaknesses
- The paper does not provide a detailed comparison with other robust RL methods, which could help to contextualize the advantages of state entropy regularization.
- The theoretical guarantees provided by the paper are specific to structured perturbations, and it is not clear how well these results generalize to other types of perturbations.
- While the paper discusses the limitations of entropy regularization, it does not provide a comprehensive discussion of the potential drawbacks of state entropy regularization specifically.

## Questions
- How does state entropy regularization compare to other robust RL methods in terms of computational complexity and implementation ease?
- Can the theoretical guarantees provided in the paper be generalized to other types of perturbations beyond structured perturbations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4