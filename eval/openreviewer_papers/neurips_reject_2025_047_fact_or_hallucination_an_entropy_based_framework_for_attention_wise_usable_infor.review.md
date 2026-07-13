# Review

## Summary
This paper proposes Shapley NEAR, a method for hallucination detection in LLMs. The method is based on the NEAR score, which is calculated by summing the information gain across all attention heads and layers in the LLM. Information gain is calculated as the difference in entropy with and without the context. The NEAR score is then averaged using Shapley values to account for the contribution of each individual sentence. The paper demonstrates that this method outperforms existing baselines on multiple QA datasets using three different LLMs. The authors also conduct ablation studies to show that all layers and attention heads contribute to the NEAR score, and that the method can detect both parametric and context-induced hallucinations.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and the experimental setup.
- The proposed method is novel and theoretically grounded, providing a principled approach to hallucination detection in LLMs.
- The paper demonstrates the effectiveness of Shapley NEAR on multiple QA datasets using three different LLMs, outperforming existing baselines.
- The authors conduct thorough ablation studies to analyze the contribution of each component of the proposed method, providing insights into the importance of considering all layers and attention heads.

## Weaknesses
- The paper focuses exclusively on QA tasks, and it is unclear how well the proposed method generalizes to other types of text generation tasks, such as summarization or dialogue systems.
- While the paper compares Shapley NEAR to several existing baselines, it does not compare to some of the latest methods in hallucination detection, such as those based on mechanistic interpretability or advanced uncertainty quantification techniques.
- The paper does not provide a detailed analysis of the computational complexity or runtime of the proposed method, which could be a limitation for practical applications.
- The paper could benefit from a more detailed analysis of the failure cases or scenarios where Shapley NEAR may not perform well, which could provide insights for future research.

## Questions
- Have you considered how Shapley NEAR could be adapted or extended to work with other types of text generation tasks, such as summarization or dialogue systems?
- Have you compared Shapley NEAR to any of the latest methods in hallucination detection, such as those based on mechanistic interpretability or advanced uncertainty quantification techniques?
- Can you provide more details on the computational complexity and runtime of Shapley NEAR, and how it compares to the baselines you considered?
- Can you provide a more detailed analysis of the failure cases or scenarios where Shapley NEAR may not perform well, and what insights this may provide for future research?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4