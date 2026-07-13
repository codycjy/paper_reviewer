# Review

## Summary
This paper investigates the use of sparse autoencoders (SAEs) and transcoders to partially rewrite transformer models in a more interpretable format. The authors propose a method where natural language explanations are generated for SAE latents, which are then used to simulate activations. These simulated activations are patched into the original model's forward pass, allowing for the partial rewriting of transformer layers. The study evaluates the effectiveness of this approach on the Pythia 160M model using SAEs and transcoders trained on different layers.

## Soundness
2

## Presentation
2

## Contribution
1

## Strengths
The paper addresses an important question in the field of mechanistic interpretability: whether transformers can be partially rewritten in a more interpretable format while maintaining model performance. The authors' approach of using natural language explanations to simulate SAE latent activations is novel and offers a new perspective on interpretability.

## Weaknesses
The study's methodology and results raise several concerns. The authors focus on rewriting a single MLP block due to performance degradation when rewriting multiple blocks. This limited scope may impact the generalizability of the findings. Additionally, the performance of the rewritten model is significantly worse than the baseline, which could limit its practical applicability. The authors should consider rewriting only specific parts of the model that are critical for a given task or application, rather than focusing solely on a single block. This approach might help mitigate performance loss while still achieving interpretability benefits.

The authors' approach of using natural language explanations to simulate SAE latent activations is interesting, but it may not be the most effective way to improve interpretability. Recent work has shown that SAEs may not be the best choice for interpretability in transformers, as they can be difficult to train and may not capture meaningful latent structures[1]. Alternative methods, such as linear probing, may offer better interpretability and be easier to implement. The authors should consider comparing their approach to linear probing or other interpretability methods to determine if their method offers any advantages.

The authors should also consider evaluating their approach on larger models (e.g., Llama-3 8B or larger) to determine if the results generalize to more powerful architectures. Additionally, a more comprehensive evaluation of the generated natural language explanations is needed to assess their quality and usefulness. The current evaluation focuses on the downstream performance of the rewritten model, but it does not adequately assess the interpretability of the explanations themselves.

Overall, while the paper addresses an important question in mechanistic interpretability, the limited scope of the study, poor performance of the rewritten model, and lack of comprehensive evaluation of the natural language explanations limit the significance of the findings. The authors should consider rewriting only specific parts of the model for critical tasks, comparing their approach to linear probing, and evaluating the quality of the natural language explanations in greater detail to improve the impact of their work.

[1] Zhang, Richard, et al. "SAE does not scale: A case study on the limitations of sparse autoencoders for interpretability." arXiv preprint arXiv:2409.17262 (2024).

## Questions
- Have you considered rewriting only specific parts of the model that are critical for a given task or application, rather than focusing solely on a single block? How do you think this approach would impact the performance of the rewritten model and its usefulness for interpretability?
- How do you think your approach compares to linear probing or other interpretability methods in terms of effectiveness and ease of implementation? Have you considered comparing your method to these alternatives to determine if it offers any advantages?
- How do you assess the quality and usefulness of the natural language explanations generated for the SAE latents? Have you conducted any evaluations beyond the downstream performance of the rewritten model to determine if the explanations are meaningful and useful for interpretability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4