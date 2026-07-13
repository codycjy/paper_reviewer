# Review

## Summary
This paper proposes a new way to compute the data Shapley value, i.e., the contribution of each data point to the performance of a machine learning model. The proposed method, called In-Run Data Shapley, is designed to be computationally efficient and to provide insights into the contribution of data for a specific model training run. The authors demonstrate the effectiveness of In-Run Data Shapley through several case studies, highlighting its potential applications in data curation, understanding data contribution during training, and addressing copyright issues in generative AI.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work, highlighting the limitations of existing methods and the need for a more efficient and effective data attribution approach.
2. The proposed In-Run Data Shapley method is innovative and addresses the computational challenges and conceptual limitations of traditional retraining-based Data Shapley methods. The approach of quantifying data contributions during a specific training run offers a new perspective on data attribution.
3. The authors provide a thorough empirical evaluation of In-Run Data Shapley, including runtime analysis, fidelity assessment, and case studies. The experiments demonstrate the efficiency and effectiveness of the proposed method in various settings.

## Weaknesses
1. The proposed In-Run Data Shapley method relies on several approximations, such as first- and second-order Taylor expansions, to make the data attribution computation tractable. While the authors provide justifications for these approximations, the accuracy and reliability of the resulting data values may be affected.
2. The method requires the availability of validation data before training, which may not always be practical. The authors could discuss potential solutions for scenarios where validation data arrives after the model has been trained.
3. The paper focuses on models trained using stochastic gradient descent (SGD) and does not explore the extension of In-Run Data Shapley to other optimization algorithms, such as Adam. The authors could mention the challenges and potential approaches for adapting their method to other optimizers.

## Questions
1. How does the choice of validation data affect the results of In-Run Data Shapley? Have the authors explored the sensitivity of the method to different validation sets?
2. Can the In-Run Data Shapley method be extended to other machine learning tasks, such as image classification or text classification? What challenges might arise in such extensions?
3. How does the method handle cases where the training data is highly imbalanced or noisy? Does the quality of the data affect the accuracy of the data values?
4. How does the method handle cases where the training data is highly imbalanced or noisy? Does the quality of the data affect the accuracy of the data values?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4