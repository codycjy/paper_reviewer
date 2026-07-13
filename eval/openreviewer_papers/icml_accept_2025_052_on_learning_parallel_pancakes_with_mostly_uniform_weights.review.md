# Review

## Summary
The paper studies the problem of learning k-mixtures of Gaussians with a common covariance matrix but unknown mean vectors. The paper focuses on the case where the weights of the mixture components are not exponentially small. It presents two main results: 

1. A Statistical Query (SQ) lower bound showing that distinguishing a k-GMM from a standard Gaussian requires d^{\Omega(log k)} time, even when the weights are uniform. This result establishes that the quasi-polynomial upper bound is close to optimal for this problem. 
2. A quasi-polynomial upper bound for the same problem when most of the weights are uniform while a small fraction of the weights are arbitrary. This result improves the complexity dependence on the minimum weight w_{min} and provides a more nuanced understanding of the complexity landscape based on the weight distribution.

## Soundness
4

## Presentation
3

## Contribution
3

## Strengths
The paper is well written and the results are interesting. The first result gives a tight bound in a special case of the problem and the second result improves the bounds in a different special case.

## Weaknesses
The first result is not completely new, as it is a special case of the more general result from [1]. The second result is new, but it only gives an upper bound for the problem.

[1] Ilias Diakonikolas, Daniel M. Kane, and Andrew Stewart. Statistical query lower bounds for robust estimation of high-dimensional gaussians and gaussian mixtures.

## Questions
In the second result, do you have a lower bound or a conjecture for the sample complexity?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4