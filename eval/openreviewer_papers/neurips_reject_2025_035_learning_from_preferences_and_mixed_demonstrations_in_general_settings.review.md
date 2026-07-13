# Review

## Summary
This paper proposes a method for combining preferences and demonstrations. It first proposes a general framework for interpreting all these feedbacks as partial orderings, and then uses this framework to derive LEOPARD, which is a practical algorithm that combines preferences and demonstrations. The paper then evaluates LEOPARD in several standard RL environments and shows that it outperforms several reasonable baselines.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper is overall well-written and easy to follow. The proposed method is simple and easy to implement. The experimental results are strong and support the main claims of the paper.

## Weaknesses
The paper does not seem to have much novelty. It seems like it is simply applying the RRC framework to the case where the feedback consists of preferences and demonstrations. While this is a fine application of an existing framework, it does not seem to rise to the level of novelty expected for an ICLR paper.

## Questions
1. The experiments use synthetic feedback. How does the method perform with real human feedback?

2. The experiments only consider the case where the preferences and demonstrations are for the same task. How does the method perform when the preferences are for one task and the demonstrations are for another?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4