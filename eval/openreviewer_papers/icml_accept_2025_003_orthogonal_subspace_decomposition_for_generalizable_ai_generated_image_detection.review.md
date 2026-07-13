# Review

## Summary
This paper presents a novel approach to detecting AI-generated images (AIGIs), addressing the critical challenge of generalization to unseen forgery techniques. The authors identify the asymmetry phenomenon, where conventional detectors overfit to limited training data, leading to poor performance on novel fake images. To tackle this, they propose decomposing the feature space into two orthogonal subspaces using Singular Value Decomposition (SVD). This method preserves pre-trained knowledge in the principal subspace while adapting the residual subspace to learn new forgery patterns. The approach is shown to significantly improve generalization across various deepfake and synthetic image benchmarks, achieving state-of-the-art results with minimal parameter overhead. The paper also highlights the hierarchical relationship between real and fake data, enhancing the model's ability to make semantically aligned discriminations.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The use of SVD for orthogonal subspace decomposition in AIGI detection is novel and well-justified, providing a clear mathematical framework to address overfitting and improve generalization.
- The paper provides extensive experimental evidence across multiple datasets and protocols, demonstrating the robustness and superiority of the proposed method over existing state-of-the-art techniques.
- The method achieves impressive results with a significantly lower parameter count, highlighting its efficiency and practical applicability.
- The theoretical insights, particularly the asymmetry phenomenon and the hierarchical relationship between real and fake data, contribute to the understanding of AIGI detection and are well-supported by empirical analysis.

## Weaknesses
- While the method shows strong performance on the tested datasets, the paper lacks discussion on its robustness to various forms of image manipulation and degradation, such as different compression techniques, resolution changes, or other distortions.
- The paper could benefit from a more detailed analysis of the computational efficiency, including training time comparisons with other methods, especially for large-scale datasets.
- The approach's reliance on pre-trained models might limit its applicability in scenarios where such models are not readily available or when the distribution of training data significantly differs from the test data.

## Questions
- How does the proposed method perform on AIGIs that exhibit significant compression artifacts or other forms of degradation? Have the authors tested the robustness of the method against various image processing techniques?
- Could the authors provide more details on the training time and computational resources required, especially when scaling the method to larger datasets or higher-resolution images?
- Have the authors explored the potential of extending this method to other forms of AI-generated content, such as text or audio?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4