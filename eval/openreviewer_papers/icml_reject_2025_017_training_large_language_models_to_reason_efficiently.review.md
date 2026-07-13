# Review

## Summary
The paper proposes a method to make reasoning models more efficient at inference time by training them to produce shorter chains of thought. The authors use reinforcement learning to train models to balance between accuracy and inference cost, so they produce the minimum number of tokens needed to solve a problem correctly. The key idea is to penalize the length of correct responses in the reinforcement learning objective. The authors evaluate their approach on math datasets, showing that it reduces inference costs by 16-50% while maintaining accuracy. The method allows adjusting a hyperparameter to trade-off between efficiency and performance. The authors also discuss related methods for improving reasoning capabilities of LLMs.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is clearly written, with a logical flow and well-defined methodology. The authors provide detailed explanations of their approach and the experimental setup.
2. The method allows deriving a family of reasoning models with different efficiency levels by adjusting a single hyperparameter. This is useful for applications with varying computational budgets.
3. The experiments on math datasets demonstrate substantial reductions in inference costs while maintaining accuracy. The results show a clear trade-off between efficiency and performance, which can be controlled via the hyperparameter.

## Weaknesses
1. The method is evaluated on math datasets only. It's unclear how well it generalizes to other reasoning tasks. The authors should explore other types of reasoning tasks, such as logical reasoning, commonsense reasoning, or complex decision-making tasks, to demonstrate the broader applicability of their approach.

2. The evaluation focuses on token count as the efficiency metric. While token count is an important aspect of inference cost, it doesn't capture the entire picture. The authors should consider other efficiency metrics like memory usage, latency, or throughput. Additionally, the paper lacks a comprehensive analysis of the trade-off between efficiency and accuracy across different types of problems.

3. The paper lacks a rigorous analysis of the method's limitations. The authors should provide a more detailed discussion of the scenarios where their approach might not be suitable, such as problems requiring extensive reasoning or creative problem-solving. This would help set more accurate expectations for the method's capabilities.

## Questions
1. How well does the method generalize to other types of reasoning tasks beyond math, such as logical reasoning, commonsense reasoning, or complex decision-making tasks?

2. The evaluation focuses on token count as the efficiency metric. How does the method perform when considering other efficiency metrics like memory usage, latency, or throughput?

3. How does the trade-off between efficiency and accuracy vary across different types of problems? Is the reduction in inference cost uniform across all problem types?

4. What are the limitations of the proposed approach? Are there certain types of problems or scenarios where the method might not be suitable or effective?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4