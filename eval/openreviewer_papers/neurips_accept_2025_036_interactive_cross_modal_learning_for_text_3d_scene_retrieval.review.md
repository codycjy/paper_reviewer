# Review

## Summary
This paper proposes an Interactive Text-3D Scene Retrieval Method (IDeal), which promotes the enhancement of the alignment between texts and 3D scenes through continuous interaction. To achieve this, they present an Interactive Retrieval Refinement framework (IRR), which employs a questioner to pose contextually relevant questions to an answerer in successive rounds that either promote detailed probing or encourage exploratory divergence within scenes. Upon the iterative responses received from the answerer, IRR adopts a retriever to perform both feature-level and semantic-level information fusion, facilitating scene-level interaction and understanding for more precise re-rankings. To bridge the domain gap between queries and interactive texts, they propose an Interaction Adaptation Tuning strategy (IAT). IAT mitigates the discriminability and diversity risks among augmented text features that approximate the interaction text domain, achieving contrastive domain adaptation for our retriever.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The idea of the proposed method is interesting and reasonable. 
2. The paper is well-written and easy to understand.
3. The experiments show the effectiveness of the proposed method.

## Weaknesses
1. The paper should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. 
2. Lack of qualitative comparison with other methods.
3. Lack of visualization analysis of the proposed method.

## Questions
1. The authors should provide more details about the LLMs used in the paper, such as the type of LLMs, the training data, the parameters, etc. This would help to better understand the capabilities and limitations of the LLMs and how they affect the performance of the proposed method.
2. The authors should provide more details about the 3D point cloud encoder used in the paper, such as the type of encoder, the training data, the parameters, etc. This would help to better understand the capabilities and limitations of the encoder and how they affect the performance of the proposed method.
3. The authors should provide more details about the text encoder used in the paper, such as the type of encoder, the training data, the parameters, etc. This would help to better understand the capabilities and limitations of the encoder and how they affect the performance of the proposed method.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4