# Review

## Summary
The authors show that low-dimensional latent dynamics can generate high-dimensional neural activity. They first show that in a solvable model, low-dimensional pre-activation dynamics can generate high-dimensional post-activation dynamics with a power-law eigenspectrum. They then show that in a more general model, the post-activation eigenspectrum depends on the pre-activation dimension and activation function. They propose a latent variable model, the Neural Cross-Encoder (NCE), that treats neural activity as a linear-nonlinear function of latents and use it to analyze neural data. They show that NCE can identify the pre-activation dimension of simulated data and that the pre-activation dimension is low for grating responses and high for natural image responses.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
The authors present an interesting idea that low-dimensional latent dynamics can generate high-dimensional neural activity. They provide analytical results for a solvable model and numerical results for a more general model. They propose a novel latent variable model, the Neural Cross-Encoder, that treats neural activity as a linear-nonlinear function of latents. They validate NCE on simulated data and demonstrate its application to real neural data, showing that the pre-activation dimension is low for grating responses and high for natural image responses.

## Weaknesses
The authors show that the pre-activation dimension is low for grating responses and high for natural image responses, but do not investigate why this difference exists. It would be interesting to explore the mechanisms that lead to the different pre-activation dimensions for different types of responses.

The authors acknowledge that training NCE can be challenging when neural data is limited and that they were not able to accurately predict neuronal responses to natural images with a low-dimensional NCE model. It would be helpful to provide more details on the challenges encountered during training and to discuss potential solutions to improve the prediction of natural image responses.

## Questions
The authors state that the heavy tail of the post-activation eigenspectrum is not due to noise. It would be helpful to provide more explanation and evidence to support this claim.

The authors note that the duration of imaging experiments is limited and that optimization can get stuck in local minima. It would be helpful to provide more details on the optimization process and to discuss potential strategies for improving the training of NCE.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4