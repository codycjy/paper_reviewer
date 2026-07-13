# Review

## Summary
The authors propose speculative decoding methods that allow for heterogeneous vocabularies. They propose three methods, one of which is lossless. They evaluate the methods on a number of different models and datasets and show speedups over autoregressive decoding.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The authors tackle an important problem in speculative decoding, namely what to do when the drafter and target model have different vocabularies. They propose three methods to tackle this problem, one of which is lossless.
- The authors evaluate their methods on a large number of models and datasets, showing that the methods are applicable to a wide range of models.
- The authors show speedups over autoregressive decoding for their methods.
- The authors open source their code.

## Weaknesses
- The lossless method (SLEM) requires decoding the tokens back to text. This can be slow and also doesn't work well with non-text datasets (such as math, code, etc).
- The authors only evaluate on a few temperature settings. It would be nice to see how the methods perform at higher temperatures.
- The authors don't evaluate on any out of distribution (OOD) datasets. It would be interesting to see how the methods perform on OOD datasets, as the drafter may not be able to correctly approximate the target model on OOD data.

## Questions
- How do the methods perform at higher temperatures?
- How do the methods perform on OOD datasets?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4