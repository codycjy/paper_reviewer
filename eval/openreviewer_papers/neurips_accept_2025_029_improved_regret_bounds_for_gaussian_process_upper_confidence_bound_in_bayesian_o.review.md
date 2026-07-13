# Review

## Summary
This paper addresses the Bayesian optimization problem (also referred to as the Bayesian setting of the Gaussian process bandit), where the learner seeks to minimize the regret under a function drawn from a known Gaussian process (GP). Under a Matérn kernel with a certain degree of smoothness, the authors show that the Gaussian process upper confidence bound (GP-UCB) algorithm achieves $\widetilde{O}(\sqrt{T})$ cumulative regret with high probability. Furthermore, for a squared exponential kernel, they establish $O(\sqrt{T\ln^2T})$ regret of GP-UCB. These results fill the gap between the existing regret upper bound for GP-UCB and the best-known bound provided by Scarlett [46]. The key idea in the paper's proof is to capture the concentration behavior of the input sequence realized by GP-UCB, enabling a more refined analysis of the GP's information gain.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The authors provide a refined analysis of GP-UCB in the BO problem. For both SE and Matérn kernels, the results improve upon existing regret guarantees and fill the gap between the existing regret of GP-UCB and the current best upper bound in [46].

## Weaknesses
1. The authors claim that the key idea in their proof is to capture the concentration behavior of the input sequence realized by GP-UCB, enabling a more refined analysis of the GP's information gain. However, in my opinion, the idea is not novel enough. The concentration behavior of the input sequence has already been used in the analysis of the GP-UCB algorithm, such as in the work by Janz et al. [28]. The main idea of the paper is to use the concentration behavior of the input sequence to refine the existing information gain bounds, which seems to be an incremental contribution.

## Questions
1. The paper only considers the one-dimensional setting. Can the results be extended to the multi-dimensional setting? If so, what would be the main challenges and difficulties?
2. The authors only consider the Bayesian setting of the Gaussian process bandit problem. Can the results be extended to the frequentist setting? If so, what would be the main challenges and difficulties?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4