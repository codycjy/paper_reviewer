# Review

## Summary
This paper proposes a versatile image restoration and fusion framework that uniformly models diverse degradation types and degrees, using textual and visual prompts as a medium. Specifically, its controllability enables it to respond to user-specific customization needs. A spatial-frequency visual adapter is devised to integrate frequency characteristics and directly extract text-aligned degradation prompts from visual images, enabling automated deployment. A physics-driven imaging model is developed, integrating physical mechanisms such as the Retinex theory and atmospheric scattering principle to bridge the gap between synthetic data and real-world images, while taking into account the degradation simulation of infrared-visible dual modalities.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. This paper proposes a versatile image restoration and fusion framework that uniformly models diverse degradation types and degrees, using textual and visual prompts as a medium.
2. The writing and presentation are clear and easy to understand.

## Weaknesses
1. The comparison methods are limited. Many recent works are not compared, such as [1], [2], and [3]. 
2. The comparison metrics are limited. The authors should provide more metrics, such as MUSIQ and TreS. 
3. The authors should provide some  real-world applications to demonstrate the practicality of the proposed method. 
4. The authors should provide a complexity analysis of the proposed method.

[1] Equivariant Multi-Modality Image Fusion, CVPR2024
[2] DDFM: Denoising Diffusion Model for Multi-Modality Image Fusion, CVPR2023
[3] CDDFuse: Correlation-driven Dual-branch Feature Decomposition for Multi-Modality Image Fusion, CVPR2023

## Questions
See the above weakness.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
5