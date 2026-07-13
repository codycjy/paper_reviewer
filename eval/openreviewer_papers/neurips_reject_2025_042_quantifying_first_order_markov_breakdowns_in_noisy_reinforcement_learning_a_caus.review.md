# Review

## Summary
The paper studies the problem of partial observability in reinforcement learning. The authors propose a new metric called Markov Violation Score (MVS) to measure the extent to which the Markov property is violated in the learned policy. They then conduct experiments on several classic control tasks to show that their proposed metric is correlated with the performance of the learned policy.

## Soundness
2

## Presentation
3

## Contribution
1

## Strengths
1. The paper is well-written and easy to follow. The authors clearly describe their proposed metric and the experimental setup.

2. The paper studies an important problem of partial observability in reinforcement learning. The proposed metric, if shown to be effective, can be a useful tool for practitioners.

## Weaknesses
1. The main weakness of the paper is the lack of theoretical justification for the proposed metric. The authors propose MVS as a measure of how "severely" the one-step assumption is broken. However, it is not clear why their proposed metric is a good measure of this severity. In particular, the authors should provide some theoretical analysis on the cases where MVS is non-zero and the Markov property is violated, and show that their proposed metric is indeed correlated with the extent of the violation. Without such analysis, it is difficult to see why the proposed metric is useful.

2. The experiments in the paper are limited to three classic control tasks and the RL algorithm used is only PPO. The authors should conduct experiments on a wider range of tasks and RL algorithms to show the generality of their proposed metric.

3. The paper does not compare MVS with any existing methods for handling partial observability. The authors should compare their proposed metric with other methods, such as those based on information theory, to show why their proposed metric is a better measure of partial observability.

## Questions
1. Can the authors provide some theoretical analysis on the cases where MVS is non-zero and the Markov property is violated, and show that their proposed metric is indeed correlated with the extent of the violation?

2. Can the authors conduct experiments on a wider range of tasks and RL algorithms to show the generality of their proposed metric?

3. Can the authors compare their proposed metric with other methods, such as those based on information theory, to show why their proposed metric is a better measure of partial observability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4