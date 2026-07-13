# Review

## Summary
The authors present a unified framework for performing selective inference after a data analysis pipeline, composed of arbitrary combinations of missing value imputation, outlier detection, and feature selection algorithms. They present a modular implementation of their framework and perform a series of experiments to demonstrate its effectiveness.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
This paper addresses an important, but under-appreciated, problem in data analysis. In particular, the authors consider the setting where a series of data processing steps are performed, and then features are selected and inference is carried out on the resulting model. The authors argue that in this setting, the overall inference procedure must account for the steps of the data processing pipeline, and cannot treat the selection of features and outliers as independent. They provide a novel approach to performing selective inference in this setting, and demonstrate its utility on synthetic and real data.

The paper is well-written and clear. The authors do a good job of motivating the problem, and providing a clear and concise overview of their approach. The experiments are well-designed and demonstrate the effectiveness of the proposed method. The authors also provide code for their method, which is nice.

## Weaknesses
The main weakness of the paper is that the experiments are performed on very small datasets. It would be good to see how the method performs on larger datasets.

## Questions
* How does the performance of the proposed method compare to existing selective inference methods on larger datasets?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4