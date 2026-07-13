# Review

## Summary
This paper examines the limitations of Sliced Mutual Information (SMI) as a measure of statistical dependence, revealing that it can be misleading due to rapid saturation, bias towards information redundancy, and sensitivity to dimensionality. Through theoretical analysis and synthetic experiments, the authors demonstrate that SMI fails to capture increases in statistical dependence and can perform worse than simpler measures like correlation in high-dimensional settings. They argue that SMI's limitations should be acknowledged to avoid misleading applications in areas such as feature selection, representation learning, and independence testing.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
The paper provides a comprehensive critique of SMI, backed by both theoretical analysis and empirical evidence. The authors present a clear and well-structured argument, highlighting the limitations of SMI through illustrative examples and comparative experiments. The findings are particularly relevant given the widespread use of SMI in machine learning and data science applications. By exposing the potential pitfalls of SMI, the paper contributes to a better understanding of statistical measures and their appropriate uses.

## Weaknesses
The paper's focus on SMI's limitations might be perceived as negative, especially given its popularity in the research community. While the authors provide valuable insights into the measure's shortcomings, the paper could benefit from a more balanced perspective by discussing potential alternative measures or strategies for mitigating SMI's limitations. This would enhance the practical utility of the work and provide a more constructive path forward for researchers and practitioners.

## Questions
1. Could the authors elaborate on the potential impact of their findings on real-world applications of SMI? Are there specific domains where the limitations of SMI are more critical than others?
2. Have the authors considered proposing alternative measures or modifications to SMI that could address some of the identified limitations? A discussion on potential remedies would strengthen the paper's contribution.
3. The paper focuses on synthetic experiments. Could the authors comment on how SMI's behavior might vary with real-world data, particularly in cases with complex, high-dimensional distributions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4