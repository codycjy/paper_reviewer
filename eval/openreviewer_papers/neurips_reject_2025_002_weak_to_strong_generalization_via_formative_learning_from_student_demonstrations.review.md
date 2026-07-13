# Review

## Summary
This paper studies the problem of weak-to-strong (W2S) generalization, where a strong student model learns from a weaker teacher model. The authors propose a method called EVE (Weak Teacher Evaluation of Strong Student Demonstrations) to address the overfitting issue in W2S generalization. EVE regularizes the strong student model towards its own reference policy, rather than the weak teacher's policy. The authors provide theoretical insights into the overfitting problem and present empirical results demonstrating the effectiveness of EVE in improving W2S generalization performance.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper provides a theoretical characterization of the overfitting problem in W2S generalization and presents a novel method to address it.
- The empirical results show that EVE outperforms existing W2S learning approaches and exhibits better robustness under unreliable feedback.

## Weaknesses
- The paper lacks clarity in some sections, particularly in the description of the EVE method and the interpretation of the experimental results.
- The evaluation of the proposed method is limited to two tasks, controlled-summarization and instruction-following. The generalizability of the results to other tasks is not clear.
- The paper does not provide a detailed analysis of the computational efficiency of the proposed method compared to existing approaches.

## Questions
- Can you provide more detailed examples and explanations of how EVE works in practice?
- Can you provide more detailed explanations of the experimental results, including the metrics used and how they relate to the performance of the methods?
- Can you provide a more detailed analysis of the computational efficiency of EVE compared to existing approaches?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4