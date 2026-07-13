# Review

## Summary
This paper studies the online uniform sampling problem, where the goal is to distribute a sampling budget uniformly across unknown decision times. The authors present the first randomized algorithm designed for this problem and subsequently extend it to incorporate learning augmentation. They provide worst-case approximation guarantees for both algorithms, and illustrate the utility of the algorithms through both synthetic experiments and a real-world case study involving the HeartSteps mobile application.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper provides a clear and concise description of the problem, including the problem formulation, related work, and theoretical analysis. 
2. The paper presents a novel algorithm for the online uniform sampling problem, which is the first of its kind. The algorithm is designed to optimize the trade-off between uniformity and the sum of intervention probabilities, while satisfying the budget constraint.
3. The authors provide a thorough theoretical analysis of the proposed algorithm, including worst-case approximation guarantees. They also conduct extensive experiments on both synthetic and real-world datasets to evaluate the performance of the algorithm.

## Weaknesses
1. The online uniform sampling problem is a variant of the classic online making scheduling problem with machine teach, which has been extensively studied in the literature. The proposed algorithm is also very similar to the existing algorithm for the online making scheduling problem. The main difference is that in the proposed algorithm, the probability of assigning a task to a machine is decreasing over time, while in the existing algorithm, the probability of assigning a task to a machine is increasing over time. Therefore, the novelty of the proposed algorithm is limited.
2. The proposed algorithm is designed to optimize the objective function (1), which is not very intuitive. The first term in the objective function is the total value of all tasks, while the second term is the entropy of the probability distribution. The entropy term is not very intuitive and it is not clear why it is necessary to include it in the objective function.
3. The proposed algorithm is designed to satisfy the budget constraint in expectation. However, in many practical applications, it is more important to satisfy the budget constraint with high probability. The proposed algorithm does not provide any guarantee on the probability of satisfying the budget constraint.

## Questions
1. Can you provide a more intuitive explanation of the objective function (1) and the entropy term in particular?
2. Can you provide a guarantee on the probability of satisfying the budget constraint?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4