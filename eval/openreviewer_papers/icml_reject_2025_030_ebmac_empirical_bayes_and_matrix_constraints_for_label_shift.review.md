# Review

## Summary
The authors study the problem of estimating the importance weights and their associated confidence set in label shift problems using hierarchical models via the Empirical Bayes and Matrix Constraints (EBMaC) method. Their approach accommodates dispersion beyond what is permitted by the classic multinomial model and produces exact confidence regions in finite samples for confusion matrix and predicted labels. In addition, they describe the dependence structure of the importance weights in matrix constraints. Through a linear programming technique, they are able to compute smaller confidence sets and shorter elementwise confidence intervals for importance weights compared to existing methods, while maintaining the probability guarantee. Applying the results to prediction in the target domain directly yields smaller conformal prediction set and PAC prediction set. Numerical experiments demonstrate the advantages of EBMaC in producing tighter confidence sets for the importance weights both marginally and jointly.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well written and the contributions are clear. The authors study a very important problem in the literature and they improve the state-of-the-art.

## Weaknesses
No theoretical guarantees are provided for the proposed method. The authors should provide finite sample error bounds for their proposed estimators.

## Questions
1. The authors should provide finite sample error bounds for their proposed estimators.
2. The authors should provide a comprehensive comparative study with other existing methods in the literature.
3. The authors should provide extensive simulation studies to showcase the performance of their proposed method.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4