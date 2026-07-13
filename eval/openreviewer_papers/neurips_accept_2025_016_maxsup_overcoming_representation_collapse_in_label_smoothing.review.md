# Review

## Summary
This paper first revisits the Label Smoothing (LS) technique and decomposes the regularization term into two terms: regularization and error amplification. The authors demonstrate that the error amplification term harms the performance. Then, the authors propose a new regularization term, termed MaxSup, which applies the penalty to the largest logit rather than the ground-truth logit. The experiments demonstrate the effectiveness of the proposed MaxSup.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The revisiting of Label Smoothing is interesting and the proposed MaxSup is easy to implement.
3. The experiments demonstrate the effectiveness of the proposed MaxSup.

## Weaknesses
1. The proposed method is not well motivated. Although the authors demonstrate the negative effect of the error amplification term, it is unclear why penalizing the top-1 logit can address this issue.
2. The proposed method is too simple. The idea of penalizing the top-1 logit rather than the ground-truth logit is too straightforward. It is unclear why the authors did not consider penalizing the second logit or the mean of the top-3 logits.
3. The experiments are not convincing. The authors only conduct experiments on the ImageNet dataset with ResNet and DeiT architectures. The results on other datasets and architectures are not reported.

## Questions
1. Why can penalizing the top-1 logit address the issue of error amplification?
2. Why did the authors not consider penalizing the second logit or the mean of the top-3 logits?
3. Why did the authors not report the results on other datasets and architectures?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4