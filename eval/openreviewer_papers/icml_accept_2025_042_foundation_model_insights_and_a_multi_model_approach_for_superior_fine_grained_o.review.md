# Review

## Summary
This paper investigates the use of foundation models (FMs) as alternatives to traditional pre-trained models for subset selection in deep learning. The authors conduct extensive experiments comparing FM-based subset selection with traditional methods across various datasets, revealing that FMs consistently outperform traditional methods on fine-grained datasets but show diminished advantages on coarse-grained datasets with noisy labels. To leverage the complementary strengths of multiple FMs, the authors propose RAM-APL (RAnking Mean-Accuracy of Pseudo-class Labels), a method specifically tailored for fine-grained image datasets. RAM-APL integrates multiple FMs and quantifies data importance by analyzing feature distributions across intra- and inter-class levels. The proposed method achieves state-of-the-art performance on several fine-grained datasets, including Oxford-IIIT Pet, Food-101, and Caltech-UCSD Birds-200-2011.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a thorough empirical study comparing FMs with traditional pre-trained models, providing valuable insights into their relative performance across different datasets.
2. The proposed RAM-APL method effectively leverages multiple FMs and demonstrates significant improvements over existing methods on fine-grained datasets.
3. The paper is well-structured and clearly written, with detailed experimental results and analysis.

## Weaknesses
1. The paper primarily focuses on image classification tasks and datasets. It would be beneficial to explore the applicability of the proposed methods to other data modalities, such as text or audio.
2. The proposed RAM-APL method involves multiple steps and requires careful tuning of hyperparameters. This could make it challenging to implement and adapt to different scenarios.
3. The paper does not provide a detailed analysis of the computational complexity of the proposed method compared to traditional approaches.

## Questions
1. How does the proposed RAM-APL method perform on datasets with significant domain shifts compared to the training data of the foundation models?
2. Can the insights gained from this study be extended to other machine learning tasks beyond subset selection, such as semi-supervised learning or active learning?
3. How sensitive is the performance of RAM-APL to the choice of foundation models? Are there certain types of FMs that are particularly well-suited for subset selection?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4