# Review

## Summary
The paper studies the grokking phenomenon in the context of non-neural models, specifically recursive feature machines. They show that these models also exhibit grokking when trained on modular arithmetic tasks, and that the features learned by these models are block circulant. They also show that neural networks learn similar features and that random block circulant features are sufficient to learn modular arithmetic.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
The paper is well-written and easy to follow. The experiments are clearly presented and the findings are interesting. The paper provides evidence that the features learned by RFMs and neural networks are similar, and that random block circulant features are sufficient to learn modular arithmetic, which is a valuable contribution to the understanding of the grokking phenomenon.

## Weaknesses
The paper could benefit from a more detailed discussion of the implications of their findings for our understanding of the grokking phenomenon and feature learning in general. The paper shows that RFMs learn block-circulant features, but does not provide a clear explanation of why these features are learned or how they contribute to generalization. The authors could provide a more detailed analysis of the learned features, such as analyzing the eigenvalues of the feature matrices or examining the alignment of the learned features with the AGOP of the ground truth model.

## Questions
- The paper shows that RFMs learn block-circulant features, but does not provide a clear explanation of why these features are learned or how they contribute to generalization. Can the authors provide a more detailed analysis of the learned features, such as analyzing the eigenvalues of the feature matrices or examining the alignment of the learned features with the AGOP of the ground truth model?
- The paper shows that random block-circulant features are sufficient to learn modular arithmetic, but does not provide a clear explanation of why these features are effective or how they compare to the features learned by RFMs. Can the authors provide a more detailed comparison of the features learned by RFMs and random block-circulant features, and explain why the latter are sufficient to learn modular arithmetic?
- The paper could benefit from a more detailed discussion of the implications of their findings for our understanding of the grokking phenomenon and feature learning in general. Can the authors provide a more detailed discussion of the implications of their findings for our understanding of feature learning and the grokking phenomenon, and how their results might lead to new insights or improvements in the design of machine learning models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4