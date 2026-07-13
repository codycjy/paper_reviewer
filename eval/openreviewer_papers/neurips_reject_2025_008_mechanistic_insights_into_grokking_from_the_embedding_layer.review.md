# Review

## Summary
This paper studies the grokking behavior of neural networks, particularly focusing on the role of embedding layers in modular arithmetic tasks. The authors find that the presence of embedding layers is crucial for the emergence of the grokking phenomenon. They identify two key mechanisms: (1) embedding update dynamics, where rare tokens stagnate due to sparse gradient updates and weight decay, and (2) bilinear coupling, where the interaction between embeddings and downstream weights introduces saddle points and increases sensitivity to initialization. To address these issues, the paper proposes strategies such as frequency-aware sampling and embedding-specific learning rates. The findings are supported by theoretical analysis and experiments.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a novel perspective on the role of embedding layers in grokking, which has not been explored in depth before. This contributes to the understanding of this phenomenon.

- The authors identify and analyze two key mechanisms that contribute to grokking, providing insights into the underlying optimization dynamics.

- The paper proposes practical strategies to mitigate the identified issues and accelerate convergence. These strategies are shown to be effective in the experiments.

- The findings have broader implications for Transformer optimization, where similar challenges arise due to the bilinear nature of attention mechanisms.

## Weaknesses
- The theoretical analysis and proposed strategies are specifically tailored to the modular arithmetic tasks considered in the paper. It is not clear how well these insights would generalize to more complex tasks, such as language modeling or image classification.

- The paper focuses on MLP architectures for simplicity. While this allows for controlled analysis, it is unclear how these findings would translate to more complex architectures like Transformers.

- The proposed strategies, such as frequency-aware sampling and embedding-specific learning rates, may add complexity to the training process. It is not clear how practical these strategies are for large-scale applications.

## Questions
- How well do the theoretical insights and proposed strategies generalize to more complex tasks beyond modular arithmetic? Can the authors provide evidence or examples to support this?

- The paper focuses on MLPs for simplicity. How well do the findings translate to more complex architectures like Transformers? Are there any key differences or limitations to consider?

- The proposed strategies may add complexity to the training process. Can the authors provide a more detailed analysis of the computational overhead and practical implications of these strategies?

- The paper compares different sampling strategies (uniform, skewed, random). How sensitive are the results to the choice of sampling strategy in practice?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4