# Review

## Summary
This paper investigates the use of large language models (LLMs) as judges to evaluate other models' performance, with a focus on debiasing methods to mitigate the biases introduced by LLM judges. The authors show that when the judge model performs worse than the evaluated model, even the best debiasing methods offer no advantage over simply using twice the ground truth data. This finding suggests that the LLM-as-a-judge paradigm has significant limitations when applied to evaluate state-of-the-art models. The paper provides both theoretical analysis and empirical evidence to support its claims, highlighting the need for more robust evaluation methods at the evaluation frontier.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a rigorous theoretical analysis of the limitations of using LLMs as judges when the evaluated model outperforms the judge. It presents clear mathematical formulations and proofs, demonstrating that the best debiasing methods are no better than using twice the ground truth data when the judge model is less accurate than the evaluated model.
2. The paper offers empirical evaluations on popular benchmarks like MMLU and MT-Bench, validating its theoretical findings. The experiments show that in practice, the sample size savings achievable with debiasing methods are much more modest than the theoretical limits suggested, further emphasizing the practical limitations of the LLM-as-a-judge paradigm at the evaluation frontier.
3. The paper is well-written and easy to follow.

## Weaknesses
1. The paper does not consider more sophisticated sampling strategies, such as stratified PPI, which might offer better sample efficiency. It would be interesting to see how these advanced methods perform in comparison to the simple doubling of ground truth data.
2. The paper focuses on tasks where performing and judging the task are of similar difficulty. It would be valuable to explore tasks where evaluation is substantially easier than the task itself or where data for training a specialized evaluator is abundant. This could provide insights into scenarios where sample efficiency gains of more than a factor of two might be possible.

## Questions
See weakness

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4