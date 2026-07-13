# Review

## Summary
The paper proposes a novel method for in-context imitation learning (ICIL) in robotics. The key idea is to frame ICIL as a graph generation problem, where a diffusion model learns to predict robot actions based on a context of demonstrations and current observations. The graph representation enables structured reasoning and effective learning from limited data. The model can be trained using procedurally generated pseudo-demonstrations, providing a scalable source of training data. The approach achieves strong performance in both simulated and real-world experiments, outperforming baselines and enabling efficient learning of everyday robot tasks with just one or two demonstrations.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a novel and elegant formulation of ICIL as a graph generation problem. This allows the model to effectively reason about the relationships between demonstrations, current observations, and predicted actions.
2. The use of a diffusion model to learn the action distribution within the graph framework is innovative and well-suited for capturing complex action sequences.
3. The approach addresses the challenge of limited robot data by leveraging procedurally generated pseudo-demonstrations, which provides a virtually unlimited source of training data.
4. The paper includes thorough experiments in both simulation and real-world settings, demonstrating the effectiveness of the approach across various everyday tasks.

## Weaknesses
1. The method assumes the availability of segmented point clouds for observations, which may limit its applicability in scenarios where such data is not readily available or practical to obtain.
2. The current implementation focuses on relatively short-horizon tasks, and it is unclear how well the approach would scale to longer-horizon tasks requiring more complex planning.
3. The paper does not address the challenge of collision avoidance or provide end-to-end control of the full robot configuration space, which are important considerations for practical robotic applications.

## Questions
1. How does the performance of Instant Policy scale with the complexity of the tasks, particularly for longer-horizon tasks that require more sophisticated planning and decision-making?
2. What are the potential approaches to extend the method to handle raw, unsegmented sensor data, such as images or point clouds without explicit segmentation?
3. How can the method be adapted to incorporate collision avoidance and full robot control, while maintaining the benefits of in-context learning and diffusion-based action prediction?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4