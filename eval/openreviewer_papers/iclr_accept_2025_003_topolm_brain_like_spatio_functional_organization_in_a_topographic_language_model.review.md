# Review

## Summary
This paper introduces a novel topographic transformer language model, TopoLM, designed to investigate the spatial-functional organization of language processing in the brain. By incorporating a spatial smoothness loss, the model learns to assemble into clusters that correspond to semantically interpretable groupings of text. Through comprehensive experiments, the authors demonstrate that TopoLM successfully predicts the emergence of a spatially organized cortical language system and aligns well with the empirical organization of functional clusters selective for fine-grained linguistic features in the human cortex.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1.	The paper is well-organized and clearly written, with a logical flow that makes it easy to follow.
2.	The authors conducted extensive experiments, providing a wealth of evidence that demonstrates the effectiveness of the proposed TopoLM.

## Weaknesses
1.	The core idea of this paper—introducing a spatial smoothness loss to promote the formation of topographic organization—is similar to the approach used in [1]. This reduces the novelty of the proposed method.
2.	The authors argue that the spatial smoothness principle is a unifying concept for understanding the functional organization of the cortex. However, they only provide empirical evidence from language and vision tasks, which is insufficient to support this general claim.
3.	While the authors compare TopoLM with a non-topographic baseline model, they do not include a comparison with other topographic language models, such as Topoformer-BERT [2]. Including such comparisons would strengthen the evaluation of TopoLM's performance.
4.	The authors claim that the spatial smoothness principle is a unifying concept for understanding the functional organization of the cortex. However, they only provide empirical evidence from language and vision tasks, which is insufficient to support this general claim.

[1] Margalit, E., Lee, H., Finzi, D., DiCarlo, J. J., Grill-Spector, K., & Yamins, D. L. K. (2024). A unifying framework for functional organization in early and higher ventral visual cortex. Neuron, 112(14), 2435-2451.e7.

[2] BinHuraib, T., Binhuraib, T., Tuckute, G., & Blauch, N. M. (2024). Topoformer: Brain-like topographic organization in transformer language models through spatial querying and reweighting. In ICLR 2024 Re-Align Workshop Paper (Vol. 2024).

## Questions
1.	How does the spatial smoothness principle apply to other cognitive functions, such as emotion or memory? Can TopoLM be extended to model these aspects?
2.	What are the computational costs associated with implementing spatial loss in TopoLM? How does this impact the model's scalability?
3.	Can TopoLM be used to predict the spatial organization of other species, such as non-human primates or even simpler organisms like mice? If so, what adaptations would be necessary?
4.	How does the spatial organization in TopoLM affect its interpretability compared to non-topographic models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4