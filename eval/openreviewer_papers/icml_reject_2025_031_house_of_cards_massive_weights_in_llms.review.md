# Review

## Summary
This paper explores the massive weights in LLMs and their impact on model performance. The authors find that a small number of massive weights in the feed-forward network of early layers have a significant impact on model performance. They propose a method called MacDrop, which applies dropout to these massive weights during fine-tuning to reduce their influence and improve model robustness.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The authors conduct extensive experiments to validate their observations and the effectiveness of MacDrop.

## Weaknesses
- The authors do not provide a detailed analysis of why massive weights emerge during pretraining and why they have such a significant impact on model performance.
- The proposed MacDrop method adds additional computational overhead during fine-tuning, which may limit its practical application.

## Questions
- Could the authors provide more insights into the underlying mechanisms that lead to the formation of massive weights during pretraining?
- How does the performance of MacDrop vary with different choices of k and p0?
- How does MacDrop affect the convergence rate of fine-tuning? Is there a significant difference in performance between early stopping and converging at a high dropout probability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4