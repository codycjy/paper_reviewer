# Review

## Summary
The paper proposes a benchmark for evaluating the strategic planning, real-time decision-making, and adaptability capabilities of LLMs using StarCraft II. The paper shows the performance of several LLMs on the benchmark and provides some analysis.

## Soundness
1

## Presentation
2

## Contribution
1

## Strengths
- The paper proposes a new benchmark based on StarCraft II for LLM evaluation.
- The paper evaluates several LLMs on the benchmark and provides some analysis.

## Weaknesses
- The paper does not provide sufficient details about the benchmark, making it difficult to understand how it is constructed and how LLMs are evaluated on it. For example, what are the specific game setups and scenarios used in the benchmark? How are LLMs controlled to make decisions in the game? What is the frequency of LLM inference? How is the LLM decision converted to game actions?
- The paper does not explain how the proposed metrics are computed or why they are designed in such a way. For example, what is the rationale behind the formula of Eq. (2)? Why is the metric defined in such a way? How is the weight of scenario computed? How is the average result across runs computed? What is the normalization process? Similarly for other metrics.
- The paper does not provide sufficient experimental details. For example, what are the hyperparameters for LLM prompting? What are the specific prompts used? How many games are used for evaluation? How are the LLM outputs converted to game actions?
- The paper does not provide a comparison between the proposed benchmark and existing benchmarks, making it difficult to understand the novelty and contribution of the proposed benchmark. For example, what are the differences between the proposed benchmark and existing StarCraft II benchmarks? Why are the proposed metrics better than existing ones?
- The paper does not provide a comparison between the proposed benchmark and real-world scenarios, making it difficult to understand the practical value of the proposed benchmark. For example, how does the proposed benchmark reflect real-world strategic planning and decision-making? How can the evaluation results on the benchmark transfer to real-world applications?
- The paper does not provide a detailed analysis of the results, making it difficult to understand the insights and conclusions. For example, what are the reasons behind the performance differences of LLMs on different metrics? What are the implications of the results on LLM design and development?

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4