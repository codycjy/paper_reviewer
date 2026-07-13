# Review

## Summary
The paper introduces CONCEPTATTENTION, a novel method that leverages the expressive power of multi-modal diffusion transformers (DiTs) to generate high-quality saliency maps that precisely locate textual concepts within images. The method repurposes the parameters of DiT attention layers to produce contextualized concept embeddings without requiring additional training. The key discovery is that performing linear projections in the output space of DiT attention layers yields significantly sharper saliency maps compared to commonly used cross-attention maps.

## Soundness
2

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel method, CONCEPTATTENTION, that leverages the expressive power of multi-modal diffusion transformers (DiTs) to generate high-quality saliency maps that precisely locate textual concepts within images. This approach is innovative as it repurposes the parameters of DiT attention layers to produce contextualized concept embeddings without requiring additional training.
2. The paper is well-written and structured, making it easy to follow the authors' arguments and methodologies. The use of figures and tables to illustrate key points is effective and enhances the clarity of the paper.
3. The paper addresses an important problem in the field of interpretability of generative models.

## Weaknesses
1. The paper does not provide a detailed comparison with other state-of-the-art methods for interpretability of generative models.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method.

## Questions
1. How does CONCEPTATTENTION compare to other state-of-the-art methods for interpretability of generative models? Please provide a detailed comparison.
2. What are the limitations of CONCEPTATTENTION? Please provide a detailed analysis of the computational complexity of the proposed method.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4