# Review

## Summary
The paper proposes a method to derive the statistical significance of features selected by a data analysis pipeline, which is a sequence of feature processing steps such as missing value imputation, outlier detection, and feature selection. The method is based on selective inference, which computes p-values for hypotheses that are selected from a set of hypotheses based on data. The authors propose to use selective inference to compute p-values for features selected by a pipeline. The main challenge is to characterize the selection event, which depends on the specific steps in the pipeline. The authors propose a line search method to identify the relevant truncation intervals to compute the p-values. The authors also provide a software package to easily specify pipelines and compute the corresponding p-values. The authors evaluate the type I error rate and power of the method on synthetic data and real data.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper addresses an important problem of quantifying the uncertainty of features selected by a data analysis pipeline. The method has the potential to improve the reliability of machine learning pipelines.
- The proposed method based on selective inference is a principled approach that can provide valid p-values for any pipeline configuration.
- The line search method is a novel approach to identify the relevant truncation intervals. It is based on parametric programming and directed acyclic graphs, which is a principled and efficient way to identify the intervals.
- The software package provides a simple way to specify pipelines and compute the corresponding p-values. It would be useful for practitioners.

## Weaknesses
- The method is limited to linear models and does not account for non-linear relationships between the features and the response variable.
- The method assumes that the noise variance is known or estimable from an independent dataset. In practice, the noise variance is often unknown and needs to be estimated from the data, which can bias the p-values.
- The method does not account for model selection bias, which can inflate the p-values if the pipeline selects a model with a large number of features.
- The method does not provide confidence intervals for the p-values, which are needed to quantify the uncertainty of the significance.
- The evaluation is limited to a few synthetic datasets and real datasets. More extensive evaluation on diverse datasets would be needed to demonstrate the robustness and scalability of the method.

## Questions
- How does the method perform when the noise variance is unknown and needs to be estimated from the data?
- How does the method account for model selection bias when the pipeline selects a model with a large number of features?
- Can the method provide confidence intervals for the p-values to quantify the uncertainty of the significance?
- How does the method scale to high-dimensional datasets with thousands of features?
- How does the method perform on more complex datasets such as images or text documents?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4