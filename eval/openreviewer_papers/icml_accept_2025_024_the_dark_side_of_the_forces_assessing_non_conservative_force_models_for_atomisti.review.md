# Review

## Summary
The paper investigates the use of non-conservative force models in atomistic machine learning for predicting interatomic forces and energies. The authors compare conservative and non-conservative models, identifying significant issues with non-conservative models, such as poor convergence in geometry optimization and instability in molecular dynamics simulations. They propose a hybrid approach that combines conservative and non-conservative models, suggesting that direct force prediction can be useful for accelerating simulations while maintaining energy conservation. The study emphasizes the importance of energy conservation in interatomic modeling and provides insights into the development of more robust and accurate force fields.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a detailed analysis of the differences between conservative and non-conservative force models, highlighting the theoretical and practical implications of each approach.
2. The authors conduct a range of experiments, including molecular dynamics simulations and geometry optimizations, to validate their findings and demonstrate the performance of the proposed hybrid model.

## Weaknesses
1. The paper primarily focuses on liquid water as a case study. While this provides a detailed view of the model's performance in one context, it may limit the generalizability of the findings to other materials and systems.
2. The proposed hybrid model that combines conservative and non-conservative forces is not new, and the paper does not thoroughly compare its performance with existing hybrid models or other state-of-the-art methods in the field.

## Questions
1. How does the proposed hybrid model compare with other hybrid models or conservative models in terms of accuracy and computational efficiency?
2. Are there specific types of materials or molecular systems where non-conservative models perform particularly poorly or well? How do these vary from the case study presented?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4