# Review

## Summary
The paper proposes a novel approach to de novo peptide sequencing (DNPS) that leverages mass spectrometry data. The authors reformulate DNPS as a mass prediction problem rather than a multiclass classification problem. They introduce an adversarial multi-task learning scheme that combines experimental and simulated spectra to improve generalization to unseen post-translational modifications (PTMs). The model is evaluated on a large dataset of experimental spectra and shows promising results in predicting previously unseen PTMs.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper presents an innovative approach to DNPS by framing it as a mass prediction problem, which allows for the prediction of peptide sequences with unseen PTMs.
2. The authors provide a thorough evaluation of their method on a large dataset of experimental spectra and demonstrate its effectiveness in predicting previously unseen PTMs.
3. The paper is well-written and clearly explains the methodology and results.

## Weaknesses
1. The method's performance is not entirely convincing. The model trained on simulated data fails to generalize well to experimental data, and the multi-task learning model shows only marginal improvements.
2. The paper lacks a comparison with other state-of-the-art DNPS methods, making it difficult to assess the proposed method's relative performance.
3. The paper does not provide a detailed analysis of the model's robustness to noise in the input spectra, which is a common challenge in mass spectrometry data.

## Questions
1. Have you considered comparing your method with other state-of-the-art DNPS methods to provide a more comprehensive evaluation of its performance?
2. How does your method perform on noisy spectra? Have you evaluated its robustness to different levels of noise, and what strategies do you suggest for improving robustness?
3. Could you provide more details on the training process, including the hyperparameters used and the convergence behavior of the model?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4