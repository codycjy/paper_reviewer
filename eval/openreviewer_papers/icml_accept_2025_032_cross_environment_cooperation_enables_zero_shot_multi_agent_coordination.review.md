# Review

## Summary
This paper studies the problem of zero-shot coordination in cooperative multi-agent reinforcement learning. In particular, the authors propose a new paradigm called Cross-Environment Cooperation (CEC) that uses self-play training on a distribution of procedurally generated environments to learn general cooperative skills that transfer to new partners and new problems. The authors evaluate CEC on the Overcooked environment and demonstrate that it outperforms competitive baselines both quantitatively and qualitatively when collaborating with real people.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a thorough explanation of their proposed method.

2. The idea of using procedural environment generation to improve generalization in multi-agent reinforcement learning is interesting and novel.

3. The authors conduct extensive experiments on both AI-AI and Human-AI collaboration tasks, and the results show that CEC can outperform existing methods in terms of both reward and human subjective preferences.

## Weaknesses
1. The authors only evaluate their proposed method on the Overcooked environment, which is a simplified cooperative task. It would be more convincing if the authors could demonstrate the effectiveness of CEC on more complex and diverse tasks.

2. The authors do not provide a theoretical analysis of why CEC can improve generalization. A better understanding of the underlying principles of CEC could provide more insights and guidance for future research.

3. The authors do not compare their proposed method with some of the latest state-of-the-art methods for zero-shot coordination, such as [1] and [2]. Including these comparisons could provide a more comprehensive evaluation of CEC.

[1] Liang, Yancheng, et al. "Learning to Cooperate with Humans Using Generative Agents." arXiv preprint arXiv:2411.13934 (2024).

[2] Wang, Xiang, et al. "Quantifying Zero-Shot Coordination Capability with Behavior Preferring Partners." arXiv preprint arXiv:2404.14675 (2024).

## Questions
1. Can you provide a more detailed analysis of the differences between CEC and PBT? What are the key advantages of CEC over PBT?

2. How does CEC compare to other state-of-the-art methods for zero-shot coordination, such as [1] and [2]?

3. Can you provide a theoretical analysis or intuition for why CEC can improve generalization in zero-shot coordination tasks?

4. Have you tested CEC on any other environments or tasks beyond Overcooked? If so, what are the results?

5. How sensitive is CEC to the choice of procedural environment generation algorithm? Have you experimented with different generation algorithms and evaluated their impact on the performance of CEC?

[1] Liang, Yancheng, et al. "Learning to Cooperate with Humans Using Generative Agents." arXiv preprint arXiv:2411.13934 (2024).

[2] Wang, Xiang, et al. "Quantifying Zero-Shot Coordination Capability with Behavior Preferring Partners." arXiv preprint arXiv:2404.14675 (2024).

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4