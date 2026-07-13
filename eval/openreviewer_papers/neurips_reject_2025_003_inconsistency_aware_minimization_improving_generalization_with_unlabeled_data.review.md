# Review

## Summary
The paper proposes a new measure of sharpness called local inconsistency, which is defined as the maximum KL divergence of the model outputs with respect to all perturbations within a L2 ball of radius rho around the parameters. The paper shows that this measure is closely related to the maximum eigenvalue of the Fisher information matrix and is also related to the inconsistency measure proposed by Johnson and Zhang. The paper then proposes two algorithms for minimizing local inconsistency: one direct and one similar to SAM. The paper shows that the proposed algorithms can improve generalization in both supervised and unsupervised settings.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The proposed measure of local inconsistency is novel and has several desirable properties: it is label-free, computable from a single model, and is related to the inconsistency measure proposed by Johnson and Zhang.
- The paper provides a theoretical analysis of the relationship between local inconsistency and the Fisher information matrix, as well as its relationship to the inconsistency measure proposed by Johnson and Zhang.
- The proposed algorithms for minimizing local inconsistency are simple and intuitive. The paper shows that they can improve generalization in both supervised and unsupervised settings.

## Weaknesses
- The paper does not provide a rigorous theoretical analysis of the generalization benefits of minimizing local inconsistency. The informal theorem presented in the paper relies on several assumptions and heuristic steps, and it is unclear how tight the resulting bound is.
- The paper does not provide a comprehensive comparison with existing sharpness-aware algorithms. The paper only compares with SAM and ASAM, but there are many other sharpness-aware algorithms that outperform SAM, such as SWA [1], SGA [2], and GSM [3]. It would be beneficial to compare with these algorithms and discuss their relationship with local inconsistency.

[1] Foret et al. "Sharpness-aware minimization for efficiently improving generalization." ICLR 2021.

[2] Zhuang et al. "Surrogate gap minimization improves sharpness-aware training." NeurIPS 2022.

[3] Zhang et al. "Gsm: A generalized sharpness-aware minimization framework for improving generalization." NeurIPS 2022.

## Questions
- Can you provide a more rigorous theoretical analysis of the generalization benefits of minimizing local inconsistency? For example, can you provide a tight bound on the generalization gap in terms of local inconsistency, or prove that minimizing local inconsistency improves the PAC-Bayes bound?
- Can you provide a comprehensive comparison with existing sharpness-aware algorithms, such as SWA, SGA, and GSM? How do these algorithms relate to local inconsistency, and can you provide a comparison of their empirical performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4