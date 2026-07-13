# Review

## Summary
The paper introduces a novel backup strategy for Monte-Carlo Tree Search (MCTS) tailored for highly stochastic and partially observable Markov decision processes. The authors adopt a probabilistic approach, modeling both value and action-value nodes as Gaussian distributions, to introduce a novel backup operator that computes value nodes as the Wasserstein barycenter of their action-value children nodes; thus, propagating the uncertainty of the estimate across the tree to the root node. The authors study their novel backup operator when using a novel combination of L1-Wasserstein barycenter with α-divergence, by drawing a crucial connection to the generalized mean backup operator. The authors complement their probabilistic backup operator with two sampling strategies, based on optimistic selection and Thompson sampling, obtaining their Wasserstein MCTS algorithm. The authors provide theoretical guarantees of asymptotic convergence of O(n−1/2), with n as the number of visited trajectories, to the optimal policy and an empirical evaluation on several stochastic and partially observable environments, where their approach outperforms well-known related baselines.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
The paper proposes a novel backup strategy for Monte-Carlo Tree Search (MCTS) tailored for highly stochastic and partially observable Markov decision processes. The authors adopt a probabilistic approach, modeling both value and action-value nodes as Gaussian distributions, to introduce a novel backup operator that computes value nodes as the Wasserstein barycenter of their action-value children nodes; thus, propagating the uncertainty of the estimate across the tree to the root node. The authors study their novel backup operator when using a novel combination of L1-Wasserstein barycenter with α-divergence, by drawing a crucial connection to the generalized mean backup operator. The authors complement their probabilistic backup operator with two sampling strategies, based on optimistic selection and Thompson sampling, obtaining their Wasserstein MCTS algorithm. The authors provide theoretical guarantees of asymptotic convergence of O(n−1/2), with n as the number of visited trajectories, to the optimal policy and an empirical evaluation on several stochastic and partially observable environments, where their approach outperforms well-known related baselines.

## Weaknesses
The authors do not provide a clear and detailed explanation of how their approach outperforms well-known related baselines. They do not provide a thorough comparison of their method with existing methods, nor do they provide a detailed analysis of the reasons behind the improved performance. Additionally, the authors do not provide a clear and detailed explanation of how their approach handles high stochasticity and partial observability, nor do they provide a thorough analysis of the limitations of their method in these scenarios. Overall, the authors do not provide a clear and detailed explanation of how their approach outperforms well-known related baselines, nor do they provide a thorough analysis of the reasons behind the improved performance and the handling of high stochasticity and partial observability.

## Questions
1. Can the authors provide a clear and detailed explanation of how their approach outperforms well-known related baselines? 
2. Can the authors provide a thorough comparison of their method with existing methods, and a detailed analysis of the reasons behind the improved performance? 
3. Can the authors provide a clear and detailed explanation of how their approach handles high stochasticity and partial observability, and a thorough analysis of the limitations of their method in these scenarios?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4