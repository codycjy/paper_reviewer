# Review

## Summary
This paper studies the performative reinforcement learning (performative RL) problem, which is a generalization of the standard MDP setting. In performative RL, the agent's policy not only affects the reward function and transition dynamics, but also induces a changing environment. This paper aims to solve the performative RL problem with entropy regularization. The authors provide a gradient dominance property for the performative RL problem, and show that any stationary point of the problem is a performatively optimal policy. Moreover, the authors propose a zero-th order policy gradient method and provide a sample complexity bound.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. This paper provides a gradient dominance property for the performative RL problem, and show that any stationary point of the problem is a performatively optimal policy. This result is novel and significant, since it is the first paper that converges to a performatively optimal policy.

2. The authors propose a zero-th order policy gradient method and provide a sample complexity bound. This result is also novel and significant, since most existing works only provide heuristic algorithms.

## Weaknesses
1. The zero-th order policy gradient method may not be practical, since it requires to query the performative value function at many different points.

2. The algorithm requires to know the exact performative value function, which is usually not the case in practice.

## Questions
1. Is it possible to design a black-box policy optimization algorithm for the performative RL problem? For example, can we apply mirror descent to the performative RL problem? If not, can you provide some intuition on why mirror descent cannot be applied?

2. In the algorithm, we need to compute the performative value function at $\pi+\delta u_i$ and $\pi-\delta u_i$. In practice, how do we compute the performative value function at these points? Do we need to query the environment?

3. In the algorithm, we need to know the exact performative value function. In practice, do we need to know the exact performative value function or we can just use an estimator?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4