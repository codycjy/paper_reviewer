# Review

## Summary
The paper proposes MAC-CAFE, a framework to iteratively refine knowledge bases based on expert feedback. It uses a multi-actor, centralized critic reinforcement learning approach, where each document is assigned to an actor modeled as a ReACT agent, performing structured edits based on document-specific instructions from a centralized critic. Experimental results show MAC-CAFE improves KB quality and RAG system performance, enhancing accuracy by up to 8% over baselines.

## Soundness
3

## Presentation
2

## Contribution
2

## Strengths
1. The paper addresses a relevant and important problem in RAG systems, focusing on the quality of knowledge bases.
2. The approach is well-motivated and grounded in existing literature, with a clear problem formulation.
3. The proposed MAC-CAFE framework is novel and well-designed, utilizing a multi-actor, centralized critic architecture that leverages reinforcement learning effectively.
4. The paper provides a thorough experimental evaluation across multiple datasets, demonstrating the effectiveness of MAC-CAFE in improving KB quality and RAG system performance.

## Weaknesses
1. The paper could benefit from a more detailed comparison with existing methods, particularly in terms of computational efficiency and scalability.
2. While the paper mentions the limitations of LLMs in handling long contexts, a more in-depth analysis of how these limitations affect MAC-CAFE's performance and potential mitigation strategies would be valuable.
3. The evaluation metrics could be expanded to include more diverse scenarios and tasks to better capture the system's robustness and generalizability.

## Questions
1. How does MAC-CAFE compare to other knowledge base editing methods in terms of computational efficiency and scalability, especially for large-scale KBs?
2. Could you provide more details on how the limitations of LLMs in handling long contexts affect MAC-CAFE's performance? Have you explored any techniques to mitigate these limitations?
3. The paper mentions the use of G-Eval with GPT4-1106-PREVIEW for coherence assessment. How reliable and accurate is this method, and have you explored other evaluation techniques to validate the coherence of edited KBs?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4