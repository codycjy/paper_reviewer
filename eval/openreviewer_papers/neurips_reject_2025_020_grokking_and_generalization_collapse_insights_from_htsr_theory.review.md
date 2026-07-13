# Review

## Summary
This paper investigates the phenomenon of grokking in neural network training, where test accuracy improves drastically despite prolonged periods of near-perfect training accuracy. The authors focus on a specific setup: a depth-3, width-200 ReLU MLP trained on a subset of MNIST without weight decay. They employ the theory of Heavy-Tailed Self-Regularization (HTSR) to track the heavy-tailed exponent $\alpha$, which they find reliably predicts both the initial grokking transition and subsequent anti-grokking phase. The study benchmarks HTSR against other approaches like weight norm analysis and progress measures, showing its unique ability to predict a late-stage catastrophic generalization collapse. The work contributes to understanding generalization dynamics in neural network training.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper provides a novel perspective on grokking by applying HTSR theory, offering a new metric ($\alpha$) for tracking generalization dynamics.
2. The study uniquely identifies a late-stage generalization collapse ("anti-grokking") and demonstrates how $\alpha$ can predict this phase.

## Weaknesses
1. The study is limited to a specific architecture (depth-3, width-200 ReLU MLP) and dataset (MNIST subset), which may limit the generalizability of the findings.
2. The paper acknowledges that interpretations of $\alpha$ should be made carefully, as it is an empirical measure without always clear implications for generalization performance.

## Questions
1. How do the authors envision the HTSR approach being applied practically to improve neural network training, especially regarding the adaptive training strategies or differentiable regularizers mentioned?
2. The paper mentions that $\alpha$ can vary significantly between training runs. Could the authors provide more insights into the stability of $\alpha$ across different runs and its implications for model training?
3. Given the focus on the MNIST dataset, which is relatively simple, do the authors have plans or suggestions for testing the HTSR theory on more complex datasets to validate its generalizability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4