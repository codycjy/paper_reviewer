# Review

## Summary
This paper investigates the potential of large language models (LLMs) to emulate both fast, intuitive reasoning (System 1) and slow, analytical reasoning (System 2), inspired by dual-process theories of human cognition. The authors create a dataset of 2,000 reasoning tasks with responses representing both System 1 and System 2 thinking. Using preference-based training methods (DPO and SimPO), they align LLMs with either System 1 or System 2 responses and evaluate these models on a range of reasoning benchmarks. The results show that System 2 models excel in arithmetic and symbolic reasoning, while System 1 models perform better in commonsense reasoning tasks. The paper also explores the accuracy-efficiency trade-off and finds that System 2 models, while more uncertain, are better suited for structured, multi-step reasoning, whereas System 1 models provide faster, more confident responses for intuitive scenarios. The study concludes by highlighting the potential of LLMs to adapt their reasoning strategies like humans, offering insights into more flexible and efficient AI systems.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces an innovative approach to aligning LLMs with different cognitive reasoning modes (System 1 and System 2), drawing inspiration from dual-process theories in cognitive science. This perspective on reasoning is novel in the context of LLMs and offers a new framework for understanding model behavior.

2. The authors create a dataset of 2,000 reasoning tasks with responses representing both fast, intuitive (System 1) and slow, deliberate (System 2) thinking. This dataset is a valuable contribution and provides a solid foundation for future research on dual-process reasoning in LLMs.

3. The paper provides a comprehensive evaluation of the aligned LLMs across 13 reasoning benchmarks covering arithmetic, commonsense, and symbolic reasoning. This broad evaluation framework allows for a detailed comparison of System 1 and System 2 models and provides insights into their respective strengths and weaknesses.

4. The study reveals an accuracy-efficiency trade-off between System 1 and System 2 models, demonstrating that different reasoning paradigms excel at different types of tasks. This finding is significant as it challenges the assumption that step-by-step reasoning is always optimal and highlights the need for adapting reasoning strategies based on task demands.

## Weaknesses
1. The study primarily focuses on two specific LLMs (Llama-3-8B-Instruct and Mistral-7B-Instruct-v0.1). This limited selection may restrict the generalizability of the findings. It would be valuable to explore whether the observed effects are consistent across a broader range of LLM architectures and sizes.

2. The paper utilizes preference-based training methods (DPO and SimPO) to align LLMs with System 1 and System 2 responses. However, there is limited discussion on the potential limitations and pitfalls of these methods. A more in-depth exploration of the implications of using these training approaches could provide a more balanced perspective.

3. The evaluation focuses on reasoning benchmarks that are largely static and may not fully capture the complexity of real-world decision-making scenarios. Incorporating more dynamic and interactive evaluation methods could provide a more comprehensive assessment of the models' reasoning capabilities.

## Questions
1. Could you elaborate on the potential limitations of using DPO and SimPO for aligning LLMs with System 1 and System 2 responses? Are there specific scenarios where these methods might fail to capture the nuances of the respective reasoning modes?

2. How do you envision the findings of this study being applied in real-world AI systems? Are there specific domains where the trade-off between System 1 and System 2 reasoning is particularly relevant?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4