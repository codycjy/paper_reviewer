# Review

## Summary
This paper introduces EMBODIEDBENCH, a benchmark designed to evaluate vision-driven embodied agents. EMBODIEDBENCH features a diverse set of 1,128 testing tasks across four environments, ranging from high-level semantic tasks to low-level tasks involving atomic actions. The benchmark assesses six essential agent capabilities and provides a standardized evaluation platform. The paper evaluates 24 leading proprietary and open-source MLLMs within EMBODIEDBENCH and presents findings on their performance, highlighting existing challenges and offering insights to advance MLLM-based embodied agents.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-structured, with a clear abstract, introduction, methodology, experiments, and conclusion sections that logically flow from one to the next.
2. The figures are clear and easy to understand.
3. The paper introduces a new benchmark for evaluating vision-driven embodied agents, addressing a gap in the current research landscape.

## Weaknesses
1. The main contribution of the paper is the dataset, while the technical contribution is relatively small.
2. The paper does not provide a detailed explanation of the methodology used to collect the dataset, which may limit the reproducibility of the study.
3. The paper does not provide a detailed explanation of the evaluation metrics used, which may limit the reproducibility of the study.
4. The paper does not provide a detailed analysis of the errors made by the MLLMs, which could provide insights for future research.

## Questions
1. How does the performance of the MLLMs vary across different environments and tasks within EMBODIEDBENCH?
2. What are the main challenges faced by MLLMs when performing low-level manipulation tasks?
3. How does the inclusion of visual information affect the performance of the MLLMs in high-level and low-level tasks?
4. Can you provide more details on the data collection process, including how the tasks were designed and how the performance of the MLLMs was evaluated?
5. Can you provide more details on the types of errors made by the MLLMs and how these errors can be addressed in future research?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4