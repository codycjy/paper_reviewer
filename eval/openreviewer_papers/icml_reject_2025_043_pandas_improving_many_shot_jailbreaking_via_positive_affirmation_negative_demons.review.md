# Review

## Summary
The paper introduces PANDAS, a hybrid technique that improves many-shot jailbreaking by modifying these fabricated dialogues with Positive Affirmations, Negative Demonstrations, and an optimized Adaptive Sampling method tailored to the target prompt’s topic. The authors also introduce ManyHarm, a dataset of harmful question–answer pairs, and demonstrate through extensive experiments that PANDAS significantly outperforms baseline methods in long-context scenarios.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is effective and the experiments are solid.
3. The authors conduct an attention analysis to understand how models’ long-context capabilities are exploited and how PANDAS improves upon MSJ.

## Weaknesses
1. The proposed method is not that novel. The authors simply add some components to the existing method Many-shot jailbreaking (MSJ).
2. The authors should also consider some other baselines. For example, some works also study the order of demonstrations. The authors should compare with those methods.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4