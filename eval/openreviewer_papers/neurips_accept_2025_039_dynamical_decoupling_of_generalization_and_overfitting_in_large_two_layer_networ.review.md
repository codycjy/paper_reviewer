# Review

## Summary
The authors study the training dynamics of a two-layer neural network in the mean-field regime. They characterize the different phases that the training goes through, in particular the separation between feature learning and overfitting. Their main tool is dynamical mean field theory, which they adapt to the setting of two-layer networks trained on Gaussian data. They also provide some rigorous results on the training dynamics.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well written and easy to follow. The authors do a good job at introducing the necessary background and explaining the results.
- The results are interesting and shed light on the training dynamics of neural networks in the mean-field regime. The separation between feature learning and overfitting is well explained and supported by numerical simulations.
- The paper contains some rigorous results that support the claims made in the paper.

## Weaknesses
- The numerical simulations are only shown for the case of lazy initializations. It would be interesting to see how the training dynamics behaves for small initializations.
- The theoretical results are not entirely satisfactory. Theorem 1 only gives a upper bound on the generalization error that is vacuous in the regime of interest. Theorem 2 shows that the mean-field equations are a good description of the training dynamics, but it does not say anything about the generalization error.

## Questions
- Can you provide more details about the simulations shown in Figure 3? In particular, how do the weights behave in each of the three regimes?
- Can you provide a more detailed comparison between the mean-field equations (2.10) and the full dynamics (1.2)? In particular, how do they differ and how does this impact the generalization error?
- Can you provide a more detailed discussion of the limitations of the theoretical results? In particular, how do the assumptions of Theorem 2 limit its applicability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4