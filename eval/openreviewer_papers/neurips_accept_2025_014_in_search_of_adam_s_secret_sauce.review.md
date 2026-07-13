# Review

## Summary
This paper studies the Adam optimizer. The authors conduct a large-scale empirical study of several simplified variants of Adam, including the signed gradient and signed momentum methods. They find that while signed momentum methods are faster than SGD, they consistently underperform compared to Adam, even after careful tuning. However, the analysis reveals that constraining the Adam momentum parameters to be equal ($\beta_1 = \beta_2$) preserves near-optimal performance. This choice also offers new theoretical insights and a precise statistical interpretation, showing that Adam implements an online algorithm for estimating the mean and variance of gradients from a mean-field Gaussian variational inference perspective.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. This paper is well-written and well-organized.
2. The paper conducts a large number of experiments to verify the impact of different hyperparameters on the performance of the Adam optimizer.
3. The paper provides a new interpretation of the Adam optimizer, offering new insights for further research.

## Weaknesses
1. The paper only discusses the impact of different hyperparameters on the performance of the Adam optimizer, without providing detailed experimental parameters for each figure, such as learning rate, momentum, and weight decay. This makes it difficult for readers to fully understand the experimental results.
2. The paper lacks a detailed analysis of the experimental results. While it presents the experimental outcomes, it does not delve into the reasons behind these results, leaving readers without a clear understanding of the factors contributing to the observed performance.
3. The paper does not provide a detailed explanation of the theoretical interpretation of Adam. While it presents a new perspective on Adam, it lacks a thorough analysis of why this interpretation is valid, leaving readers without a clear understanding of the theoretical underpinnings.

## Questions
1. In the paper, the authors mention that $\beta_1 = \beta_2$ performs well, but it seems that $\beta_1$ and $\beta_2$ are not the only factors that impact Adam's performance. Have the authors considered the impact of other hyperparameters on Adam's performance?
2. The paper mentions that $\beta_1 = \beta_2$ performs well, but it is not clear why this is the case. Can the authors provide a detailed explanation of the reasons for this?
3. The paper does not provide a detailed explanation of the theoretical interpretation of Adam. Can the authors explain why the new interpretation presented in the paper is valid?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4