# Review

## Summary
This paper studies the effect of large batch training on the optimization and generalization of language model pre-training. The authors find that training with large batch sizes can substantially outperform small-batch training, provided that sufficient training tokens are used. However, this advantage is often overlooked because of poor optimization dynamics during the early warm-up phase. To address this issue, the authors introduce a simple batch size scheduler that stabilizes and improves training at remarkably large batch sizes.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is clearly written and easy to follow.
2. The paper studies an important problem in large-scale language model training: large batch training.
3. The paper includes comprehensive experimental results on gradient dynamics and optimization geometry.

## Weaknesses
1. The paper only considers linear batch size schedulers, which may limit the generality of the findings.
2. The paper does not provide any theoretical analysis of the optimization dynamics or gradient geometry under different batch sizes.
3. The paper does not compare the proposed batch size scheduler with other common methods, such as the cosine scheduler or the trapezoidal rule scheduler.

## Questions
1. How does the proposed batch size scheduler compare with other common schedulers, such as the cosine scheduler or the trapezoidal rule scheduler?
2. Is there any theoretical justification for the observed gradient stabilization under large batch sizes?
3. How does the batch size affect the model's generalization ability, and is there a clear relationship between batch size and generalization error?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4