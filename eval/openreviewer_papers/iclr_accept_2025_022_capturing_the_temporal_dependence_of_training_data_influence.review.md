# Review

## Summary
This paper studies leave-one-out influence function when the training algorithm is sensitive to the order of data, which violates the assumption of traditional influence function. To address this problem, the authors propose to use data value embedding to approximate the influence of training data at specific time. The data value embedding is computed using the cumulative effect of the original data point’s removal as it propagates through the entire training process. The authors further propose a series of techniques to improve the efficiency of the proposed method. The experimental results show that the proposed method is more efficient than the current most efficient implementation of influence function and provide insights for managing the computational overhead of data selection by strategically timing the selection process.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is well motivated and technically sound. It is novel to use data value embedding to approximate the influence of training data at specific time. The data value embedding is computed using the cumulative effect of the original data point’s removal as it propagates through the entire training process. This is different from the traditional influence function which only considers the model at the end of training.

2. The proposed method is much more efficient than the current most efficient implementation of influence function. It provides insights for managing the computational overhead of data selection by strategically timing the selection process. The experimental results on analyzing training dynamics of foundation models are interesting.

## Weaknesses
1. It would be better if the authors can provide some discussion on the potential limitations of the proposed method. For example, does the proposed method only work for specific types of models or training algorithms? Are there any cases where the proposed method may not be able to provide accurate approximations?

2. The authors mention that the proposed method can be extended to parallelized setting. It would be better if the authors can provide more details on how to do the extension and what are the challenges.

## Questions
1. Does the proposed method only work for specific types of models or training algorithms? Are there any cases where the proposed method may not be able to provide accurate approximations?

2. How to extend the proposed method to parallelized setting? What are the challenges?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4