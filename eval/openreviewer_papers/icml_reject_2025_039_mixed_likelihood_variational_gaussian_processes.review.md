# Review

## Summary
The authors consider the problem of using Gaussian processes to model human preference data, which is non-Gaussian in nature. They propose to use a mixed likelihood approach, where the GP is trained using an ELBO that combines multiple likelihoods. The authors demonstrate the benefits of this approach on a number of real-world problems involving human preference data.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The proposed approach is a natural and flexible way of modelling mixed data types.
- The authors demonstrate the utility of their method on a number of real-world problems.

## Weaknesses
- The authors do not compare against any competing methods. It would be useful to see how the proposed approach compares to alternative methods for modelling human preference data, such as those based on neural networks.
- The proposed approach is only applicable when the different data types have the same underlying latent function. However, in practice, it may be the case that the different data types have different underlying latent functions. It would be useful to discuss this limitation and potential ways to address it.
- The proposed Likert scale likelihood is not very well motivated. It would be useful to provide more details on why this particular likelihood was proposed and how it compares to other likelihood functions for ordinal data.

## Questions
See weaknesses above.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4