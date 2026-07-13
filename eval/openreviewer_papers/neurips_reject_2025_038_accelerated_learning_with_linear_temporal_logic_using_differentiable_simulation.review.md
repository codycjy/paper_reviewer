# Review

## Summary
This paper presents a method that integrates LTL with differentiable simulators, facilitating efficient gradient-based learning directly from LTL specifications. The authors introduce soft labeling to achieve differentiable rewards and states, mitigating the sparse-reward issue intrinsic to LTL without compromising objective correctness.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
The research topic of this paper is interesting and important. The paper is well-organized.

## Weaknesses
1. The authors claim that they propose the first method that integrates LTL with differentiable simulators, facilitating efficient gradient-based learning directly from LTL specifications. However, there are already some papers that have proposed to integrate LTL with gradient-based methods [1-2]. The authors should discuss these works and clarify the novelty of their approach.

2. The authors should provide more details about the implementation of their method, including the specific algorithms used, the hyperparameters, and the training procedure. This would help to reproduce the results and understand the method better.

3. The authors should provide more details about the experimental setup, including the specific environments used, the action spaces, and the observation spaces. This would help to understand the experiments better.

4. The authors should discuss the limitations of their approach, such as the computational complexity, the scalability, and the applicability to real-world scenarios.

[1] Leung K, Aréchiga N, Pavone M. Backpropagation through signal temporal logic specifications: Infusing logical structure into gradient-based methods[J]. The International Journal of Robotics Research, 2023, 42(6): 356-370.

[2] Meng Y, Fan C. Signal temporal logic neural predictive control[J]. arXiv preprint arXiv:2301.10422, 2023.

## Questions
1. How does the proposed method compare to other methods that integrate LTL with gradient-based methods [1-2]? What are the advantages and disadvantages of the proposed method compared to these existing methods?

2. What are the specific algorithms used in the proposed method? How are the hyperparameters selected? What is the training procedure like?

3. What are the specific environments used in the experiments? What are the action spaces and the observation spaces of these environments?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4