# Review

## Summary
This paper studies the effect of increasing the depth of networks for self-supervised RL, finding that it can enable new goal-reaching capabilities in contrastive RL. They conduct experiments on a suite of continuous control tasks and find that increasing the depth of the network can qualitatively change the behaviors learned, and can outperform other goal-conditioned baselines. They also find that increasing the depth is more effective than increasing the width for enabling scaling in contrastive RL.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow
- The paper conducts extensive experiments across a variety of continuous control tasks, and shows that increasing the depth of the network can enable new goal-reaching capabilities in contrastive RL
- The paper finds that increasing the depth is more effective than increasing the width for enabling scaling in contrastive RL
- The paper also conducts a number of ablations to understand what factors are important for scaling in contrastive RL, such as increasing the batch size, scaling both the actor and critic networks, and increasing the depth of the network

## Weaknesses
- While the paper shows that increasing the depth of the network can enable new goal-reaching capabilities in contrastive RL, it is not clear why this is the case. The paper hypothesizes that increasing the depth leads to richer learned representations, but does not provide any direct evidence for this hypothesis. It would be interesting to see if the representations learned by deeper networks are indeed richer, as this would help to explain the observed performance improvements. For example, the paper could visualize the latent representations learned by networks of different depths, or evaluate the performance of downstream tasks that depend on the quality of the representations.
- The paper focuses on increasing the depth of the network, but does not provide any new insights or algorithms for self-supervised RL. The paper simply uses the existing contrastive RL algorithm and applies it to networks of increasing depth. It would be interesting to see if the authors could develop new algorithms or techniques specifically designed for training deep networks in self-supervised RL. This could involve addressing specific challenges associated with training deep networks, such as increased computational requirements or instability during training.
- The paper does not compare the performance of their approach to other state-of-the-art methods in self-supervised RL. It would be interesting to see how their approach compares to other approaches, such as those that use more sophisticated contrastive learning objectives or those that incorporate additional forms of self-supervision. This would help to better understand the relative strengths and weaknesses of their approach.

## Questions
- The paper shows that increasing the depth of the network can enable new goal-reaching capabilities in contrastive RL, but does not provide any direct evidence for the hypothesis that increasing the depth leads to richer learned representations. Could the authors provide any direct evidence for this hypothesis? For example, could the authors visualize the latent representations learned by networks of different depths, or evaluate the performance of downstream tasks that depend on the quality of the representations?
- The paper focuses on increasing the depth of the network, but does not provide any new insights or algorithms for self-supervised RL. Could the authors develop new algorithms or techniques specifically designed for training deep networks in self-supervised RL? This could involve addressing specific challenges associated with training deep networks, such as increased computational requirements or instability during training.
- The paper does not compare the performance of their approach to other state-of-the-art methods in self-supervised RL. Could the authors compare the performance of their approach to other approaches, such as those that use more sophisticated contrastive learning objectives or those that incorporate additional forms of self-supervision? This would help to better understand the relative strengths and weaknesses of their approach.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4