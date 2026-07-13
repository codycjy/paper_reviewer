# Review

## Summary
The paper presents an investigation into using RL agents to address the cold-start problem in AI teacher algorithms that require extensive human learning data. The proposed approach aims to warm-start data-hungry teacher algorithms using RL agents, providing an initial foundation that can be refined and augmented with human learning data.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper introduces a novel approach to addressing the cold-start problem in AI teacher algorithms by leveraging RL agents to generate training data. The proposed two-stage framework and the pedagogy-based teacher algorithms (PERM-H and SimMAC) are innovative contributions to the field.

The paper demonstrates the effectiveness of the approach through human trials in two game-based environments, the Jumper game and the Emergency Response game. The results show that the RL-bootstrapped curricula outperform baselines and match expert-handcrafted curricula.

## Weaknesses
The paper could provide more details on the implementation of the proposed approach, including the specific RL algorithms used, the hyperparameter settings, and the computational resources required.

While the paper mentions that the approach is not intended to replace human data, it would be helpful to discuss the potential limitations and drawbacks of using RL agents as warm-start learners, such as the possibility of RL agents not fully capturing the complexity of human learning patterns.

## Questions
How does the proposed approach handle the potential differences in learning styles and abilities among human learners?

What are the potential limitations and drawbacks of using RL agents as warm-start learners, and how can these be mitigated in future work?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4