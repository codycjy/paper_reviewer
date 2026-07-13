# Review

## Summary
This paper investigates whether model-free RL agents can learn to plan by applying concept-based interpretability methods to a model-free agent (DRC) in the Sokoban environment. The authors demonstrate that the DRC agent uses learned concept representations to predict the long-term effects of actions and influence action selection, resembling a planning algorithm. Their methodology involves probing for planning-relevant concepts, investigating plan formation, and verifying the causal effect of plans on the agent's behavior through interventions.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper introduces a novel methodology for investigating planning in model-free RL agents, providing non-behavioral evidence through concept-based interpretability.
- The paper is well-structured and clearly written, with detailed explanations of the methodology and findings.
- The study addresses an important question about the planning capabilities of model-free RL agents, which has implications for the understanding of RL agents' internal mechanisms.

## Weaknesses
- The study is limited to a single agent (DRC) and environment (Sokoban), which may not fully represent the diversity of model-free RL agents and environments. It would be more convincing if the authors could demonstrate the generalizability of their methodology to other agents and environments.
- The paper primarily focuses on the planning capabilities of the agent, but it would be valuable to investigate the relationship between planning and other emergent properties, such as generalization and transfer learning.

## Questions
- How do you ensure that the linear probes are learning the concepts and not just fitting to the data? Have you considered alternative probing methods or baseline comparisons to validate the results?
- The paper mentions that the agent's plans often contain flaws, how do these flaws affect the agent's performance and behavior? Are there any mechanisms in place to detect and correct these flaws?
- The study is limited to a single environment (Sokoban). How do you expect the results to generalize to other environments and agent architectures? Have you considered testing the methodology on other environments or agents?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4