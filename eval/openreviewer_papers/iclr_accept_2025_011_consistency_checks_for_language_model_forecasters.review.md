# Review

## Summary
This paper focuses on the evaluation of LLM-based forecasters, given that ground truth is only known in the future. Following the consistency check framework, the authors propose a new, general consistency metric based on arbitrage. They build an automated evaluation system that generates a set of base questions, instantiates consistency checks from these questions, elicits the predictions of the forecaster, and measures the consistency of the predictions. They then build a standard, proper-scoring-rule forecasting benchmark, and show that the consistency metrics correlate with LLM forecasters’ ground truth Brier scores. They also release a consistency benchmark that resolves in 2028, providing a long-term evaluation tool for forecasting.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. This paper focuses on the evaluation of LLM-based forecasters, which is an important and interesting topic.
2. The paper is well-written and easy to follow.
3. The authors conduct experiments with various LLM models.

## Weaknesses
1. The novelty of the paper is limited. The concept of consistency checks was first introduced in [1], and the authors of this paper simply extend the consistency checks to LLM-based forecasters.
2. The paper does not provide any new insights or conclusions. The main conclusion, "consistency metrics correlate with LLM forecasters’ ground truth Brier scores", is obvious and has been reflected in previous works [1].
3. The authors do not provide the reasons why the proposed consistency metrics are better than the metrics in [1]. In fact, the metrics in [1] are more intuitive.
4. The paper is not well-motivated. The authors claim that the ground truth of some events will not be available for a long time, so it is necessary to evaluate the LLM forecasters' performance instantly. However, the authors do not explain why the proposed metrics can evaluate the LLM forecasters' performance well.

[1] Lukas Fluri, Daniel Paleka, and Florian Tramèr. Evaluating superhuman models with consistency checks. In 2024 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML), volume 31, page 194–232. IEEE, April 2023.

## Questions
1. What is the meaning of the x-axis in Figure 2?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4