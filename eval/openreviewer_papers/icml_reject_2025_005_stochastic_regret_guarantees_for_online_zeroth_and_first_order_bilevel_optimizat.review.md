# Review

## Summary
This paper studies the online bilevel optimization problem, which is a generalization of single-level online convex optimization. The paper proposes a first-order and a zeroth-order algorithm. The first-order algorithm achieves $O(T^{-2/3})$ stochastic regret and the zeroth-order algorithm achieves $O(T^{-1/3})$ stochastic regret. Numerical experiments are conducted to verify the performance of the proposed algorithms.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The theoretical results are well presented.

2. The theoretical results are novel and interesting. In particular, the regret bound of the first-order algorithm improves upon the previous best-known result by a factor of $T$.

## Weaknesses
1. The paper lacks a discussion on the technical contributions. In particular, it is not clear to me why the new search direction (6a)-(6c) helps improve the regret bound. A more detailed discussion on this would be helpful.

2. The paper lacks a discussion on the lower bound. It would be helpful to provide a lower bound to show the optimality of the regret bounds.

## Questions
1. Can the authors provide some insights on why the new search direction (6a)-(6c) helps improve the regret bound?

2. Can the authors provide a lower bound to show the optimality of the regret bounds?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4