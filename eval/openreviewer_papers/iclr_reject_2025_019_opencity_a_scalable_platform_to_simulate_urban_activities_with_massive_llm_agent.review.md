# Review

## Summary
This paper presents OpenCity, a scalable simulation platform optimized for both system and prompt efficiencies. OpenCity includes a LLM request scheduler to reduce communication overhead by parallelizing requests through IO multiplexing and a "group-and-distill" prompt optimization strategy to minimize redundancy by clustering agents with similar static attributes. Through experiments on six global cities, OpenCity achieves a 600-fold acceleration in simulation time per agent, a 70% reduction in LLM requests, and a 50% reduction in token usage. These improvements enable the simulation of 10,000 agents’ daily activities in 1 hour on commodity hardware.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. OpenCity introduces a group-and-distill prompt strategy that reduces token usage by 45.5% and achieves a 635x acceleration in simulation time, enabling the simulation of 10,000 agents in just 1 hour.

2. OpenCity establishes a benchmark for LLM agents in urban activity simulation, comparing simulated behaviors with real-world data from six major cities.

3. OpenCity provides a user-friendly web interface, allowing researchers without programming backgrounds to configure simulations and visualize results easily.

## Weaknesses
1. The evaluation metrics primarily focus on acceleration and efficiency improvements. It would be beneficial to include more direct assessments of the simulation quality, such as comparisons with real-world urban data or evaluations using established metrics like the Mean Squared Error (MSE) for agent-based model simulations.

2. The paper could provide more detailed information about the hardware specifications used in the experiments, such as the number of CPU cores and type of network interface. This would help clarify the computational resources required to achieve the reported performance improvements.

3. It would be helpful to include a more comprehensive comparison with existing simulation platforms, highlighting the specific advantages of OpenCity in terms of scalability, speed, and accuracy.

4. The paper could benefit from a more detailed explanation of the "group-and-distill" strategy, including examples of how agents are clustered and how this approach reduces token usage. This would help readers better understand the key contributions of the paper.

## Questions
1. How does OpenCity handle the variability in response times from different LLMs, especially when using commercial LLMs accessed via APIs? Are there any strategies implemented to mitigate the impact of delays?

2. How does OpenCity manage the computational resources, such as CPU and memory, to ensure optimal performance, especially when dealing with a large number of agents?

3. Can you provide more details about the hardware specifications used in your experiments, such as the number of CPU cores and type of network interface?

4. How does OpenCity compare with other existing simulation platforms in terms of scalability, speed, and accuracy?

5. Can you provide more detailed explanations of the "group-and-distill" strategy, including examples of how agents are clustered and how this approach reduces token usage?

6. How does OpenCity handle the potential increase in token usage when the number of agents increases, and are there any mechanisms in place to manage this?

7. How does OpenCity ensure the reproducibility of the experiments, and are the results consistent across different runs?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4