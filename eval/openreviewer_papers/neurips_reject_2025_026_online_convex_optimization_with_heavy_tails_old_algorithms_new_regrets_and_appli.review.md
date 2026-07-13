# Review

## Summary
This paper examines different old algorithms for OCO (e.g., Online Gradient Descent) in the more challenging heavy-tailed setting. Under the standard bounded domain assumption, the authors establish new regrets for these classical methods without any algorithmic modification. These regret bounds are fully optimal in all parameters and suggest that OCO with heavy tails can be solved effectively without any extra operation (e.g., gradient clipping).

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The authors provide some theoretical guarantees for OCO with heavy tails.

## Weaknesses
1. The motivation is unclear. Why is it important to study OCO with heavy tails? What are the practical applications of OCO with heavy tails? The authors should provide some examples.

2. The bounded domain assumption is too strong. Many machine learning models, such as deep neural networks, have an unbounded domain. Therefore, the theoretical results of this paper have limited practical value.

3. The theoretical proof techniques used in this paper are standard and there is no technical novelty. The authors should highlight the technical contribution of this paper.

4. This paper is not well-written and there are many typos. For example, in Line 21, round should be rounds; in Line 26, subgradient should be subgradient set; in Line 28, inequality should be an equality; in Line 112, the fourth point should be an assumption (the stochastic noise $\epsilon_t$ satisfies ...).

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4