# Review

## Summary
The paper proposes a temporally sparse attack (TSA) on LLM-based time series forecasters. The attack is formulated as a cardinality-constrained optimization problem, which is solved by subspace pursuit. The results show that TSA can degrade the performance of LLM-based forecasters with only 10% of the input being modified.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The problem of attacking LLM-based forecasters is interesting.

## Weaknesses
1. The threat model is not well justified. The paper assumes that the attacker has no access to the training data, the internal structure or parameters of the LLM-based forecasting model, and the ground truth values. However, it is unclear how the attacker can affect the input without accessing the training data or the internal structure of the model. It is also unclear why the attacker cannot access the ground truth values, as they are the actual values that the forecaster is trying to predict.
2. The assumption that the attacker can query the target model is too strong. If the attacker can query the model, they can extract information about the model's internal structure and parameters, which contradicts the assumption that the attacker has no access to the internal structure or parameters of the LLM-based forecasting model.
3. The motivation for using CCOP and SP is not well explained. There are many optimization algorithms that can enforce sparsity constraints. What is the reason for using SP?
4. The paper does not compare TSA with any baseline attacks. It would be helpful to compare TSA with other attack methods, such as full-series attacks or attacks that modify a larger portion of the input.

## Questions
Please see the weaknesses above.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4