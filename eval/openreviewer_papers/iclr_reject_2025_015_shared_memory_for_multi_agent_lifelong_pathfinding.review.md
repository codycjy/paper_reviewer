# Review

## Summary
This paper introduces the Shared Recurrent Memory Transformer (SRMT), a novel approach to multi-agent reinforcement learning (MARL) that addresses the challenge of coordinating agents in partially observable environments. SRMT extends memory transformers to multi-agent settings by pooling and globally broadcasting individual working memories, allowing agents to share information implicitly and coordinate their actions. The authors evaluate SRMT on a toy Bottleneck navigation task and the POGEMA benchmark, demonstrating its effectiveness in achieving cooperation among agents.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- SRMT introduces a unique approach to MARL by incorporating shared recurrent memory, extending memory transformers to multi-agent settings. This allows agents to share information implicitly, which is a novel contribution to the field.
- The paper provides a thorough evaluation of SRMT on standard benchmarks, including a toy Bottleneck navigation task and the POGEMA benchmark. The results demonstrate that SRMT consistently outperforms baseline methods, particularly in challenging scenarios with sparse rewards and extended corridor lengths.
- SRMT shows robust generalization to longer corridors and maze-like environments not seen during training, indicating its scalability and robustness as a coordination mechanism for multi-agent systems.

## Weaknesses
- The paper could benefit from a more detailed comparison with existing MARL methods that use communication or centralized training, such as DCC, MAMBA, and SCRIMP. While SRMT is compared with several baselines, a deeper analysis of how it differs from these methods and why it outperforms them would strengthen the paper's contribution.
- While the paper demonstrates the effectiveness of SRMT in specific tasks, it would be valuable to see how it performs in more complex environments or with a larger number of agents. The scalability of the method to larger multi-agent systems is not fully explored.
- The paper could provide more insight into the shared memory mechanism and how it enables better coordination among agents. A deeper analysis of the memory representations and their relationship to agent behavior would be valuable.

## Questions
- How does SRMT differ from other MARL methods that use communication or centralized training? Could the authors provide a more detailed comparison with methods like DCC, MAMBA, and SCRIMP?
- Can the authors provide more insight into the shared memory mechanism? How does it enable better coordination among agents, and what do the memory representations look like during different phases of the task?
- Have the authors considered evaluating SRMT in more complex environments or with a larger number of agents? How does the method scale with the size of the multi-agent system?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4