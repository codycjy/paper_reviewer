# Review

## Summary
The paper studies online calibration of multi-dimensional predictions. The paper shows that the previous algorithm of Pen25 can be interpreted as a swap regret minimization algorithm. This new interpretation allows the algorithm to be applied to a more general setting where the predictions and outcomes belong to an arbitrary convex set and the distance metric is an arbitrary norm. The paper also proves a lower bound showing that the number of rounds must grow exponentially with the dimension for this problem.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The paper is well written and easy to follow.
- The connection between TreeCal and TreeSwap is novel and interesting, and it allows for a simpler analysis of TreeCal. 
- The paper provides a nice overview of the related work on calibration.
- The paper provides a nice overview of the TreeCal and TreeSwap algorithms, and the visualization in Figure 1 is very helpful.

## Weaknesses
- The main contribution of the paper is a new analysis of a known algorithm (TreeCal). While this analysis is novel and provides new insights, it is not clear if this is a significant enough contribution for a conference paper.

## Questions
- Is it possible to obtain better bounds by analyzing TreeSwap with Follow-The-Leader instead of Be-The-Leader? What would be the challenge in this analysis?
- The lower bound in Theorem 4.1 is for linear losses, while the upper bound in Theorem 3.1 is for arbitrary convex losses. Is this a significant gap, or can the lower bound be extended to arbitrary convex losses?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4