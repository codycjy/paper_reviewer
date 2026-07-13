# Review

## Summary
This paper presents a general and loss-driven LossLess Compression theoretical framework (LLC), which further delineates the compression neighborhood and higher-order analysis boundaries through the total differential, thereby specifying the error range within which a model can be compressed without loss. To verify the effectiveness of LLC, the authors apply various compression techniques, including quantization and decomposition.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
This paper presents a general and loss-driven LossLess Compression theoretical framework (LLC), which further delineates the compression neighborhood and higher-order analysis boundaries through the total differential, thereby specifying the error range within which a model can be compressed without loss.

## Weaknesses
1. The paper is poorly written. It is difficult to understand the motivation and contributions of this paper. For example, in the introduction section, the authors should introduce the motivation of this paper first, and then introduce the challenges, rather than introducing the related work.

2. The authors claim that "Currently, there is no systematic approach to determining this error boundary or understanding its specific impact on model performance. " However, many quantization works [1, 2] have discussed the impact of quantization error on model performance.

3. The authors claim that "To verify the effectiveness of LLC, we apply various compression techniques, including quantization and decomposition. " However, the main contribution of this paper is to propose a general and loss-driven lossless model compression framework, not a quantization method or a decomposition method. The authors seem to have mixed their contributions with existing methods.

4. The authors should discuss more about the quantization and decomposition methods used in this paper, such as HAWQ and SVD, rather than their own method.

5. The experimental results of this paper are not convincing. The authors should compare more existing methods.

[1] Hessian Based Activations Search for Quantized Neural Networks. IJCNN 2020.
[2] HAWQ-V2: Hessian AWare Trace-Weighted Quantization of Neural Networks. NeurIPS 2020.

## Questions
Please see Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
5