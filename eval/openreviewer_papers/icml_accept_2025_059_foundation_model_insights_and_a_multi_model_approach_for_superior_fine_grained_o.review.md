# Review

## Summary
This paper presents an in-depth analysis of the effectiveness of foundation models (FMs) compared to traditional pre-trained models for subset selection tasks. It demonstrates that FMs consistently outperform traditional models on fine-grained datasets but show limited advantages on coarse-grained datasets with noisy labels. Additionally, the paper introduces a novel pipeline that leverages multiple FMs with unknown selection performance as information extractors, leading to the proposal of the RAM-APL method. Extensive experiments on fine-grained datasets, including Oxford-IIIT Pet, Food-101, and Caltech-UCSD Birds-200-2011, show that RAM-APL achieves state-of-the-art performance.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The analysis of FMs versus traditional IEs on fine-grained and coarse-grained datasets is thorough and provides valuable insights.
3. The proposed pipeline effectively addresses the limitations of traditional methods by leveraging the complementary strengths of multiple FMs.
4. The experimental results are comprehensive, covering various datasets and sampling rates, and demonstrate the effectiveness of the proposed method.

## Weaknesses
1. The paper primarily focuses on image classification tasks. It would be beneficial to explore the applicability of the proposed method to other data modalities, such as text or audio.
2. The proposed method involves multiple FMs, which may increase computational costs compared to traditional methods. A more detailed analysis of the computational efficiency and scalability of the proposed method would be helpful.
3. The paper could provide more insights into the selection of hyperparameters α and β in Equation 8 and their impact on the performance of the method.

## Questions
1. Can the proposed method be applied to other data modalities, such as text or audio?
2. How does the computational cost of the proposed method compare to traditional methods, especially when using multiple FMs?
3. What are the considerations for selecting hyperparameters α and β, and how sensitive is the method to these choices?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4