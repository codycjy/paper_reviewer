# Review

## Summary
The paper investigates the scaling behavior of LLMs when tackling tasks with multiple attempts, finding that the negative log of the average success rate follows a power law with the number of attempts. It presents a mathematical analysis explaining why this scaling emerges, suggesting that it arises from the distribution of single-attempt success probabilities having a heavy left tail. This distributional approach not only explains the observed power law but also offers a more accurate method for predicting the scaling exponent, reducing computational costs. The paper contributes to the understanding of LLM performance as inference compute is scaled up.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper provides a rigorous mathematical framework to explain the power law scaling observed in LLMs when tackling tasks with multiple attempts. By analyzing the distribution of single-attempt success probabilities, the authors offer a clear explanation for the emergence of this scaling behavior. The paper also proposes a more efficient method for predicting the power law exponent, which could be valuable for practical applications. Additionally, the work contributes to our understanding of how LLM performance improves with inference compute, which is crucial for the deployment and scaling of these models.

## Weaknesses
The paper primarily focuses on mathematical analysis and empirical validation of known scaling behaviors. While this provides valuable insights into the observed phenomena, it may not introduce fundamentally new concepts or approaches. Additionally, the analysis is based on certain assumptions about the distribution of single-attempt success probabilities, which may not hold in all practical scenarios. The paper could benefit from more extensive empirical studies across a wider range of tasks and models to further validate the proposed explanations. Moreover, the mathematical derivations, while thorough, may be dense and difficult for some readers to follow.

## Questions
- Can the authors provide more empirical evidence to support the assumptions made about the distribution of single-attempt success probabilities? How robust are the findings to violations of these assumptions in practical scenarios?
- How generalizable are the proposed methods and findings to other types of tasks and models not covered in the paper? Have the authors considered testing the approach on different domains?
- What are the practical implications of the predicted power law exponents on the design and deployment of LLMs? How can the proposed methods help organizations make informed trade-offs between model size, inference costs, and performance targets?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4