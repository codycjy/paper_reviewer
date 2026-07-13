# Review

## Summary
This paper introduces a novel method, DTWIL, for action-constrained imitation learning. The authors propose a trajectory alignment process that uses DTW to measure the distance between the expert's trajectory and the agent's trajectory, and employ MPC to optimize the agent's trajectory to reduce this distance. The aligned trajectories are then used to train a behavioral cloning policy. The method is evaluated on several tasks in the Mujoco simulation environment, demonstrating good performance compared to several baselines.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper is well-motivated, addressing the problem of action-constrained imitation learning, which is relevant to real-world applications such as robot control.

2. The proposed DTWIL method is novel, particularly in its use of DTW for trajectory alignment in the context of action-constrained imitation learning.

3. The method is evaluated on several tasks in the Mujoco simulation environment, showing good performance compared to several baselines.

## Weaknesses
1. The paper does not provide sufficient details on how the MPC optimization is performed, including the specific optimization objective and constraints used. This makes it difficult to fully understand or reproduce the method.

2. The method involves several hyperparameters, such as the planning horizon and the rejection sampling threshold, but the paper does not provide a sensitivity analysis or guidelines for selecting these hyperparameters.

3. The evaluation is limited to several tasks in the Mujoco simulation environment. The method's performance on more complex or diverse environments, such as those encountered in real-world robotics applications, is not demonstrated.

4. The paper does not provide a thorough comparison with existing methods for action-constrained reinforcement learning or imitation learning. The baselines used in the evaluation are not state-of-the-art, and the paper does not discuss how DTWIL compares to more advanced methods.

## Questions
1. Can you provide more details on the specific optimization objective and constraints used in the MPC optimization? How is the trade-off between optimizing for DTW distance and satisfying the action constraints managed?

2. How are the hyperparameters, such as the planning horizon and the rejection sampling threshold, selected? Have you performed a sensitivity analysis to evaluate the method's robustness to these hyperparameters?

3. How does DTWIL compare to more advanced methods for action-constrained reinforcement learning or imitation learning? Have you evaluated the method on more complex or diverse environments to assess its generalization capabilities?

4. How does the computational cost of DTWIL compare to the baselines? Is the increased computational cost justified by the improved performance?

5. Can you provide more details on the implementation of the method, including the specific algorithms used for MPC optimization and trajectory alignment? This would help in reproducing the results and understanding the method's implementation details.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4