# Review

## Summary
The paper investigates the hidden layer properties of LLMs. In particular, they show that intermediate layers can encode richer representations and outperform last layer's performance on a range of downstream tasks. They propose a framework of representation quality metrics and provide insights into how each layer balances information compression and signal preservation.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a detailed analysis of hidden layer properties of LLMs, challenging the conventional wisdom that only final layers matter.
- The authors propose a unified framework of representation quality metrics, connecting information theory, geometry, and invariance to input perturbations.
- The paper presents extensive experiments on 32 text-embedding tasks across different architectures (transformers, state-space models) and domains (language, vision), demonstrating the consistency of intermediate layers' performance.
- The findings have practical implications for feature extraction and generation tasks, suggesting the use of mid-layer representations for more robust and accurate results.

## Weaknesses
- The paper could benefit from a more detailed discussion on the practical applications and implications of the findings, especially for readers who may not be familiar with the technical details of LLMs.
- While the authors provide a theoretical framework, the paper could further strengthen its claims with more rigorous empirical analysis and comparisons with existing methods.
- The paper could include more detailed ablation studies to isolate the impact of different components of the proposed framework and provide a deeper understanding of their contributions.

## Questions
- Can the authors provide more insights into the practical implications of using mid-layer representations for downstream tasks? How can this information guide the development of new LLM architectures?
- How generalizable are the findings across different types of LLMs and tasks? Are there any limitations or biases in the experimental setup that could affect the results?
- Can the authors provide more details on the computational resources required to implement the proposed framework and evaluate the mid-layer representations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4