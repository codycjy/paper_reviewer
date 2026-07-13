# Review

## Summary
The paper introduces a Shared Recurrent Memory Transformer (SRMT) to address the challenge of behavior prediction in multi-agent reinforcement learning (MARL). SRMT extends memory transformers to multi-agent settings by pooling and globally broadcasting individual working memories, enabling agents to exchange information implicitly and coordinate their actions. The proposed approach is evaluated on the Partially Observable Multi-Agent Pathfinding problem in a toy Bottleneck navigation task and the POGEMA benchmark set of tasks.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The idea of using shared memory in multi-agent pathfinding problems is interesting. 
2. The proposed method is evaluated on various environments, including a toy Bottleneck navigation task and the POGEMA benchmark set of tasks.

## Weaknesses
1. The paper lacks an analysis of the shared memory. For example, it is unclear how many times the shared memory is read or written, and whether there are any errors in the shared memory. 
2. The paper does not provide a comparison of the proposed method with other multi-agent pathfinding algorithms, such as PRIMAL[1], PRIMAL2[2], DHC[3], and PICO[4]. 
3. The paper does not provide a comparison of the proposed method with other multi-agent reinforcement learning algorithms, such as QPLEX[5], QMIX[6], and MAT[7]. 
4. The paper does not provide a theoretical analysis of the proposed method, such as its convergence properties or computational complexity. 
5. The paper does not provide a discussion of the limitations of the proposed method or potential directions for future research. 
6. The paper does not provide a discussion of the scalability of the proposed method, such as its performance and efficiency in larger-scale environments. 

[1] Sartoretti, Guillaume, et al. "Primal: Pathfinding via reinforcement and imitation multi-agent learning." IEEE Robotics and Automation Letters 4.3 (2019): 2378-2385. 
[2] Damani, Mehul, et al. "PRIMAL 2: Pathfinding via Reinforcement and Imitation Multi-Agent Learning-Lifelong." IEEE Robotics and Automation Letters 6.2 (2021): 2666-2673. 
[3] Ma, Ziyuan, Yudong Luo, and Hang Ma. "Distributed heuristic multi-agent path finding with communication." 2021 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2021. 
[4] Li, Wenhao, et al. "Multi-agent path finding with prioritized communication learning." 2022 International Conference on Robotics and Automation (ICRA). IEEE, 2022. 
[5] Wang, Jianhao, et al. "QPLEX: Duplex dueling multi-agent q-learning." arXiv preprint arXiv:2008.01062 (2020). 
[6] Rashid, Tabish, et al. "Monotonic value function factorisation for deep multi-agent reinforcement learning." Journal of Machine Learning Research 21.178 (2020): 1-51. 
[7] Iqbal, Shariq, and Fei Sha. "Actor-attention-critic for multi-agent reinforcement learning." arXiv preprint arXiv:1810.02912 (2018).

## Questions
1. How does the proposed method perform compared to other multi-agent pathfinding algorithms, such as PRIMAL, PRIMAL2, DHC, and PICO? 
2. How does the proposed method perform compared to other multi-agent reinforcement learning algorithms, such as QPLEX, QMIX, and MAT? 
3. What are the limitations of the proposed method, and what are potential directions for future research? 
4. How scalable is the proposed method, and how does its performance and efficiency change in larger-scale environments? 
5. How does the proposed method handle non-stationarity in multi-agent environments, where agents' behaviors may change over time?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4