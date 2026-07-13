# Review

## Summary
This paper proposes SPE-Unlearn, a structure-aware parameter-efficient machine unlearning approach tailored for the Transformer architecture. SPE-Unlearn introduces a learnable pair of masks to respectively pinpoint influence-critical parameters in the heads and filters of Transformers. The learning objective of these masks is derived by jointly considering both desiderata of unlearning, i.e., sufficiency in influence removal and efficiency, and optimized through an efficient algorithm featured by a greedy search with a warm start. Extensive experiments on various Transformer models and datasets demonstrate the effectiveness and efficiency of SPE-Unlearn for Transformer unlearning.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. This paper introduces a new paradigm for identifying influence-critical parameters in Transformers, SPE-Unlearn, which operates at the structural level. Our approach theoretically derives importance scores for selecting key structures using a pair of learnable masks. These structure-aware masks can be seamlessly integrated into existing unlearning methods.
2. This paper integrates SPE-Unlearn into second-order unlearning and analyze the gains with structure- aware masks. Extensive experiments across diverse datasets using three models demonstrate the proposed method offers a superior trade-off among efficacy, fidelity, and efficiency.
3. This paper categorizes successive unlearning into two successive scenarios: memory-free unlearning and memory-aided unlearning. Empirical studies show that unlearning with structure-aware masks can handle a greater number of removal requests compared to standard unlearning before retraining becomes necessary, especially in memory-free scenarios.

## Weaknesses
1. The paper does not discuss the computational complexity of the proposed method.
2. The paper does not provide a detailed analysis of the limitations of the proposed method.
3. The paper does not provide a detailed analysis of the potential impact of the proposed method on model fairness.

## Questions
1. What are the potential limitations of the proposed method, and how might they impact its practical application?
2. How does the proposed method handle the potential increase in computational complexity compared to other unlearning methods?
3. How does the proposed method handle the potential impact on model fairness?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4