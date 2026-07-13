# Review

## Summary
This paper investigates the context-reliance failure mode of instruction tuning. It finds that the context reliance under knowledge conflicts initially increases as expected, but then gradually decreases as instruction finetuning progresses. The authors conduct controlled studies and theoretical analysis to show that this is due to the presence of non-context-critical datapoints in the instruction tuning datasets. Based on this, the authors propose some mitigation strategies with limited but insightful gains.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper investigates an interesting and important issue of LLMs' context reliance, which is helpful for improving the performance and reliability of LLMs in various applications.
2. The paper conducts comprehensive empirical studies and theoretical analysis to understand the context-reliance failure mode of instruction tuning.
3. The paper proposes some mitigation strategies based on the analysis results, which could be helpful for improving the context reliance of LLMs.

## Weaknesses
1. The mitigation strategies proposed in this paper only bring limited gains, which may limit their practical usefulness.
2. The analysis and mitigation strategies in this paper are mainly focused on knowledge conflicts. It is unclear whether the findings and strategies can be generalized to other context-reliance scenarios.

## Questions
1. The paper uses counterfactual accuracy and parametric accuracy to measure the context reliance of the model. How to calculate these two metrics?
2. The paper uses perplexity to determine whether the data points are context-critical or non-context-critical. How to calculate the perplexity of a data point? Is this method reliable enough to classify the data points?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4