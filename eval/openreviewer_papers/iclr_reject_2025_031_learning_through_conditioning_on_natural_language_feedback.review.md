# Review

## Summary
This paper explores learning from natural language feedback by allowing models to condition their responses on feedback from larger frontier models. The authors propose a framework where smaller instruction-tuned models can learn from the feedback provided by more capable models, aiming to improve the models' performance on various tasks. The paper also addresses the challenges faced by smaller models in effectively utilizing this feedback due to noise in their generative output. Techniques such as negative sampling are incorporated to enhance the learning process. The findings suggest that models trained with feedback-conditioned responses perform similarly to those trained directly on teacher responses, indicating the potential of this approach in leveraging the linguistic capabilities of language models for instructive learning.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The idea of learning from natural language feedback is interesting and has the potential to improve the performance of smaller models.

## Weaknesses
1. The paper lacks a clear comparison with existing methods, making it difficult to assess the relative advantages of the proposed approach. Including comparisons with other learning techniques or providing a more detailed analysis of the benefits of feedback conditioning over other methods would strengthen the paper.
2. The authors do not provide a detailed analysis of the computational costs associated with their approach. Given that the method involves conditioning on feedback from larger models, there may be significant computational overheads. Discussing the trade-offs between performance improvements and computational costs would be valuable.
3. The paper does not thoroughly explore the potential limitations of the proposed method. For example, the authors do not discuss the impact of noisy or incorrect feedback from the teacher model on the learning process. Addressing these limitations and providing strategies to mitigate their effects would enhance the robustness of the approach.

## Questions
1. How does the proposed feedback-conditioning approach compare to other learning techniques in terms of performance and computational efficiency?
2. Can the authors provide more details on the computational costs associated with their approach, and how these costs compare to other methods?
3. How does the quality of feedback from the teacher model impact the learning process? Have the authors explored the effects of noisy or incorrect feedback, and if so, how have they addressed these issues?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4