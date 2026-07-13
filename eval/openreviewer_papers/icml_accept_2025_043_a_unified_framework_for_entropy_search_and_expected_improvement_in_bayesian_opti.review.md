# Review

## Summary
This paper proposes a novel acquisition function for Bayesian optimization. The acquisition function is based on the Max-value Entropy Search (MES) strategy. MES aims to maximize the entropy of the unknown function's maximum value given the observed data. This is done by reducing the entropy of the posterior distribution of the unknown function's maximum value given an evaluation at a particular point. The paper proposes a variational inference approach to MES which is computationally more efficient. It also proposes a generalization of the proposed method which uses a gamma distribution instead of an exponential distribution. The paper shows that when the gamma distribution is an exponential distribution, the proposed method is equivalent to the widely used Expected Improvement acquisition function. The paper also presents an extensive empirical evaluation of the proposed method and compares it to EI and MES.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper presents a novel acquisition function for Bayesian optimization. The acquisition function is based on the Max-value Entropy Search (MES) strategy. MES aims to maximize the entropy of the unknown function's maximum value given the observed data. This is done by reducing the entropy of the posterior distribution of the unknown function's maximum value given an evaluation at a particular point. The paper proposes a variational inference approach to MES which is computationally more efficient. It also proposes a generalization of the proposed method which uses a gamma distribution instead of an exponential distribution. The paper shows that when the gamma distribution is an exponential distribution, the proposed method is equivalent to the widely used Expected Improvement acquisition function. The paper also presents an extensive empirical evaluation of the proposed method and compares it to EI and MES.

## Weaknesses
The paper does not discuss the computational complexity of the proposed method. The paper does not discuss the sensitivity of the proposed method to the choice of the variational distribution.

## Questions
1. What is the computational complexity of the proposed method?
2. How sensitive is the proposed method to the choice of the variational distribution?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4