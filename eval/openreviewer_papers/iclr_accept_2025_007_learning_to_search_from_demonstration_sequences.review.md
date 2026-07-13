# Review

## Summary
This paper introduces a novel approach for integrating search into a neural network architecture. The authors propose a Differentiable Tree Search Network (D-TSN) that learns to construct search trees from sequences of expert demonstrations. The key innovation is using gradient descent to optimize the search process, even when the world model is unknown. The authors employ a stochastic tree expansion policy and optimize it using REINFORCE with variance reduction. The method is evaluated on tasks requiring long-horizon planning, including a reasoning task (Game of 24), a 2D grid navigation task, and Procgen games. The results show that D-TSN outperforms baselines, especially when the world model needs to be jointly learned.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
1. The paper addresses an important problem in reinforcement learning and planning: how to effectively integrate search when only demonstration sequences are available, without explicit access to a search tree or a known world model.
2. The proposed solution is novel and theoretically sound. The use of a stochastic tree expansion policy and optimization via REINFORCE is a creative approach to make the learning process differentiable.
3. The paper provides a thorough theoretical analysis, including proofs of the continuity of the loss function and detailed derivations of the gradient computations.

## Weaknesses
1. The paper's main weakness lies in its experimental evaluation. While the method is tested on three different domains, the evaluation could be more comprehensive. The authors should consider using standard benchmarks in reinforcement learning and planning to better compare their method against existing approaches.
2. The paper lacks a thorough analysis of the computational complexity of the proposed method. The authors should provide a detailed comparison of the computational requirements of D-TSN against the baselines, especially in terms of the number of iterations needed for training and inference.
3. The paper does not provide a clear analysis of the sensitivity of the method to hyperparameters. The authors should include a hyperparameter sensitivity analysis to show how robust the method is to different configurations.

## Questions
1. Can you provide more details on the computational complexity of D-TSN compared to the baselines? How does the number of iterations required for training and inference compare?
2. How sensitive is D-TSN to the choice of hyperparameters? Can you provide a hyperparameter sensitivity analysis to show the robustness of the method?
3. The paper mentions that D-TSN can learn a world model jointly. How does the quality of the learned world model compare to a separately learned one? Can you provide an analysis of the compounding errors in the world model during deeper searches?
4. How does D-TSN compare to other methods that embed search inductive biases into neural network architectures, such as NEAR and MCTSnets? Can you provide a comparison against these methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4