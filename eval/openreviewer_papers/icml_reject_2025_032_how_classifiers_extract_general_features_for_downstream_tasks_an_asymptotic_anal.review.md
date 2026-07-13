# Review

## Summary
The authors investigate the conditions for successful feature transfer in classifier-trained networks, focusing on clustering in unseen distributions. They analyze a two-layer nonlinear network trained with a single large gradient descent step on a mean-squared classification loss in the proportional regime. They find that higher similarity between training and unseen distributions improves cohesion and separability, while separability further requires unseen data to be assigned to different training classes. In multiclass classification, the feature extractor maps input points based on their similarity to training classes, and unrelated training classes have a negligible impact on feature extraction. The authors validate their theoretical findings on synthetic datasets and demonstrate practical applicability using ResNet and variations of CAR, CUB, SOP, ISC, and ImageNet datasets.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The authors provide a theoretical analysis of feature transfer in classifier-trained networks, focusing on clustering in unseen distributions. The analysis is rigorous and well-supported.

2. The authors validate their theoretical findings on synthetic datasets, demonstrating the applicability of their analysis in practical scenarios.

3. The paper is well-organized and clearly written, making it easy to follow the authors' arguments and findings.

## Weaknesses
1. The analysis is limited to a two-layer nonlinear network trained with a single large gradient descent step on a mean-squared classification loss in the proportional regime. The authors should discuss the limitations of this setting and how it relates to practical scenarios.

2. The authors should provide more details on the experimental setup, including data preprocessing, model architecture, hyperparameters, and optimization details. This would enhance the reproducibility of the experiments.

3. The authors should discuss the potential impact of their findings on the design and development of neural networks, particularly in the context of transfer learning and open-set clustering.

4. The authors should provide a more detailed comparison with existing methods, discussing the advantages and limitations of their approach compared to other state-of-the-art techniques for feature transfer and clustering.

## Questions
See weakness

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4