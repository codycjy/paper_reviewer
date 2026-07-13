# Review

## Summary
The paper presents a computationally efficient algorithm for reinforcement learning in linear Bellman complete MDPs with deterministic dynamics. The algorithm is based on randomized least squares value iteration and leverages a span argument to bound the regret. The paper provides regret bounds and sample complexity bounds for the algorithm under various assumptions on the MDP, such as exact and approximate square loss minimization oracles, and low inherent linear Bellman error.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper makes a significant contribution to the field of reinforcement learning by providing the first computationally efficient algorithm for linear Bellman complete MDPs with deterministic dynamics. The algorithm and its analysis are novel and non-trivial, and the paper provides a thorough and clear presentation of the results.

## Weaknesses
The paper has a few weaknesses that should be addressed. First, the algorithm and its analysis are not fully explained, and some parts of the paper are difficult to follow. Second, the paper does not provide any empirical evaluation of the proposed algorithm, which would help to validate the theoretical results and demonstrate the practical effectiveness of the algorithm. Third, the paper does not provide any discussion of the limitations of the proposed algorithm or potential directions for future research.

## Questions
1. Can you provide a more detailed explanation of the algorithm and its analysis? Specifically, can you elaborate on the choice of the noise variances and the D-optimal design, and how these choices affect the performance of the algorithm?
2. Can you provide empirical evaluation of the algorithm on some benchmark RL environments? This would help to validate the theoretical results and demonstrate the practical effectiveness of the algorithm.
3. Can you provide a discussion of the limitations of the proposed algorithm and potential directions for future research? For example, can you discuss the challenges and opportunities for extending the algorithm to stochastic dynamics, and the potential applications of the algorithm to real-world RL problems?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4