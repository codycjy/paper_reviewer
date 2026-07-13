# Review

## Summary
This paper studies the identifiability of self-supervised learning (SSL) and supervised learning (SL) with cross-entropy loss. It shows that SSL and SL can recover the ground truth factors of variation up to linear transformations. The paper first shows that the parametric instance discrimination (PID) method of Ibrahim et al. (2024) can identify the ground truth factors of variation up to linear transformations. Then, the paper shows that standard cross-entropy based supervised classification can also identify the ground truth factors of variation up to linear transformations.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper is well-written and easy to follow.
- The theoretical analysis is rigorous.

## Weaknesses
- The theoretical result of the paper is not surprising. Ibrahim et al. (2024) has already shown that PID can identify the ground truth factors of variation. It is obvious that if PID can identify the ground truth factors of variation, then standard cross-entropy based supervised classification can also identify the ground truth factors of variation up to linear transformations. Therefore, the contribution of the paper is limited.
- The paper does not provide any insights on how to improve the performance of SSL and SL.

## Questions
- Can the theoretical results of the paper guide the development of new SSL and SL methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4