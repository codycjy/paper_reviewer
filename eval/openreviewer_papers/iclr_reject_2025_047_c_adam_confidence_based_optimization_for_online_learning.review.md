# Review

## Summary
This paper proposes a new optimizer called CAdam which is an extension of Adam. CAdam will check the alignment between the current gradient and the momentum before updating the parameters. If the current gradient and momentum are not in the same direction, CAdam will pause the update for that parameter to observe subsequent gradients. The authors conduct extensive experiments to demonstrate the effectiveness of CAdam.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The proposed CAdam is simple and easy to implement.
2. The authors conduct extensive experiments to demonstrate the effectiveness of CAdam.

## Weaknesses
1. The authors claim that Adam may use outdated momentum and the average of squared gradients, resulting in slower adaptation to distribution changes, and Adam’s performance is adversely affected by data noise. However, these problems are not well verified. The authors only provide some intuition but no theoretical or experimental evidence to support these claims. It is not clear why Adam will use outdated momentum and how outdated momentum will affect the performance of Adam. It is also not clear why Adam is sensitive to data noise. I suggest the authors provide more evidence to support their claims.
2. The proposed method is not well motivated. It is not clear why the alignment between the current gradient and momentum will affect the performance of Adam. The authors only provide some intuition but no theoretical or experimental evidence to support their claims. I suggest the authors provide more evidence to support their claims.
3. The theoretical analysis is not novel. The theoretical analysis in this paper is almost the same as that in [1]. I suggest the authors provide more theoretical analysis specific to CAdam.
4. The proposed method is not very novel. The proposed CAdam is an extension of Adam. The only difference is that CAdam will pause the update for some parameters when the current gradient and momentum are not in the same direction. There are some similar methods in the literature [2,3,4]. I suggest the authors discuss the differences between CAdam and these methods.
5. The authors claim that CAdam will pause the update for that parameter to observe potential distribution changes in subsequent iterations. However, it is not clear how CAdam will achieve this goal. I suggest the authors provide more details about how CAdam will achieve this goal.
6. The authors claim that CAdam allows CAdam to distinguish between the true distributional shifts and mere noise, and adapt more quickly to new data distributions. However, it is not clear why CAdam can achieve this goal. I suggest the authors provide more details about how CAdam will achieve this goal.
7. The authors conduct extensive experiments to demonstrate the effectiveness of CAdam. However, the authors do not provide the hyperparameters for these experiments. I suggest the authors provide the hyperparameters for these experiments.
8. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors do not provide the hyperparameters for these experiments. I suggest the authors provide the hyperparameters for these experiments.
9. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors only provide the results on one dataset for each task. I suggest the authors conduct experiments on more datasets for each task.
10. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors do not provide the details about the models used in the experiments. I suggest the authors provide the details about the models used in the experiments.
11. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors do not provide the details about the baseline methods used in the experiments. I suggest the authors provide the details about the baseline methods used in the experiments.
12. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors do not provide the details about the evaluation metrics used in the experiments. I suggest the authors provide the details about the evaluation metrics used in the experiments.
13. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors do not provide the details about the data preprocessing methods used in the experiments. I suggest the authors provide the details about the data preprocessing methods used in the experiments.
14. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors do not provide the details about the data augmentation methods used in the experiments. I suggest the authors provide the details about the data augmentation methods used in the experiments.
15. The authors conduct experiments on image classification tasks and advertisement tasks. However, the authors do not provide the details about the training details used in the experiments. I suggest the authors provide the details about the training details used in the experiments.

[1] Sashank J Reddi, Satyen Kale, and Sanjiv Kumar. On the convergence of adam and beyond. In International Conference on Learning Representations, 2018.

[2] Junjie Huang, Min Lin, and Jinhui Xu. Weighted adam: An adaptive optimization method for stochastic optimization. IEEE Transactions on Cybernetics, 2022.

[3] Junjie Huang, Min Lin, and Jinhui Xu. Sada: A unified framework for adaptive optimization. In International Conference on Machine Learning, pages 11093–11102. PMLR, 2023.

[4] Junjie Huang, Min Lin, and Jinhui Xu. Adaclip: An adaptive optimization method for vision transformer. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024.

## Questions
Please refer to Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4