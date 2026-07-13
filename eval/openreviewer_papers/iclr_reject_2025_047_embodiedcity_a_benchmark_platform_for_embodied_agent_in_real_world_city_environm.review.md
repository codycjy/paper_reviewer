# Review

## Summary
This paper presents a new benchmark for embodied agents, set in a realistic city environment. The simulator includes a 2.8km x 2.4km district of Beijing, with 3D models for buildings, streets, etc. The environment supports both drones and vehicles, and offers a range of tasks including scene understanding, QA, dialogue, navigation and task planning. The authors have also evaluated several popular LLMs on this benchmark.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The simulator is based on a real city district, which makes it more realistic and useful for training and evaluating embodied agents.
2. The tasks cover a wide range of embodied AI abilities, from perception to planning.
3. The authors have evaluated several popular LLMs on this benchmark, providing a good starting point for future research.

## Weaknesses
1. The benchmark only covers a small district of Beijing, which may limit the diversity of the environments. How does the environment support different agents? For example, robots with different sensors and effectors, or agents with different morphology. It is unclear how the simulator can be extended or modified to support these different agents. I am also curious about how the simulator can support agents with different levels of perception and action capabilities.
2. The tasks are all based on language inputs and outputs, which may not fully capture the challenges of embodied agents that need to reason and act in the environment. For example, how would the performance of these LLMs change if the input and output are in the form of sensor readings and control commands? This could be more relevant for embodied agents that need to operate in the environment.
3. The evaluation of the LLMs is based on standard language evaluation metrics (BLEU, ROUGE, etc.), which may not fully capture the performance of the agents in the environment. For example, how would the evaluation change if the performance is measured by the distance the agent travels, or the success rate of completing tasks? This could provide a more comprehensive assessment of the agents' capabilities in the environment.

## Questions
1. How does the environment support different agents? For example, robots with different sensors and effectors, or agents with different morphology. It is unclear how the simulator can be extended or modified to support these different agents. I am also curious about how the simulator can support agents with different levels of perception and action capabilities.
2. The tasks are all based on language inputs and outputs, which may not fully capture the challenges of embodied agents that need to reason and act in the environment. For example, how would the performance of these LLMs change if the input and output are in the form of sensor readings and control commands? This could be more relevant for embodied agents that need to operate in the environment.
3. The evaluation of the LLMs is based on standard language evaluation metrics (BLEU, ROUGE, etc.), which may not fully capture the performance of the agents in the environment. For example, how would the evaluation change if the performance is measured by the distance the agent travels, or the success rate of completing tasks? This could provide a more comprehensive assessment of the agents' capabilities in the environment.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4