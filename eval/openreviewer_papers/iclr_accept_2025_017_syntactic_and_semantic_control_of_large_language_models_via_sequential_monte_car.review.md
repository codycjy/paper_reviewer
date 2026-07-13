# Review

## Summary
The paper proposes an SMC algorithm to sample from the product of experts distribution between the language model and the potential function. The authors conduct extensive experiments on various tasks to demonstrate the effectiveness of the proposed method. The authors also show that the proposed method outperforms other methods in terms of approximating the target distribution.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
- The proposed method is novel and general, which could be applied to various tasks and language models.
- The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method.
- The paper is well-written and easy to follow.

## Weaknesses
- The paper does not report the running time of the proposed method and other baselines. It would be helpful to report the running time, especially the additional time required by the expensive potential functions.
- It would be better to report the performance of the proposed method with a larger number of particles, e.g., 50.

## Questions
- Why do you use Llama 3.1 (8B) for the goal inference task and Llama 3.1 (70B) for the data science task? It would be better to use the same language model for a fair comparison.
- In Table 2, Full IS achieves the best performance on the molecular synthesis task. However, in Table 4, Grammar-only SMC achieves the best performance. Do you have any intuition about this?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4