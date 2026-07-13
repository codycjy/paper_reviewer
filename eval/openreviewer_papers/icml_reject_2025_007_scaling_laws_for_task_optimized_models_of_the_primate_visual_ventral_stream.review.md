# Review

## Summary
This paper investigates how scaling model size and training dataset size impact alignment with the primate visual ventral stream. The authors train various models (ResNet, EfficientNet, Vision Transformer, etc.) on ImageNet and EcoSet datasets, evaluating their alignment with brain data using benchmarks from Brain-Score. They find that while behavioral alignment improves with scale, neural alignment saturates. The study reveals that dataset size has a greater impact than model size on improving alignment, especially for higher visual areas. The paper concludes by emphasizing the need for new strategies to enhance neural alignment beyond just scaling.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well-written and easy to follow. The motivation is clear, and the problem addressed is significant. The authors conduct extensive experiments with various models and datasets, providing robust evidence for their findings. The results are clearly presented, with well-designed figures that effectively convey the main takeaways. The authors also make their code and model checkpoints publicly available, promoting reproducibility and future research in this area.

## Weaknesses
The paper primarily focuses on scaling model size and dataset size, which may not be the most effective ways to improve neural alignment. The authors could explore other factors that might influence alignment, such as different training objectives or more biologically plausible architectures.

While the paper includes a diverse set of models, it mainly focuses on a few architectures (ResNet, EfficientNet, ViT). Including a wider range of model types, such as recurrent models or models with more complex inductive biases, could provide a more comprehensive understanding of how different architectures affect alignment.

The paper relies on the Brain-Score benchmarks to evaluate alignment with neural data. While these benchmarks are widely used, they may not be the most comprehensive or up-to-date measures of alignment. The authors could consider other evaluation methods or combine multiple benchmarks to get a more complete picture of model-brain alignment.

The authors could explore how different training objectives, such as self-supervised learning or adversarial training, affect the scaling behavior and alignment with brain data.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4