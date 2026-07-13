# Review

## Summary
The paper proposes a hypothesis to explain why inference-time scaling has been shown to improve adversarial robustness in some settings but not in others. Specifically, the hypothesis posits that inference-time scaling can improve robustness, but only when the adversarial examples are sufficiently in-distribution. The paper then tests this hypothesis by attacking models with varying levels of robustness with both white-box and black-box transfer attacks. The paper finds that the hypothesis is correct: inference-time scaling only improves robustness in models that are already robust.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
- The paper is well-written and easy to follow. The figures are also informative and clear.
- The hypothesis is intuitive and makes sense. It is also novel, as far as I know.
- The experiments are clear and convincing. I especially like the ones in Figure 6, which address potential concerns about the hypothesis.

## Weaknesses
- The paper could benefit from more discussion of why the hypothesis makes sense. The paper mentions that when the model is not robust, the adversarial examples are often OOD, and the model is unable to reason its way out of giving the correct answer. This is intuitive, but it would be nice to have more discussion of this point, as it is the crux of the hypothesis.
- The paper could benefit from more discussion of the limitations of the hypothesis. For example, the hypothesis doesn’t explain why inference-time scaling improves robustness even for OOD examples in some settings [1]. It would be good to discuss why the hypothesis doesn’t explain these results, or if the hypothesis can be modified to explain them.

[1] https://arxiv.org/abs/2404.09349

## Questions
- What do you think makes an adversarial example “in-distribution” or “out-of-distribution”? For example, in the setting where inference-time scaling helps, the adversarial examples are often semantically meaningful. But what makes them meaningful? Is it just that they are more in-distribution in the sense that they look like natural images, or is there another reason? This is related to the first weakness I mentioned: I think the paper could benefit from more discussion of why the hypothesis makes sense.
- What do you think explains the results in [1], where inference-time scaling improves robustness even for OOD examples? Is it the case that OOD examples are still somewhat in-distribution in these settings, or is there another reason?

[1] https://arxiv.org/abs/2404.09349

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4