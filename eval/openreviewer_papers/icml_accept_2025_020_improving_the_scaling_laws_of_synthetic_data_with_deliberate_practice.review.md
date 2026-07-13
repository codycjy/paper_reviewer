# Review

## Summary
The authors propose Deliberate Practice for Synthetic Data Generation (DP), a novel framework that improves sample efficiency through dynamic synthetic data generation. The authors theoretically show how training on challenging, informative examples improves scaling laws and empirically validate that DP achieves better scaling performance with significantly fewer training samples and iterations.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed Deliberate Practice (DP) for Synthetic Data Generation framework is novel. Unlike static approaches that generate all synthetic training data upfront, DP incorporates a dynamic loop between a diffusion model and a downstream learner throughout the training.
2. The paper provides a theoretical analysis of the scaling behavior of a simple model trained on selected examples.
3. The paper is well-written and easy to follow.

## Weaknesses
1. The proposed method is only evaluated on the image classification task.
2. The proposed method is only evaluated on the ViT-B architecture.
3. The proposed method is only compared with two baselines.

## Questions
1. Can the proposed method be extended to other tasks, such as object detection and semantic segmentation?
2. Can the proposed method be extended to other architectures, such as ConvNeXt and Swin Transformer?
3. Can the proposed method be compared with more baselines, such as [1] and [2]?

[1] Fake it till you make it: Learning transferable representations from synthetic imagenet clones. In CVPR, 2023.

[2] Scaling laws of synthetic images for model training... for now. In CVPR, 2024.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4