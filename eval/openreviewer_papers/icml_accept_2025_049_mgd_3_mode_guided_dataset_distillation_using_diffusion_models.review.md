# Review

## Summary
This paper proposes a mode-guided diffusion model for dataset distillation, which leverages a pre-trained diffusion model without the need for fine-tuning with distillation losses. The proposed approach addresses dataset diversity in three stages: mode discovery to identify distinct data modes, mode guidance to enhance intra-class diversity, and stop guidance to mitigate artifacts in synthetic samples that affect performance. The experimental results show that the proposed approach outperforms state-of-the-art methods on several datasets.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed approach leverages a pre-trained diffusion model without the need for fine-tuning with distillation losses, which reduces computational costs.
2. The proposed approach addresses dataset diversity in three stages, which enhances the diversity and representativeness of the synthetic samples.
3. The experimental results show that the proposed approach outperforms state-of-the-art methods on several datasets.

## Weaknesses
1. The proposed approach relies on the pre-trained diffusion model, which may limit its applicability to other datasets or tasks.
2. The proposed approach may introduce artifacts in synthetic samples, which can affect the performance of the trained model.

## Questions
1. How does the proposed approach ensure that the synthetic samples are diverse and representative of the original dataset?
2. What are the limitations of the proposed approach, and how can they be overcome in future research?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4