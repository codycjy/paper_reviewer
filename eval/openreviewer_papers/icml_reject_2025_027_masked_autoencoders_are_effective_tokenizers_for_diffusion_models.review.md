# Review

## Summary
This paper presents a theoretical and empirical analysis of latent space properties for diffusion models, demonstrating that fewer modes in latent distributions enable more effective learning and better generation quality. Based on these insights, the authors developed MAETok, which achieves state-of-the-art performance through mask modeling without requiring variational constraints. Using only 128 tokens, this approach significantly improves both computational efficiency and generation quality on ImageNet.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the relationship between the number of GMM modes and diffusion loss, which is interesting.
3. The authors demonstrate that the proposed MAETok can achieve good reconstruction and generation performance.

## Weaknesses
1. The authors should compare the proposed method with more baseline methods, such as MAR[1] and MAGVIT[2].
2. The authors should compare the inference efficiency of the proposed method with other methods.
3. The authors should compare the proposed method with other methods on text-to-image tasks.
4. The authors should provide some visualization examples of the proposed method.

[1] Li T, Chang H, Mishra S K, et al. Mage: Masked generative encoder to unify representation learning and image synthesis[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2023: 11977-11987.
[2] Yu L, Lezama J, Gundavarapu N B, et al. Language model beats diffusion - tokenizer is key to visual generation[C]//The Twelfth International Conference on Learning Representations. 2024.

## Questions
Please see the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4