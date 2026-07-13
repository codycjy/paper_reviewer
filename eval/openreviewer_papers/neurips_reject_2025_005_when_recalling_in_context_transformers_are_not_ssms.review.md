# Review

## Summary
This paper compares the performance of transformers and state-space models (SSMs) on associative recall (AR) tasks, revealing significant differences in optimization sensitivity and scaling behavior. The authors show that while transformers are generally better at AR, their performance is less sensitive to learning rate choices and scales less effectively with width compared to SSMs like Mamba. Additionally, they find that single-layer transformers exhibit induction head-like dynamics during training, unlike SSMs, which have smoother training trajectories. Through architectural ablations, they demonstrate that Mamba's performance is robust to various modifications, suggesting that its advantages stem from more than just specific architectural components.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The authors conduct comprehensive experiments across different model architectures, sequence lengths, and hyperparameters, providing detailed performance metrics and training dynamics analysis.
2. The study uncovers important insights about the scaling behavior and optimization challenges of modern recurrent models, which could guide future research in sequence modeling.

## Weaknesses
1. The study is limited to a single synthetic task (MQAR), which may not fully represent real-world language processing. While MQAR is a useful benchmark, the findings might not generalize to more complex natural language tasks.
2. The authors acknowledge that optimization issues like learning rate sensitivity and vanishing gradients could disproportionately affect recurrent models, especially SSMs. However, the paper could benefit from more concrete suggestions for improving the optimization landscape of these models.
3. The paper focuses on comparing two specific model classes (transformers and SSMs). However, it doesn't explore how the findings might generalize to other types of recurrent models or hybrid architectures that combine attention mechanisms with recurrence.

## Questions
1. Could the authors provide more insights into why single-layer transformers fail at MQAR? Is it related to the lack of multi-layer induction head dynamics, or are there other fundamental limitations?
2. The study shows that Mamba's performance is relatively stable across different architectural modifications. Could the authors comment on whether similar robustness is observed for other SSM variants like Mamba2 or DeltaNet?
3. Given the challenges observed with learning rate optimization in SSMs, have the authors considered exploring alternative optimization strategies or learning rate schedulers that might improve performance stability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4