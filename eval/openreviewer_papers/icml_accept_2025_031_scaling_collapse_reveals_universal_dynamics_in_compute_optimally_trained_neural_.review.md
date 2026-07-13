# Review

## Summary
The paper studies the training dynamics of neural networks by studying the scaling of the loss w.r.t. the training compute (FLOPs). It is observed that the loss curves of models of different sizes, when appropriately normalized, collapse onto a single curve. This is then explained by considering a simple model of the SGD noise dynamics.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper studies an important problem, that of understanding the training dynamics of neural networks. It makes interesting observations regarding the scaling of the loss with the training compute, and proposes a simple model that explains the observed phenomena.

## Weaknesses
While the observations made in the paper are interesting, I have some concerns regarding their significance and novelty:

1. **Significance**: The main observation in the paper is that the loss curves of models of different sizes, when appropriately normalized, collapse onto a single curve. This is then used to infer that the training dynamics of the models are similar. However, it is not clear to me why this is a meaningful conclusion. For instance, consider two models with very different architectures (say a ResNet and a Transformer). It is possible that during the early stages of training, the loss curves of the two models are very different. However, if the training is continued for a long time, it is possible that the loss curves become similar (after appropriate normalization). This is because the two models may start to behave similarly during the later stages of training. The fact that the loss curves become similar (after normalization) does not imply that the training dynamics of the two models are similar. In fact, the training dynamics of the two models may differ significantly in the early stages. Thus, I believe that the significance of the main observation in the paper needs to be clarified.

2. **Novelty**: The main observation in the paper is that the loss curves of models of different sizes, when appropriately normalized, collapse onto a single curve. While this observation is interesting, it is not completely novel. For instance, this kind of scaling behavior has been observed in previous work [1] (see Figure 3). Moreover, the scaling behavior observed in the current paper is similar to the scaling behavior of the form $L \sim t^{-\alpha}p^{-\beta}$, which has been studied in previous work [2]. Thus, I believe that the novelty of the main observation in the paper needs to be clarified.

[1] Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., ... & Amodei, D. (2020). Scaling laws for neural language models. arXiv preprint arXiv:2001.08361.

[2] Yang, G., & Hu, E. J. (2021, July). Feature learning in infinite-width neural networks. In International Conference on Machine Learning (pp. 11885-11894). PMLR.

## Questions
Please see the weaknesses section.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4