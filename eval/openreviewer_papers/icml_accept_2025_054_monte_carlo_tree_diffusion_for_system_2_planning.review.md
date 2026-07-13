# Review

## Summary
This paper presents Monte Carlo Tree Diffusion (MCTD), a novel framework that combines diffusion models with Monte Carlo Tree Search (MCTS) to improve planning in complex, long-horizon tasks. MCTD addresses limitations in standard diffusion-based planners by integrating a tree structure, allowing it to manage exploration-exploitation trade-offs and refine plans iteratively. Empirical results show that MCTD outperforms existing diffusion baselines, achieving better solution quality as inference time increases.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. This paper proposes a novel framework that integrates diffusion models with Monte Carlo Tree Search (MCTS). 
2. This paper is well-written and easy to follow.

## Weaknesses
1. The experimental scenarios are overly simplistic. The authors only test their method on a few tasks from OGBench, which are relatively simple and do not reflect the complexity of real-world tasks. For example, the authors could test their method on more complex tasks such as Kitchen, Adroit, or real-world robotic tasks.
2. The authors do not compare their method with other state-of-the-art methods. For example, they could compare with Hierarchical Planning with Diffusion (HPD) [1] and PlanDQ [2].
3. The authors do not analyze the computational complexity of their method. For example, they could analyze the time complexity of their method and compare it with other methods.
4. The authors do not conduct ablation studies on the design choices of their method. For example, they could conduct ablation studies on the number of guidance levels and the jumpy denoising interval.

[1] Chen, C., Deng, F., Kawaguchi, K., Gulcehre, C., & Ahn, S. (2024). Simple Hierarchical Planning with Diffusion. arXiv preprint arXiv:2401.05794.
[2] Chen, C., Baek, D., Deng, F., Kawaguchi, K., Gulcehre, C., & Ahn, S. (2024). PlanDQ: Hierarchical Plan Orchestration via D-Conductor and Q-Performer. arXiv preprint arXiv:2406.04178.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4