# Review

## Summary
This paper proposes a new GAN inversion method, aiming to improve the editing realism. The proposed method first analyzes the characteristics of GANs, including the local optimum and curvatures within the generating space. Then, it embeds each inverting image into an individual distribution, including semantic editing and non-semantic nuisance noise, to reflect the local curvature. After that, the statistical manifold for the GAN generating space is established based on the Cramer-Rao metric, and the manipulation inversion is optimized on the manifold. Finally, an adversarial strategy is proposed to reduce the searching trials during the optimization procedure.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated, with clear explanations and rationales behind each component.
3. The paper includes comprehensive evaluations and comparisons with state-of-the-art methods, demonstrating the superior performance of the proposed approach.

## Weaknesses
1. In Table 1, the proposed method is compared with several GAN inversion methods, but it lacks a comparison with some recent methods, such as StyleTransformer [1] and StyleRes [2].
2. In Figure 4, the results of manipulation inversion are presented, but there is no comparison with other methods. It would be beneficial to include a comparison with existing methods to better evaluate the proposed approach.
3. In Figure 5, the results of reconstruction are compared with several methods, but the proposed method is not included. It would be helpful to include the results of the proposed method for a comprehensive comparison.

[1] Hu X, Huang Q, Shi Z, et al. Style transformer for image inversion and editing[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022: 11337-11346.

[2] Pehlivan H, Dalva Y, Dundar A. Styleres: Transforming the residuals for real image editing with stylegan[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023: 1828-1837.

## Questions
Please refer to the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4