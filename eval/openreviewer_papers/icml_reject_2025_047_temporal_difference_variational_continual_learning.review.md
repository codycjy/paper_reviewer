# Review

## Summary
The paper introduces a novel approach to tackle the challenge of catastrophic forgetting in continual learning by leveraging a Bayesian framework and integrating temporal-difference learning objectives. The authors propose a method called Temporal-Difference Variational Continual Learning (TD-VCL), which aims to mitigate the accumulation of approximation errors typical in variational continual learning (VCL) by incorporating multiple past posterior estimates.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper provides a rigorous theoretical foundation, connecting VCL to temporal-difference learning in reinforcement learning, which adds depth to the understanding of the proposed method.

2. The authors introduce a novel objective that addresses a key limitation in existing VCL approaches, potentially improving the retention of past knowledge across tasks.

3. The paper includes a range of experiments on challenging benchmarks, demonstrating the effectiveness of TD-VCL in maintaining high accuracy over successive tasks.

## Weaknesses
1. The paper lacks a discussion on the computational overhead introduced by incorporating n-step regularization, which could be significant for real-time or resource-constrained applications.

2. The authors do not address the potential for negative transfer when integrating n-step temporal-difference learning, where earlier tasks might interfere with the learning of later ones.

3. The reliance on hyperparameters like n and λ, which vary across datasets, raises concerns about the method's generalizability and ease of use in practical scenarios.

## Questions
1. How does the computational complexity of TD-VCL compare to other state-of-the-art continual learning methods, especially in terms of memory and processing requirements?

2. Can the authors elaborate on the specific scenarios or domains where TD-VCL is expected to perform exceptionally well or poorly, based on the observed trends in the experiments?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4