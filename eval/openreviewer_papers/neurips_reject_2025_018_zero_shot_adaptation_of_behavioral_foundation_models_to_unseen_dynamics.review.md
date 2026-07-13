# Review

## Summary
The paper proposes a method for improving the generalisation of Forward-Backward (FB) style behavioural foundation models. The core idea is to introduce a context variable, which is inferred from transitions, that is used to condition the successor measure. The context variable is inferred using a transformer encoder. The paper also proposes to use a von Mises-Fisher prior over the FB task vectors to encourage them to be better separated in the space. The paper provides theoretical analysis of the regret under multiple dynamics and with latent space partitioning. The proposed method is evaluated on two discrete and one continuous environment, showing improved generalisation to unseen contexts.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a good analysis of why FB representations cannot distinguish between distinct dynamics.
- The proposed method is interesting and appears to be novel.
- The paper is well written and easy to follow.
- The paper provides theoretical analysis of the regret under multiple dynamics and with latent space partitioning.
- The empirical evaluation shows good performance.

## Weaknesses
- The paper could evaluate on more complex environments. The current environments are quite simple and small in scale. The paper could evaluate on more complex grid-world environments or even continuous control environments with varying dynamics.
- The paper could evaluate on more environments with varying dynamics. The current environments only have a limited number of different dynamics.
- The paper could provide ablations for the impact of the context length on the performance.
- The paper could provide more details on how the regret bound is affected by the proposed method.
- The paper does not discuss limitations of the proposed method.

## Questions
- How does the proposed method scale with the complexity of the environment?
- How does the proposed method scale with the number of different dynamics in the training environments?
- What is the impact of the context length on the performance?
- How is the regret affected by the proposed method?
- What are the limitations of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4