# Review

## Summary
The paper studies the training dynamics of neural networks, in particular how loss curves scale with model size, training compute and training duration. The paper shows that there is a universal scaling law describing the training dynamics when networks are trained optimally (i.e. when they are trained for the minimum amount of time necessary to achieve the lowest loss). The paper also shows that the scaling law is very precise and that different learning rate schedules and architectures all follow the same scaling law. Finally, the paper proposes a simple model of stochastic gradient descent that predicts the scaling law.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The paper studies an important problem, that of understanding the training dynamics of neural networks.
- The paper makes several interesting observations: that there exists a scaling law describing the training dynamics, that the scaling law is very precise, that it applies to different architectures and different learning rate schedules, and that it can be predicted by a simple model.
- The paper is very clearly written.

## Weaknesses
- The paper only studies scaling laws in the context of optimal training. This is a limitation since in practice, networks are often not trained optimally.
- The paper only studies scaling laws for the loss. It would be interesting to study other quantities, like the training and test accuracy.
- The paper only studies scaling laws for the loss when the learning rate decays to zero at the end of training. It would be interesting to study other learning rate schedules, like cyclic learning rates, or learning rates that do not decay to zero.
- The paper only studies scaling laws for the loss when the model is initialized using $\mu$P. It would be interesting to study other initialization schemes.

## Questions
- Do you expect the same scaling law to describe the training dynamics when the network is not trained optimally?
- Do you expect the same scaling law to describe the training dynamics when the learning rate does not decay to zero at the end of training?
- Do you expect the same scaling law to describe the training dynamics when the model is initialized using a different scheme?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4