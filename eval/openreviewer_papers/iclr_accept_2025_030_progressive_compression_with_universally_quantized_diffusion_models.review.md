# Review

## Summary
The authors propose a new form of diffusion model with uniform noise in the forward process, whose negative ELBO corresponds to the end-to-end compression cost using universal quantization. They obtain promising first results on image compression, achieving competitive rate-distortion and rate-realism results on a wide range of bit-rates with a single model, bringing neural codecs a step closer to practical deployment.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The authors introduce a new form of diffusion model, Universally Quantized Diffusion Model(UQDM), that is suitable for end-to-end learned progressive data compression. Unlike in the closely-related Gaussian diffusion model, compression with UQDM is performed efficiently with universal quantization, avoiding the generally exponential runtime of relative entropy coding.
2. The authors investigate design choices of UQDM, specifying its forward and reverse processes largely by matching the moments of those in Gaussian diffusion, and obtain the best results when we learn the reverse-process variance as inspired by Nichol & Dhariwal (2021).
3. The authors apply UQDM to image compression, and obtain competitive rate-distortion and rate-realism results which exceed existing progressive codecs at a wide range of bit-rates (up to lossless compression), all with a single model. Their results demonstrate, for the first time, the high potential of an unconditional diffusion model as a practical progressive codec.

## Weaknesses
1. In Figure 2, why does the performance of UQDM with fixed reverse variance become worse when T is larger than 5? While the performance of VDM is consistently improving as T increases.
2. In Figure 3, the performance of UQDM is worse than CTC at low bitrates, could the authors explain the reason?

## Questions
Please see the weakness.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4