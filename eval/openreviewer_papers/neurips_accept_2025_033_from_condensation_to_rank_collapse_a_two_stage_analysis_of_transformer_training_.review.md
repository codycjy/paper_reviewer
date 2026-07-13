# Review

## Summary
This paper studies the training dynamics of a one-layer transformer with small initialization. The authors establish a two-stage framework to characterize the training process. In the first stage, the outer parameters of the model exhibit substantial updates, while the query and key matrices remain quasi-static. The authors demonstrate that the outer parameters undergo a condensation process, aligning with a certain direction. In the second stage, the query and key matrices become dynamically activated, leading to a rank collapse of the normalized key-query matrices.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The two-stage training dynamics of the one-layer transformer, as revealed by the authors, are interesting and novel.
3. The theoretical analysis and empirical results presented in this paper are solid.

## Weaknesses
1. The authors focus on the training dynamics of a one-layer transformer, which is relatively simple compared to practical transformers. It would be helpful if the authors could discuss the potential implications of their findings for the training dynamics of multi-layer transformers.
2. The authors do not consider the activation function in their analysis. While they argue that including the activation function does not alter the model's learning dynamics, it would be beneficial to provide empirical evidence to support this claim.
3. The authors' analysis is limited to binary classification tasks. It would be valuable to explore whether the observed dynamics hold for other types of tasks, such as multi-class classification or sequence-to-sequence learning.

## Questions
1. Can the authors discuss the potential implications of their findings for the training dynamics of multi-layer transformers?
2. Can the authors provide empirical evidence to support their claim that including the activation function does not alter the model's learning dynamics?
3. Can the authors' analysis be extended to other types of tasks, such as multi-class classification or sequence-to-sequence learning?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4