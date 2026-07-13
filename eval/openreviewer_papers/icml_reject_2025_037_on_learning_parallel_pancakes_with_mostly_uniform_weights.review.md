# Review

## Summary
This paper studies the problem of learning a $k$-mixture of Gaussians, in the setting where the covariance is known and only the means are unknown. It is known that this problem is hard in general, i.e., the sample complexity is $d^{\Omega(k)}$. However, if the weights of the mixture components are bounded from below, then it is possible to learn the means with a sample complexity of $d^{O(\log k)}$ (Anderson et al., 2024). The main contribution of this paper is to show that this is tight, i.e., a sample complexity of $d^{O(\log(1/w))}$ is not possible in general, by providing a SQ lower bound. The paper also studies a relaxation of this problem, where only a subset of the mixture components have bounded weights. In this case, it is possible to learn the means with a sample complexity that depends on the number of components with bounded weights.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
This paper settles an open question regarding the complexity of learning mixtures of Gaussians with bounded weights. It is well-written and easy to follow.

## Weaknesses
I did not find any major weaknesses.

## Questions
- In the abstract, it is mentioned that the complexity depends on the minimum weight $w_{\min}$, but I could not find this dependence in the upper bound from Theorem 1.4. Can you clarify where the dependence on $w_{\min}$ is?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4