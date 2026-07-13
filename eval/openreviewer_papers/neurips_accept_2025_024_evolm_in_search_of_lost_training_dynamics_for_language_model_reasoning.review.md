# Review

## Summary
This paper studies the effect of different training stages in the life cycle of a language model. Specifically, they study the effect of pre-training, continued pre-training, supervised fine-tuning, and reinforcement learning. They conduct experiments on different scales of model sizes and datasets. They evaluate the model on both upstream and downstream tasks. Based on their experiments, they draw many conclusions and provide insights.

## Soundness
3

## Presentation
4

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The presentation is great.
2. The experiments are solid. They conduct experiments on different model sizes and datasets.
3. The conclusions drawn from their experiments are interesting and insightful.

## Weaknesses
1. The paper mainly focuses on reasoning tasks. It would be better to study other types of tasks as well.
2. The paper mainly focuses on models with sizes up to 4B. It is not clear whether these conclusions can be generalized to larger models.

## Questions
1. In the paper, you draw many conclusions. However, how do you get these conclusions exactly? Do you conduct statistical significance tests on these numbers?
2. In Table 1, why are the numbers of 4B sometimes better than that of 1B? I would expect the numbers of 4B to be at least as good as that of 1B.
3. In Table 2, the CPT Config is 16B. Should it be 8+32 or 8+42?
4. In Figure 5, why is the performance of SFT+RL better than SFT only when there is CPT? If there is no CPT, why is SFT only better than SFT+RL?
5. In Figure 6, why do you evaluate Maj@16, RM@16, and Pass@16 instead of Greedy?
6. In Figure 7, why do you evaluate Maj@16, RM@16, and Pass@16 instead of Greedy?
7. In Figure 8, why do you evaluate Maj@16, RM@16, and Pass@16 instead of Greedy?
8. In Figure 8, why is Pass@16 worse when the number of RL examples increases from 0 to 400K? Shouldn't it be better?
9. In Table 3, why is 20BT int better than 20BT full on Math Level 2?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4