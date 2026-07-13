# Review

## Summary
This paper introduces LLM-SRBench, a benchmark for evaluating LLMs in scientific equation discovery. It includes 239 challenging problems across four scientific domains, designed to prevent trivial memorization and assess genuine discovery capabilities. The benchmark consists of LSR-Transform, which transforms common physical models into less common mathematical representations, and LSR-Synth, which creates synthetic, discovery-driven problems. Through extensive evaluation, the best-performing system achieves only 31.5% symbolic accuracy, highlighting the challenges of the task and the need for improved methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a comprehensive benchmark that goes beyond simple equation memorization, challenging LLMs to apply scientific knowledge and reasoning skills.
2. The paper conducts extensive experiments with state-of-the-art methods, providing a thorough evaluation of LLMs in scientific equation discovery.
3. The paper is well-structured and clearly presents the benchmark's design, evaluation metrics, and experimental results.

## Weaknesses
1. The paper could benefit from a more detailed comparison with existing benchmarks, highlighting the specific limitations of current benchmarks that LLM-SRBench addresses.
2. While the paper mentions the challenges of the tasks, it could provide more insight into the specific areas where LLMs struggle, such as the complexity of the equations or the need for domain-specific knowledge.
3. The paper could explore the potential biases in the benchmark, such as the distribution of problems across scientific domains or the complexity of the equations, and how they might affect the evaluation of LLMs.

## Questions
1. How does LLM-SRBench compare to existing benchmarks in terms of its ability to prevent memorization and assess genuine scientific discovery?
2. What specific areas do LLMs struggle in within LLM-SRBench, and how do these challenges vary across different scientific domains?
3. Are there any potential biases in the benchmark, and if so, how might they affect the evaluation of LLMs? How does the paper address the variability in the complexity of the equations within the benchmark?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4