# Review

## Summary
This paper proposes a method called CF-ZIR (Common Feature learning for Zero-shot Image Recognition) to address the key issue in zero-shot image recognition of inferring and transferring relationships between visual and semantic spaces. The proposed method learns fine-grained visual-semantic relationships at the image level by leveraging inter-class association information from class semantic vectors to guide the extraction of common visual features. It introduces a dual-layer embedding method and constructs a fine-grained visual-semantic cross-domain dictionary to capture associations between independent visual and semantic class information. Experiments on three benchmark datasets demonstrate the effectiveness of the proposed approach.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper proposes a new method, CF-ZIR, which learns fine-grained visual-semantic relationships at the image level, addressing the issue of ignoring inter-class associations in existing methods.
2. The paper introduces a dual-layer embedding method that establishes relationships between visual-attributes and visual-semantics, improving the accuracy of recognition.
3. The paper conducts a large number of experiments on three benchmark datasets and demonstrates the significant performance improvements achieved by the CF-ZIR method.

## Weaknesses
1. The paper writing needs improvement. The abstract is not well organized, and the introduction section does not clearly outline the contributions and innovations of the paper.
2. The paper lacks a comparison with the latest methods, such as those from 2024, and does not provide sufficient analysis of the experimental results.
3. The paper does not clearly explain the rationale for the loss function design and does not provide ablation experiments to verify the effectiveness of each component.
4. The paper lacks a comparison of the computational complexity of the proposed method with other methods and does not provide an analysis of the computational efficiency.
5. The paper does not provide a detailed description of the implementation details, such as the hyperparameter settings and the specific network architecture used.

## Questions
1. How does the CF-ZIR method differ from existing zero-shot learning methods in terms of learning fine-grained visual-semantic relationships at the image level?
2. What are the specific innovations of the dual-layer embedding method, and how does it improve the accuracy of recognition compared to existing methods?
3. Can the authors provide more detailed explanations of the loss function design and conduct ablation experiments to verify the effectiveness of each component?
4. How does the CF-ZIR method perform in terms of computational complexity and efficiency compared to other methods? Can the authors provide a detailed analysis of the computational resources required?
5. Can the authors provide more implementation details, such as hyperparameter settings and specific network architectures used, to help readers reproduce the results?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
5