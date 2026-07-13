# Review

## Summary
This paper introduces a method to fine-tune reasoning LLMs to reduce the length of the chain-of-thoughts while preserving their accuracy. The method is based on RL, where the reward is a weighted sum of the accuracy and a negative length bonus. The experiments show that the proposed method is effective in reducing the length of the chain-of-thoughts while maintaining the accuracy on math datasets.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.

## Weaknesses
1. The proposed method is not novel. As the authors mentioned, there are existing works using a length penalty in the reward function for RL fine-tuning. The main difference is that the authors use a separate accuracy model to evaluate the response, while the existing works use a contrastive loss. The advantage of the proposed method is that it allows controlling the length and accuracy trade-off by adjusting the weight of the length penalty. However, the authors did not discuss how the accuracy model affects the performance of the proposed method.
2. The experiments are not comprehensive. The authors only evaluate the proposed method on math datasets. It would be better to evaluate the method on other reasoning datasets, such as commonsense reasoning and Big-bench.
3. The proposed method is not well-motivated. The authors aim to reduce the length of the chain-of-thoughts to reduce the inference cost. However, the inference cost is mainly determined by the model size and the input length. Reducing the length of the chain-of-thoughts may not significantly reduce the inference cost, especially for small models like 1.5B and 7B.

## Questions
1. How does the accuracy model affect the performance of the proposed method?
2. Can the proposed method generalize to other reasoning tasks beyond math?
3. How does the proposed method reduce the inference cost?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4