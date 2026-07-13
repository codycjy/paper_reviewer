# Review

## Summary
This paper proposes two Transformer variants, ResFormer and SVFormer, aimed at addressing the attention concentration problem in deep Transformer models. ResFormer approximates cross-layer attention by adding residual connections from the initial layer values to subsequent layers, while SVFormer further simplifies the architecture by sharing the value embeddings from the first layer across all layers, thereby reducing the KV cache by nearly 50%. The authors conduct experiments on the SlimPajama dataset, comparing these models with vanilla Transformers, DenseFormer, and NeuTRENO.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper introduces a novel approach to mitigating attention concentration by leveraging residual connections, which is a creative extension of existing ideas around cross-layer attention.
2. The paper provides a comprehensive set of experiments on the SlimPajama dataset, demonstrating the effectiveness of ResFormer and SVFormer in both training loss and downstream task performance.
3. SVFormer achieves significant reductions in computational overhead by sharing the initial layer's value embeddings, which is a practical advancement for deploying large-scale models.

## Weaknesses
1. The paper primarily focuses on the attention concentration problem but does not sufficiently explore or compare with alternative explanations and solutions for the over-smoothing effect in Transformers, such as those proposed in [1] and [2].
2. The experiments are limited to a single dataset, which raises concerns about the generalizability of the findings. A broader evaluation on diverse datasets would strengthen the claims.
3. The paper lacks comparisons with a wider range of state-of-the-art models and alternative methods for addressing attention concentration, making it difficult to assess the relative advantages of the proposed methods.
4. The computational efficiency claims would be more convincing with direct measurements of runtime and memory usage, particularly for SVFormer. 
5. The choice of the SlimPajama dataset is not well-justified, and the paper does not discuss potential biases or limitations introduced by this selection.

[1] Wang, Peihao, et al. "Anti-oversmoothing in deep vision transformers via the fourier domain analysis: From theory to practice." ICLR 2022.
[2] Shi, Han, et al. "Revisiting over-smoothing in BERT from the perspective of graph." arXiv preprint arXiv:2202.08625 (2022).

## Questions
1. How does the attention concentration problem relate to other known issues in Transformers, such as over-smoothing and the loss of compositional generalization? Could the proposed methods also address these issues, and if so, how?
2. What is the impact of the proposed methods on the interpretability of attention patterns in Transformer models? Do these methods lead to more focused or more spread-out attention, and why?
3. The paper mentions that SVFormer reduces the KV cache by nearly 50%. How does this reduction in KV cache impact the model's performance on long-range dependencies? Are there trade-offs in accuracy for longer sequences?
4. How does the choice of the SlimPajama dataset affect the generalizability of the findings? Would the results hold on other datasets, particularly those with different characteristics like code or multilingual data?
5. The paper compares ResFormer with vanilla Transformers, DenseFormer, and NeuTRENO. Are there other methods that were considered but not included in the comparisons? How do the proposed methods perform against these excluded alternatives?
6. What are the practical implications of using ResFormer or SVFormer in real-world applications? Are there specific domains where these methods would be particularly beneficial or limited?
7. The paper mentions that ResFormer adds a residual connection between the current layer and the first layer. How does this affect the gradient flow and stability of training? Are there cases where this addition could lead to training instability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4