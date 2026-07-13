# Review

## Summary
This paper presents an automated code review framework that integrates multiple LLMs to perform defect detection at repository level and merge request granularity. The framework is deployed in a real-world production environment and shows significant performance improvement over existing methods. The authors also conduct extensive experiments to analyze the effectiveness of individual components and provide valuable insights.

## Soundness
4

## Presentation
3

## Contribution
4

## Strengths
- The paper is well-written and easy to follow. The figures are helpful in understanding the overall framework and individual components.
- The authors conduct a comprehensive evaluation, including both main experiments and ablation studies, to demonstrate the effectiveness of the proposed method.
- The results show impressive performance gains over existing methods, indicating the potential of the framework in real-world applications.

## Weaknesses
- The authors do not provide enough details about the implementation of the framework. For example, the specific LLMs used for each role, the hyperparameters for the filtering mechanism, and the chain-of-thought templates are not disclosed.
- While the authors mention that the framework is deployed in a real-world production environment, they do not provide enough information about the production environment. For example, the number of developers using the tool, the volume of code changes reviewed, and the types of defects detected are not reported.
- The authors do not conduct a user study to evaluate the perceived usefulness and usability of the tool from the developers' perspective. While they report the key bug inclusion rate and false alarm rate, these metrics do not necessarily reflect the real-world effectiveness of the tool.

## Questions
1. Can you provide more details about the implementation of the framework? Specifically, what LLMs do you use for each role, what are the hyperparameters for the filtering mechanism, and what are the chain-of-thought templates?
2. Can you provide more information about the production environment where the framework is deployed? Specifically, how many developers use the tool, what is the volume of code changes reviewed per day/week, and what types of defects are most commonly detected?
3. Have you conducted any user studies to evaluate the perceived usefulness and usability of the tool from the developers' perspective? If not, do you plan to conduct such studies in the future?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4