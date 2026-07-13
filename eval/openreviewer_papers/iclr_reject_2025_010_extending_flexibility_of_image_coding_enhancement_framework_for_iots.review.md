# Review

## Summary
This paper proposes an image compression enhancement framework for edge devices. It introduces a conditional uniform-based sampler for flexible image size reduction and a lightweight transformer-based structure for efficient reconstruction. The framework offers improved adaptability, computational efficiency, and image quality compared to existing methods, as demonstrated through extensive evaluations.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper introduces a novel "erase-and-squeeze" technique that allows for adaptable compression levels, breaking away from the traditional uniform downsampling paradigm.
2. The framework is designed to be highly efficient on both the sender and receiver sides, making it suitable for resource-constrained edge devices.

## Weaknesses
1. The proposed method lacks a clear pipeline diagram, making it difficult to understand the entire workflow. Additionally, the process for generating the erased block map is not clearly explained.
2. The experiments are insufficient. The paper does not compare the proposed method with other downsampling methods, such as those used in GRACE[1] and Real-ESRGAN[2]. Furthermore, the comparison with super-resolution methods is also inadequate, as it only includes two super-resolution methods in Table 1.
3. The paper lacks a comparison of the computational complexity of the proposed method with other downsampling approaches.

[1] Cheng, Yihua, et al. "{GRACE}: {Loss-resilient} Real-time video through neural codecs." 21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24). 2024.
[2] Wang, Xintao, et al. "Real-esrgan: Training real-world blind super-resolution with pure synthetic data." Proceedings of the IEEE/CVF international conference on computer vision. 2023.

## Questions
1. What is the erase block map? How is it generated?
2. How does the proposed method compare with other downsampling methods?
3. How does the proposed method compare with other super-resolution methods in terms of computational complexity and reconstruction performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4