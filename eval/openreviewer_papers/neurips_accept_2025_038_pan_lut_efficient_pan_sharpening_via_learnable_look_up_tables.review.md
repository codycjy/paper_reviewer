# Review

## Summary
This paper proposes a novel learnable look-up table (LUT) framework for pan-sharpening, called Pan-LUT. The method introduces three specifically designed LUTs: the PAN-guided look-up table (PGLUT) for channel-wise spectral mapping, the spatial details look-up table (SDLUT) for capturing fine-grained spatial details, and the adaptive output look-up table (AOLUT) for adaptive channel aggregation. The proposed method achieves a balance between performance and computational efficiency, making it possible to process 15K×15K remote sensing images on a 24GB GPU.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is novel and addresses the computational efficiency issue of deep learning-based pan-sharpening methods.
2. The proposed method achieves a good balance between performance and computational efficiency, making it possible to process large remote sensing images efficiently.
3. The proposed method outperforms traditional methods by a large margin in terms of speed and efficiency.

## Weaknesses
1. The proposed method is designed specifically for pan-sharpening and cannot be extended to other image fusion tasks.
2. The proposed method is not as effective in reducing dimensional disaster as deep learning-based methods.

## Questions
1. The proposed method is designed specifically for pan-sharpening and cannot be extended to other image fusion tasks. However, deep learning-based methods can be extended to other image fusion tasks. Therefore, the generalization ability of the proposed method is weaker than that of deep learning-based methods.
2. The proposed method is not as effective in reducing dimensional disaster as deep learning-based methods. The dimension disaster problem in pan-sharpening is very important and urgent. Therefore, the practical value of the proposed method is limited.
3. The proposed method introduces three specifically designed LUTs, which may increase the complexity of the method. Therefore, the method may not be suitable for very large images or videos.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4