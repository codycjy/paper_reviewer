# Review

## Summary
The paper proposes Constant Q Cepstral Coefficients (CQCC) for classifying neurodegenerative diseases such as Parkinson’s and Amyotrophic lateral sclerosis (ALS) using speech data. The authors argue that CQCC, with its improved time-frequency resolution and form-invariance, outperforms traditional MFCC and other acoustic features like Jitter, Shimmer, and Teager Energy. The study uses the Italian Parkinson’s Voice and Speech dataset and the Minsk2019 ALS database for experiments, showing that CQCC significantly improves classification accuracy, especially when combined with Random Forest and SVM classifiers.

## Soundness
1

## Presentation
2

## Contribution
1

## Strengths
1. The paper presents a novel use of Constant Q Transform (CQT) and Cepstral analysis for neurodegenerative disease classification, which is a creative extension of existing techniques.
2. The paper is generally clear in its presentation, with a well-structured methodology and results section.
3. The paper addresses an important health issue by improving the classification accuracy for neurodegenerative diseases, which could lead to earlier and more accurate diagnoses.

## Weaknesses
1. The paper lacks a comprehensive comparison with state-of-the-art models in neurodegenerative disease classification. While it compares CQCC with MFCC, it does not include comparisons with other advanced deep learning or traditional machine learning models that might achieve better results. The authors should include comparisons with models that use alternative feature sets or more complex architectures. This would provide a clearer picture of CQCC’s effectiveness relative to current best practices.
2. The study uses a relatively small dataset, which may limit the generalizability of the findings. The authors should consider using larger and more diverse datasets to validate their results.
3. The paper does not adequately address how CQCC performs across different languages or dialects. Given the variability in speech patterns, it is essential to demonstrate that CQCC is robust across diverse linguistic contexts. The authors should provide results on datasets that include speakers from different linguistic backgrounds to show the feature’s generalizability.
4. The paper lacks a thorough error analysis to understand the limitations of CQCC. The authors should include a detailed breakdown of classification errors to identify patterns that could indicate where CQCC might fail or require improvement.
5. The paper does not discuss the computational efficiency of CQCC compared to MFCC and other features. Given the potential for real-time applications in clinical settings, it is important to assess the computational cost and processing time of CQCC. The authors should provide a comparative analysis of feature extraction times and computational requirements.
6. The paper does not discuss the robustness of CQCC to noise or variations in audio quality. Real-world recordings often contain noise and artifacts, and it is essential to assess how CQCC performs under such conditions. The authors should evaluate CQCC’s performance on datasets with varying noise levels and audio quality to demonstrate its robustness.

## Questions
1. How does CQCC compare with other state-of-the-art features or models for neurodegenerative disease classification? Can the authors provide comparative results with deeper or more complex models?
2. How does CQCC perform across different languages or dialects? Have the authors tested the feature on multilingual datasets to assess its generalizability?
3. What are the computational requirements for extracting CQCC compared to MFCC? How does the processing time compare for real-time applications?
4. How robust is CQCC to noise and artifacts in audio recordings? Have the authors tested the feature on datasets with varying noise levels to assess its robustness?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
5