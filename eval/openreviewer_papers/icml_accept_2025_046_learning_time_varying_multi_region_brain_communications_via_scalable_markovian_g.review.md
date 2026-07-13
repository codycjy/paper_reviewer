# Review

## Summary
This paper proposes a new method to model the time-varying communication between multiple brain regions. The method leverages Gaussian process factor analysis, which assumes that the latent variables are modeled as a Gaussian process, and the observed data is a linear mixture of the latent variables. The method further connects the Gaussian process with a state-space model and uses an expectation-maximization algorithm for inference. The authors apply the method to two synthetic datasets and one neural dataset.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well written, and the method is well motivated. The authors did a good job in the introduction summarizing the related work and clearly stating their contributions. The method is novel and interesting. The experiment results are convincing.

## Weaknesses
It would be better to include more related models as baselines for comparison. Also, it would be interesting to show some applications of the model, such as decoding the visual stimulus orientation from the learned latent variables.

## Questions
1. Can you include more related models as baselines for comparison?
2. Can you show some applications of the model, such as decoding the visual stimulus orientation from the learned latent variables?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4