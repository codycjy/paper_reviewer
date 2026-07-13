# Review

## Summary
This paper proposes a new notion of sharpness for neural networks, called geodesic sharpness, that takes into account the symmetries of the model. The main idea is to consider the quotient manifold of the parameter space by the group of symmetries and to define sharpness as the maximum change of loss along a geodesic curve on this quotient manifold. The paper shows that this notion of sharpness is invariant to the symmetries of the model and that it correlates with generalization for simple models such as diagonal networks. For more complex models such as transformers, the paper uses an approximation of geodesic sharpness and shows that it also correlates with generalization.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper addresses an important problem in deep learning theory, namely understanding the relationship between sharpness and generalization.
- The proposed notion of geodesic sharpness is novel and principled, based on Riemannian geometry.
- The paper provides a thorough and well-explained development of the theory, including the mathematical concepts and the practical approximation of geodesic sharpness for transformers.
- The experiments on diagonal networks show that geodesic sharpness correlates with generalization, which is a promising result.

## Weaknesses
- The paper does not provide any theoretical guarantees or insights on why geodesic sharpness should correlate with generalization. It would be helpful to have some theoretical support for the proposed notion, even for simple models such as diagonal networks.
- The experiments on transformers show a weaker correlation with generalization compared to the diagonal networks. This raises the question of whether geodesic sharpness is only useful for simple models or if it can also provide insights for more complex models. It would be helpful to have some discussion on this point.
- The paper does not compare geodesic sharpness with other recent notions of sharpness that have been proposed in the literature, such as relative sharpness (Petzka et al., 2021) or adaptive relative sharpness (Adilova et al., 2023). It would be helpful to have some comparison with these notions, at least for simple models such as diagonal networks.

## Questions
- Can you provide any theoretical guarantees or insights on why geodesic sharpness should correlate with generalization?
- Can you comment on the weaker correlation of geodesic sharpness with generalization for transformers compared to diagonal networks? What are the limitations of geodesic sharpness for complex models?
- Can you compare geodesic sharpness with other notions of sharpness in the literature, such as relative sharpness or adaptive relative sharpness, for simple models such as diagonal networks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4