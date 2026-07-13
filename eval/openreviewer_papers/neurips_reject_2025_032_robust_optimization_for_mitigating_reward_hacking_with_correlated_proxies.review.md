# Review

## Summary
The paper considers the problem of reward hacking in reinforcement learning (RL) where an agent is optimized with respect to a proxy reward function that is correlated with the true reward but may not be identical. The paper builds on a previous framework called ORPO that uses occupancy regularization to mitigate reward hacking. The paper proposes a robust optimization framework that considers the worst-case scenario within the class of proxy reward functions that are correlated with the true reward. The paper also introduces a linear max-min variant that assumes the true reward is a linear function of known features, which allows for interpretability and tractability. The paper evaluates the proposed methods on several environments and shows that they outperform ORPO in terms of worst-case performance and achieve more stable results across different levels of proxy-true reward correlation.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper addresses an important problem in RL, namely reward hacking, which can lead to unintended and suboptimal behavior of agents.
- The paper proposes a novel and principled framework that formulates reward hacking as a robust optimization problem over the space of all r-correlated proxy rewards.
- The paper introduces a tractable max-min formulation that maximizes performance under the worst-case proxy consistent with the correlation constraint.
- The paper shows that when the reward is a linear function of known features, the approach can be adapted to incorporate this prior knowledge, yielding improved policies and interpretable worst-case rewards.
- The paper evaluates the proposed methods on several environments and shows that they outperform the baseline method ORPO in terms of worst-case performance and achieve more stable results across different levels of proxy-true reward correlation.

## Weaknesses
- The paper does not provide a theoretical analysis of the proposed method, such as convergence guarantees or sample complexity bounds.
- The paper does not provide a detailed comparison of the computational complexity of the proposed method versus the baseline method ORPO.
- The paper does not provide a discussion of the limitations of the proposed method, such as the assumptions made or the scenarios where it may not be applicable.

## Questions
- How does the proposed method compare to other existing methods for mitigating reward hacking, such as inverse reward design or causal confusion mitigation?
- Can the proposed method be extended to other types of RL problems, such as offline RL or multi-agent RL?
- How sensitive is the proposed method to the choice of the reference policy, which is used to define the correlation with the true reward?
- How can the proposed method be used in practice when the true reward is unknown or difficult to specify, which is often the case in real-world applications?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4