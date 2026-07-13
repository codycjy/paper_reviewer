# Review

## Summary
This paper studies online bilevel optimization (OBO), where the lower-level problem is strongly convex and the upper-level problem is nonconvex. The authors propose a new search direction, and develop first-order and zeroth-order algorithms for OBO. The proposed algorithms achieve sublinear stochastic bilevel regret without window smoothing. Numerical results on online parametric loss tuning and black-box adversarial attacks are provided to validate the effectiveness of the proposed algorithms.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. This paper is well-written and easy to follow.

2. The authors provide the first bilevel regret bound without window smoothing.

3. The authors provide the first zeroth-order bilevel optimization algorithm.

## Weaknesses
1. The proposed algorithms require the knowledge of the problem-dependent constants in Assumptions 3.3 and 3.5. In practice, these constants are usually unknown and hard to estimate. 

2. The authors only provide the regret upper bounds for the proposed algorithms, without the corresponding lower bounds. It is hard to tell whether the obtained regret upper bounds are tight or not.

3. The numerical experiments are only conducted on very small datasets, i.e., MNIST. Experiments on larger datasets are needed to validate the effectiveness of the proposed algorithms.

## Questions
1. The authors mention that the proposed algorithms employ ZO-based estimation of Hessians, Jacobians, and gradients. However, it seems that the proposed first-order algorithm still requires the knowledge of the Hessian and Jacobian. Could the authors clarify this?

2. The authors mention that the proposed algorithms achieve sublinear bilevel regret without window smoothing. However, it seems that the regret bound still depends on the path-length $H_{p,T}$ and the function variation $V_T$. When $V_T = o(T)$ and $H_{p,T} = o(T)$, the regret bound becomes $o(T)$, which is the same as the window smoothing case. Could the authors clarify this?

3. The authors mention that the proposed algorithms are more efficient than existing OBO algorithms. However, no numerical results are provided to validate this claim. Could the authors provide some numerical results to support this claim?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4