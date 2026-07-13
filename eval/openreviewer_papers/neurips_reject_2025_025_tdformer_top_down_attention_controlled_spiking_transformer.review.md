# Review

## Summary
This paper proposes TDFormer, a top-down controlled spiking transformer. The authors introduce a top-down feedback mechanism to improve the temporal information utilization in SNNs. The model achieves state-of-the-art performance on ImageNet with an accuracy of 86.83%.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a top-down feedback structure in SNNs, which is a novel approach inspired by biological mechanisms.
2. The paper provides a solid theoretical analysis of the proposed method, including the benefits of top-down feedback in enhancing temporal dependency and mitigating gradient vanishing.
3. The experimental results show that TDFormer achieves state-of-the-art performance on multiple datasets, particularly impressive results on ImageNet.
4. The paper is well-structured and clearly written.

## Weaknesses
1. The paper could provide more details on the implementation of the top-down feedback mechanism, particularly how it is integrated with the transformer architecture.
2. The experimental section could benefit from a more extensive analysis of the results, including an error analysis to understand the limitations of the proposed method.

## Questions
1. Can you provide more details on the implementation of the top-down feedback mechanism?
2. Can you provide an error analysis of the results to understand the limitations of the proposed method?
3. How does the proposed method compare with other state-of-the-art methods in terms of computational efficiency?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4