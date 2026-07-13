# Review

## Summary
This paper proposes a new weight regularization method called Soft Weight Rescaling (SWR) to address the plasticity loss problem in neural networks. The method scales down the weight magnitudes close to the initial values by scaling down weights, and can recover plasticity without losing information. The paper provides theoretical analysis and experimental results to demonstrate the effectiveness of SWR.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The proposed method is simple and effective, and can be easily integrated into existing training frameworks.
2. The paper provides theoretical analysis to demonstrate the effectiveness of SWR.
3. The experimental results show that SWR outperforms other regularization methods in warm-start, continual learning, and single-task learning settings.

## Weaknesses
1. The novelty of the proposed method is limited. Weight rescaling has been proposed in previous work [1,2], and the difference between SWR and these methods is not significant. Moreover, the idea of using a constant to scale down the weight is not novel enough.
2. The theoretical analysis is not sufficient. The paper only proves that SWR can bound the weight magnitude, but does not analyze the generalization ability and plasticity of the regularized network.
3. The experimental results are not convincing. The paper only compares SWR with several simple baselines, and lacks comparison with state-of-the-art methods. Moreover, the paper does not provide any ablation studies to analyze the effectiveness of different components of SWR.

[1] Alabdulmohsin I, Maennel H, Keysers D. The impact of reinitialization on generalization in convolutional neural networks[J]. arXiv preprint arXiv:2109.00267, 2021.

[2] Niehaus L, Krumnack U, Heidemann G. Weight rescaling: Applying initialization strategies during training[C]//Workshop on Pre-training and Self-supervision at Scale. 2023.

## Questions
1. What is the difference between SWR and other weight rescaling methods?
2. Can the author provide more theoretical analysis on the generalization ability and plasticity of SWR?
3. Can the author provide more experimental results on different datasets and models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4