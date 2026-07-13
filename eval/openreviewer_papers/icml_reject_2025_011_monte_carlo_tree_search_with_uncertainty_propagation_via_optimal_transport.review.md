# Review

## Summary
The paper introduces a novel backup strategy for Monte-Carlo Tree Search (MCTS) tailored for highly stochastic and partially observable Markov decision processes. The authors model both value and action-value nodes as Gaussian distributions and introduce a backup operator that computes value nodes as the Wasserstein barycenter of their action-value children nodes. This approach allows for the propagation of uncertainty from the leaves to the root node. The paper also explores a combination of the L1-Wasserstein barycenter with α-divergence and establishes a connection to the generalized mean backup operator. To complement this probabilistic backup operator, the authors propose two sampling strategies: optimistic selection and Thompson sampling. Theoretical guarantees are provided for the asymptotic convergence of the algorithm to the optimal policy, and the method is empirically evaluated on several stochastic and partially observable environments, where it outperforms well-known related baselines.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
The paper presents a novel approach to backup strategies in MCTS, which is a significant contribution to the field of reinforcement learning. By modeling nodes as Gaussian distributions and using the L1-Wasserstein barycenter with α-divergence, the method effectively handles high variance and partial observability. The paper provides theoretical guarantees for the convergence of the algorithm, which adds credibility to the proposed method.

## Weaknesses
The paper could benefit from a more detailed comparison with existing methods, particularly in terms of computational complexity and empirical performance. While the authors mention that their method outperforms related baselines, a more in-depth analysis and discussion of the results would strengthen the paper. Additionally, the paper could provide more insight into the practical applications and limitations of the proposed method, as well as potential future directions for research.

## Questions
1. How does the proposed method compare to existing distributional MCTS approaches in terms of computational complexity and empirical performance?
2. Can the authors provide more insight into the practical applications of the proposed method, and are there any specific domains where it is expected to perform particularly well or poorly?
3. How sensitive is the method to the choice of hyperparameters, and are there any guidelines for selecting these parameters in practice?
4. How does the method handle very large or infinite state spaces, and what are the potential limitations in such scenarios?
5. Can the authors provide more details on the experimental setup and hyperparameter tuning process, including any ablation studies conducted?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4