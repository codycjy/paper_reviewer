# Review

## Summary
This paper presents ITBench, a framework for benchmarking AI agents on real-world IT automation tasks across domains like Site Reliability Engineering (SRE), Compliance and Security Operations (CISO), and Financial Operations (FinOps). The initial release includes 102 scenarios with varying complexity levels, along with baseline agents and a comprehensive evaluation framework. The paper reports the performance of several state-of-the-art AI agents on these tasks and provides detailed analyses of their strengths and limitations.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- ITBench addresses a critical need for systematic evaluation of AI agents on real-world IT tasks, providing a robust framework that reflects complex, multi-step decision-making scenarios.
- The paper presents a comprehensive set of 102 scenarios across three key IT domains (SRE, CISO, FinOps), covering a broad range of tasks from incident resolution to compliance assessment and cost management.
- The framework includes a well-structured evaluation methodology with clear metrics and a leaderboard system for comparing agent performance, supporting reproducibility and driving iterative improvements.

## Weaknesses
- While the paper provides a detailed analysis of agent performance, it lacks an in-depth examination of failure modes and the specific challenges AI agents face in each scenario. A more granular error analysis would offer valuable insights for improving agent designs.
- The paper does not thoroughly explore how different environmental factors, such as system observability or the complexity of the underlying infrastructure, affect agent performance. This omission limits understanding of the framework's robustness and generalizability.
- The paper primarily focuses on evaluating state-of-the-art models but does not provide a comparison with human performance on these tasks. Including such a comparison would help establish a baseline for understanding the gap between current AI capabilities and human expertise.

## Questions
- Can you provide more detailed insights into the specific failure modes of the AI agents across different scenarios? How do agents typically perform in the initial stages of an incident, and are there common patterns in the decisions that lead to failure?
- How does the performance of AI agents change when system observability is limited or incomplete? Are there specific metrics that correlate strongly with agent success, particularly in such constrained conditions?
- How do you plan to incorporate human-in-the-loop interactions or feedback into ITBench? Do you envision scenarios where humans work alongside AI agents, and if so, how would this collaboration be structured?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4