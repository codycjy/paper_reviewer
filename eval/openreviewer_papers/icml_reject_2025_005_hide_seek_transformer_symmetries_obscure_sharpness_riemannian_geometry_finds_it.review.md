# Review

## Summary
This paper introduces a new sharpness measure that accounts for the GL(h) symmetry in attention layers. The authors argue that the previous sharpness measures fail to predict the generalization performance of transformers due to the invariance under the GL(h) symmetry. They propose a sharpness measure based on the notion of the geodesic ball on the symmetry-corrected quotient manifold. Experimental results show that the proposed measure is more predictive of the generalization performance of transformers on image and text classification tasks.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
* The idea of accounting for the GL(h) symmetry in the sharpness measure is novel. The authors provide a principled approach to developing sharpness measures invariant to the GL(h) symmetry.

* The proposed measure shows a stronger correlation with the generalization performance of transformers on image and text classification tasks than previous measures.

## Weaknesses
* The authors argue that the previous sharpness measures fail to predict the generalization performance of transformers due to the invariance under the GL(h) symmetry. However, there is no empirical evidence supporting this claim. It would be more convincing if the authors provided experimental results showing that the previous measures fail to predict the generalization performance of transformers.

* The paper is not self-contained. It relies heavily on the appendix, and many important details are missing from the main text. For example, the derivation of Eq. (8) and the explanation of the experimental setup in Section 5.3 are provided in the appendix rather than in the main text.

* The paper is not well-organized. The main text contains many references to the appendix, making it difficult to follow the flow of the paper. The authors should try to make the paper more self-contained by moving important details from the appendix to the main text.

## Questions
* Can the authors provide experimental results showing that the previous sharpness measures fail to predict the generalization performance of transformers?

* Why is the correlation between the proposed measure and the generalization performance sometimes negative? Is there any intuition behind this?

* What is the computational complexity of the proposed measure? Is it more expensive to compute than the previous measures?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4