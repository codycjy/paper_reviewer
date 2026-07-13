# Review

## Summary
The paper introduces LLM-SRBench, a benchmark for evaluating Large Language Models (LLMs) in scientific equation discovery. It includes 239 challenging problems across four scientific domains, designed to prevent trivial memorization and assess genuine discovery capabilities. The benchmark consists of two categories: LSR-Transform, which transforms common physical models into less common mathematical representations, and LSR-Synth, which creates synthetic, discovery-driven problems. Through extensive evaluation of several state-of-the-art methods using both open and closed LLMs, the authors find that the best-performing system achieves only 31.5% symbolic accuracy, highlighting the challenges of the tasks and the potential value of LLM-SRBench for future research.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper introduces a new benchmark, LLM-SRBench, which is designed to evaluate LLMs in scientific equation discovery, addressing the limitations of existing benchmarks that are prone to memorization.
2. The paper proposes a novel benchmark design using alternative mathematical representations (LSR-Transform) and synthetic, discovery-driven problems (LSR-Synth) to ensure rigorous evaluation of scientific reasoning and discovery capabilities beyond simple memorization.
3. The paper presents extensive experiments on state-of-the-art methods, revealing performance peaks at approximately 31%, which demonstrates the benchmark's challenging nature and its potential for future research in scientific equation discovery.

## Weaknesses
1. The benchmark is limited to 239 problems, which is a relatively small size compared to other benchmarks in the field. This limited size may not provide a comprehensive evaluation of LLMs' capabilities in scientific equation discovery.
2. The paper does not provide a detailed analysis of the types of errors made by the LLMs. Understanding the specific errors and patterns in LLMs' predictions is crucial for identifying areas for improvement and developing more effective models.

## Questions
1. How does the performance of LLMs in scientific equation discovery change as the complexity of the equations increases? Are there specific complexities beyond which LLMs struggle to make accurate predictions?
2. Can the results from LLM-SRBench be generalized to other scientific domains or real-world applications beyond the four domains covered in the benchmark? How might the performance of LLMs vary in different contexts?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4