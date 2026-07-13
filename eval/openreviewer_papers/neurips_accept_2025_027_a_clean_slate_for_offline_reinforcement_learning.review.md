# Review

## Summary
The paper addresses the issues of ambiguous definitions and entangled designs in offline reinforcement learning (RL). It introduces a transparent evaluation procedure that quantifies online tuning budgets and provides clean implementations of various offline RL methods. The authors propose a unified algorithm, Unifloral, which encapsulates diverse prior approaches within a single hyperparameter space. Using Unifloral and the transparent evaluation procedure, two new algorithms, TD3-ACWR (model-free) and MoBRAC (model-based), are developed, demonstrating substantial performance improvements over established baselines.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to understand.
2. The taxonomy proposed in the paper is reasonable and easy to follow.
3. The paper provides implementations of various offline RL algorithms, which is beneficial for the offline RL community.

## Weaknesses
1. The paper lacks novelty. Although the unified design of the algorithm is interesting, the paper does not provide new insights into offline RL. Additionally, the proposed methods, TD3-AWR and MoBRAC, are not novel.
2. The evaluation of the proposed methods is limited to the D4RL benchmark, which is not sufficient. More experiments on other datasets are needed to validate the effectiveness of the methods.
3. The paper does not provide an analysis of the computational complexity of the proposed methods.

## Questions
1. The paper claims that the implementation of various offline RL algorithms is beneficial for the offline RL community. However, it seems that the implementations are not very clean, and some algorithms are not well organized, which can still confuse people who are new to the field. How do the authors plan to address this issue?
2. How do the proposed methods perform on other datasets beyond the D4RL benchmark?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4