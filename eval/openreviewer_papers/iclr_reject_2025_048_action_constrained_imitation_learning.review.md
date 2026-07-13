# Review

## Summary
This paper introduces Action-Constrained Imitation Learning (ACIL), a new problem setting where an agent with limited action capabilities seeks to learn from expert demonstrations with a broader action scope. The key challenge in ACIL is the mismatch in occupancy measures between the expert and the constrained agent, which traditional imitation learning methods struggle to address. The authors propose DTWIL, a novel method that uses trajectory alignment through Dynamic Time Warping (DTW) and Model Predictive Control (MPC) to create surrogate expert demonstrations that adhere to the agent’s action constraints. The approach generates a surrogate dataset that follows similar state trajectories to the expert’s, allowing for effective policy learning under the agent’s action limitations. Experimental results across various robot control tasks, including navigation and locomotion, demonstrate that DTWIL significantly improves performance and sample efficiency compared to existing imitation learning methods, particularly in environments with restrictive action sets.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper addresses the novel problem of Action-Constrained Imitation Learning (ACIL), which is highly relevant for applications involving robots or agents with limited action capabilities. This setting extends traditional imitation learning by tackling the specific challenge of learning from expert demonstrations while adhering to action constraints, which is critical for safe and effective operation in real-world environments.
2. The proposed DTWIL method is well-designed and effectively tackles the mismatch in occupancy measures between the expert and the imitator. By using Dynamic Time Warping (DTW) and Model Predictive Control (MPC), DTWIL aligns surrogate trajectories with expert trajectories while respecting the action constraints, providing a practical solution to the challenges of ACIL.
3. The paper includes extensive experiments across various environments, demonstrating the effectiveness of DTWIL in navigation and locomotion tasks. The results show that DTWIL outperforms several benchmark imitation learning algorithms in terms of sample efficiency, which is particularly valuable in settings where data collection is costly or limited.

## Weaknesses
1. The paper does not provide a theoretical analysis of the proposed method. While the empirical results are strong, a theoretical foundation could help clarify the convergence properties and potential limitations of DTWIL. For instance, a theoretical analysis could address the conditions under which DTWIL ensures an optimal or near-optimal policy, or it could provide insights into how DTWIL handles the trade-off between imitation accuracy and action feasibility. Such a theoretical component could also strengthen the understanding of how DTWIL fits within the broader landscape of imitation learning and reinforcement learning methods.
2. The experiments are conducted in relatively simple environments. While the chosen tasks, such as Maze2d and HalfCheetah, are commonly used benchmarks, they do not fully capture the complexity of many real-world applications. Real-world tasks often involve more dynamic and unpredictable environments, such as varying terrain or other agents, which can challenge the robustness of the proposed method. Testing DTWIL in more complex scenarios, such as robotic manipulation tasks or dynamic obstacle avoidance, could provide a more comprehensive evaluation of its effectiveness and highlight any potential limitations.
3. The paper does not extensively discuss the computational cost of DTWIL, particularly the time required for trajectory alignment using DTW and MPC. Given that DTWIL involves generating surrogate expert demonstrations through trajectory alignment, the computational overhead could be significant, especially in high-dimensional action spaces. Providing an analysis of the computational time and memory requirements for DTWIL, especially in comparison to other methods, would help clarify its scalability and feasibility for deployment in real-time applications. This discussion could also suggest potential optimizations to reduce computational costs without sacrificing performance.
4. The paper could benefit from a more detailed discussion on the limitations of the proposed method. While the experimental results are promising, it would be valuable to address potential challenges or scenarios where DTWIL might not perform as expected. For instance, it would be helpful to analyze whether DTWIL can effectively handle environments with highly non-linear dynamics or where the action constraints vary significantly over time. Additionally, discussing potential failure cases or scenarios where the surrogate trajectories might diverge significantly from the expert’s path could provide insights into the robustness and applicability of DTWIL.

## Questions
1. Could the authors provide a theoretical analysis or convergence guarantees for DTWIL? How does DTWIL ensure an optimal or near-optimal policy, and what are the conditions under which it is most effective?
2. How does DTWIL perform in more complex environments, such as robotic manipulation tasks or dynamic obstacle avoidance? Could the authors provide additional experiments in these scenarios to demonstrate the robustness and scalability of their method?
3. Could the authors provide a detailed analysis of the computational cost of DTWIL, particularly the time required for trajectory alignment using DTW and MPC? How does the computational overhead of DTWIL compare to other methods, and are there potential optimizations to reduce these costs without sacrificing performance?
4. Could the authors discuss the limitations of DTWIL in more detail? Are there specific scenarios or environments where DTWIL might not perform as expected? Additionally, could the authors provide examples of potential failure cases or situations where the surrogate trajectories might diverge significantly from the expert’s path?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4