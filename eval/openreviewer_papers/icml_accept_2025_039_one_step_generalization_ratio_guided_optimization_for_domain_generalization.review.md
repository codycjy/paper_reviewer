# Review

## Summary
This paper proposes a new optimizer to address the problem of domain generalization. The authors leverage the One-Step Generalization Ratio (OSGR) to quantify each parameter's contribution to loss reduction and assess gradient alignment. By dynamically equalizing OSGR via a preconditioning factor, the proposed GENIE prevents a small subset of parameters from dominating optimization, thereby promoting domain invariant feature learning. Theoretically, GENIE balances convergence contribution and gradient alignment among parameters, achieving higher OSGR while retaining SGD's convergence rate. Empirically, it outperforms existing optimizers and enhances performance when integrated with various DG and single-DG methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well written and easy to follow.
2. The proposed GENIE optimizer is novel and interesting.
3. The theoretical analysis is comprehensive and solid.
4. The experimental results are impressive.

## Weaknesses
1. The proposed GENIE optimizer is composed of several techniques, including preconditioning, noise injection, and random mask. It would be better to evaluate the effects of each component separately.
2. The authors claim that the proposed GENIE is a domain-agnostic optimizer. It would be better to explain why it is domain-agnostic and the difference between domain-agnostic and domain-specific optimizers.
3. The proposed GENIE is inspired by previous work (Liu et al., 2020) and (Michalkiewicz et al., 2023). It would be better to compare the proposed GENIE with the optimizers in (Liu et al., 2020) and (Michalkiewicz et al., 2023) in the experiments.

## Questions
Please see Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4