# Review

## Summary
The paper proposes RM-BENCH, a benchmark for evaluating reward models in language models. The benchmark aims to assess reward models' sensitivity to subtle content differences and resistance to style biases, which are often overlooked in existing benchmarks. The authors evaluate various reward models on RM-BENCH and find that even state-of-the-art models struggle to exceed random-level performance under style bias interference, highlighting significant room for improvement in current reward models.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper addresses an important and timely issue in the field of language model alignment, namely the evaluation of reward models.
2. The paper is well-written and easy to follow, with clear explanations of the benchmark construction process and evaluation metrics.
3. The authors provide a comprehensive evaluation of nearly 40 reward models on RM-BENCH, revealing insights into the limitations of current models.

## Weaknesses
1. While the paper focuses on evaluating reward models, it would be beneficial to include a discussion on how the findings can translate to improved policy model performance and alignment. This could include insights on how to use RM-BENCH to select or train better reward models that lead to more effective language model alignment.
2. The paper could benefit from a more detailed discussion of the limitations of RM-BENCH, including potential biases or shortcomings in the benchmark construction process or evaluation metrics.

## Questions
1. How well do the findings on reward model performance on RM-BENCH translate to real-world language model applications and downstream tasks?
2. How do the authors plan to address the limitations of RM-BENCH in future work, and what are the potential directions for improving the benchmark?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4