# Review

## Summary
This paper studies the problem of learning multiclass linear classifiers with random classification noise (RCN). The authors show that while the problem can be solved efficiently for binary classification, it is statistically intractable for k>=3 classes. Specifically, they prove super-polynomial SQ lower bounds for this problem, even for a constant separation between the classes. The authors also show that the problem remains hard even when the goal is to find a hypothesis that approximates the optimal loss.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a novel hardness result for the problem of learning multiclass linear classifiers with random classification noise. This problem has been studied extensively in the literature, but existing results are limited to binary classification. The authors extend these results to the multiclass setting, showing that the problem becomes statistically intractable for k>=3 classes. This is a significant contribution to the field, as it identifies a fundamental barrier in learning multiclass linear classifiers with RCN.

2. The paper provides a comprehensive analysis of the problem, including upper bounds for the sample complexity and runtime of efficient algorithms, as well as lower bounds based on the SQ complexity. The authors also show that the problem remains hard even when the goal is to find a hypothesis that approximates the optimal loss. This analysis provides a complete picture of the problem and its limitations.

3. The paper is well-written and organized, with clear explanations of the problem and the results. The authors provide intuitive explanations and examples to help the reader understand the significance of their results. The paper is also well-contextualized within the existing literature, with clear references to previous work and discussions of how the current results build upon or differ from prior results.

## Weaknesses
1. The paper does not provide any suggestions for future work or potential directions for overcoming the identified hardness results. While understanding the limitations of an algorithmic problem is important, it would be valuable for the authors to suggest possible approaches for addressing these limitations and potentially overcoming the hardness results.

2. The paper does not provide any empirical results or experimental evaluations of the proposed algorithms or the hardness results. While the theoretical results are strong, empirical results could provide additional support and insights into the practical implications of the findings.

## Questions
1. Can the authors provide any suggestions for future work or potential directions for overcoming the identified hardness results? Are there any specific approaches or algorithms that the authors believe might be promising for addressing these limitations?

2. The paper focuses on the multiclass linear classification problem with RCN. Can the authors discuss how their results might generalize to other problems or settings? Are there any similar problems or settings that the authors believe might exhibit similar hardness results?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4