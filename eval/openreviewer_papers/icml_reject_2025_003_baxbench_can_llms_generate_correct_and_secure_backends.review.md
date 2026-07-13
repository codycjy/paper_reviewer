# Review

## Summary
This paper presents BaxBench, a benchmark for evaluating the capabilities of LLMs in generating secure and correct backend code. The benchmark consists of 392 tasks across 28 scenarios, 14 frameworks, and 6 programming languages. The authors evaluate 11 state-of-the-art LLMs on BaxBench and find that even the best models struggle to generate code that is both functionally correct and secure. The paper highlights the need for more challenging coding benchmarks that reflect realistic tasks and emphasizes the importance of security in capability benchmarking.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
1. The paper addresses a critical gap in LLM benchmarking by focusing on the generation of correct and secure backend code, which is essential for real-world software development.
2. BaxBench covers a wide range of scenarios, frameworks, and programming languages, providing a comprehensive evaluation framework.
3. The evaluation of 11 state-of-the-art LLMs on BaxBench provides valuable insights into the current limitations of LLMs in generating secure and correct code.
4. The paper is well-written and easy to follow, with clear explanations of the benchmark construction process, evaluation metrics, and results.

## Weaknesses
1. The paper could benefit from a more detailed analysis of the errors made by LLMs, including the types of mistakes and the complexity of the tasks where failures occur.
2. The paper could provide more insights into the impact of different prompting strategies on the performance of LLMs, including the use of security-specific prompts.
3. The paper could benefit from a more detailed comparison with existing benchmarks, highlighting the novelty and complexity of BaxBench.

## Questions
1. Can you provide more details on the types of errors made by LLMs and the complexity of the tasks where failures occur?
2. How do different prompting strategies, including security-specific prompts, impact the performance of LLMs?
3. Can you provide more insights into the reasons behind the failure of LLMs to generate secure and correct code?
4. How does BaxBench compare to other existing benchmarks in terms of complexity and realism?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4