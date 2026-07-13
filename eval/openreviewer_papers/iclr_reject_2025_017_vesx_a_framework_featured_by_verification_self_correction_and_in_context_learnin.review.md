# Review

## Summary
The paper presents VeSX, a framework designed for web automation tasks using large language models (LLMs). VeSX introduces three key innovations: subgoal-guided verification, hierarchical self-correction, and an exemplar bank for in-context learning. These features aim to improve the feasibility of subtasks, enhance planning and execution accuracy, and increase the model's adaptability to complex web environments. The framework is evaluated on the WebArena benchmark, where it achieves a state-of-the-art average success rate of 34% across five scenarios.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper presents VeSX, a framework designed for web automation tasks using large language models (LLMs). VeSX introduces three key innovations: subgoal-guided verification, hierarchical self-correction, and an exemplar bank for in-context learning. These features aim to improve the feasibility of subtasks, enhance planning and execution accuracy, and increase the model's adaptability to complex web environments. The framework is evaluated on the WebArena benchmark, where it achieves a state-of-the-art average success rate of 34% across five scenarios.

2. The paper is well-structured, with clear explanations of each component of VeSX and detailed descriptions of the evaluation setup and results.

## Weaknesses
1. The paper does not sufficiently address how VeSX handles errors in self-verification or the implications of relying on hierarchical self-correction mechanisms in real-world applications where subtask failures may be more complex.

2. While VeSX performs well on specific benchmarks, it is unclear how well these results generalize to other types of web automation tasks or more diverse real-world scenarios.

3. The paper could benefit from a more detailed comparison with human-guided methods to understand the limitations and advantages of relying on autonomous planning and execution by the LLM.

## Questions
1. How does VeSX handle errors in self-verification, and what are the consequences of incorrect self-verification in the planning and execution phases?

2. Could the authors provide more details on how the exemplar bank is constructed and maintained, and how it ensures the retrieval of relevant examples?

3. What are the computational costs associated with VeSX, particularly in terms of memory usage and processing time for the exemplar bank and self-correction mechanisms?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4