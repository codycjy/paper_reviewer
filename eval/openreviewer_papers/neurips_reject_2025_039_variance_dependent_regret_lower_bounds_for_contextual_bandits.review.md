# Review

## Summary
This paper studies the variance-dependent lower bounds for contextual linear bandits. Specifically, the authors consider a general variance sequence under both pre-fixed and adaptive settings. For the pre-fixed variance sequence, they establish a variance-dependent lower bound for linear contextual bandits. For the adaptive variance sequence, they show a similar lower bound holds when the adversary must generate the variance before observing the decision set. However, when the adversary can generate the variance after observing the decision set, they construct a counter-example showing that it is impossible to construct a variance-dependent lower bound.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
This paper is well-written and easy to follow. The authors study the variance-dependent lower bounds for linear contextual bandits, which is an interesting theoretical problem. They provide a comprehensive analysis for different scenarios and the results are new to my knowledge.

## Weaknesses
1. The variance-dependent lower bound for the adaptive variance sequence seems less meaningful since it only holds with probability $1-1/K$. It would be better if the authors could provide some discussions on this result.

2. It would be better if the authors could provide some discussions on the technical contributions of this paper. For example, compared with Jia et al. (2024), what are the main challenges and novelties in establishing the variance-dependent lower bounds for linear contextual bandits?

## Questions
1. The variance-dependent lower bound for the adaptive variance sequence seems less meaningful since it only holds with probability $1-1/K$. Is it possible to establish a similar result that holds in an expected sense?

2. It would be better if the authors could provide some discussions on the technical contributions of this paper. For example, compared with Jia et al. (2024), what are the main challenges and novelties in establishing the variance-dependent lower bounds for linear contextual bandits?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4