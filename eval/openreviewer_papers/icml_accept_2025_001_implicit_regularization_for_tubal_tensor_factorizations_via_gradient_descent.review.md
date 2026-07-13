# Review

## Summary
This paper studies the implicit regularization of the gradient descent method for low-tubal-rank tensor recovery. Specifically, the authors consider a tensor recovery problem with a linear measurement operator that satisfies the RIP. They show that when the initialization of gradient descent is sufficiently small, the algorithm converges to the ground truth (low-tubal-rank tensor) after a certain number of iterations.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written, and the proof sketch is clear and easy to follow.

2. The implicit regularization of GD for tensor recovery problems is an interesting and important topic.

## Weaknesses
1. My main concern is about the significance of the results. The authors only prove that GD converges to the ground truth when the initialization is small, which is not very interesting. In matrix recovery problems, it is well-known that GD with small initialization behaves similarly to the truncated SVD, which can exactly recover the ground truth. The interesting part is that GD converges to the minimum-norm solution when the initialization is not small, and the implicit regularization of GD can even recover the ground truth when there is a lot of noise. Unfortunately, the current paper does not have any results for large initialization, and it is not clear whether GD can recover the ground truth for noisy tensor recovery problems.

2. The current results seem to be a straightforward extension of [Stoger & Soltanolkotabi, 2021] to the tensor setting. I am curious about the challenges in the analysis that are specific to tensor problems, compared to the matrix case.

3. The paper only considers the tubal rank, which is not very popular in tensor recovery problems. It would be more interesting to consider the general tensor rank.

## Questions
1. Can the authors explain the challenges in the analysis that are specific to tensor problems, compared to the matrix case?

2. Can the authors prove that GD can recover the ground truth for noisy tensor recovery problems, even if the initialization is not small?

3. Can the results be extended to the general tensor rank?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4