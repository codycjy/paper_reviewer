# Review

## Summary
The paper proposes a regularizer for low-rank training that makes the networks more robust to adversarial attacks. The method is based on controlling the condition number of the low-rank components. The authors show the effectiveness of the proposed method on various models and datasets.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper addresses an important problem in the field of deep learning, i.e., the robustness of compressed models.
- The paper is well-written and easy to follow.
- The authors provide a theoretical analysis of the proposed regularizer.

## Weaknesses
- The authors should provide a more detailed discussion of the related work. For instance, they mention that low-rank compression often leads to reduced accuracy, but they do not provide any references.
- The authors should provide a more detailed discussion of the limitations of the proposed method. For instance, they do not discuss whether the method can be applied to NLP tasks.
- The authors should provide a more detailed discussion of the computational complexity of the proposed method. For instance, they do not discuss the training time of the proposed method compared to other low-rank training methods.

## Questions
- Can the proposed method be applied to NLP tasks?
- How does the proposed method compare to other low-rank training methods in terms of training time?
- The authors should provide a more detailed discussion of the robustness of the proposed method to different types of adversarial attacks.
- The authors should provide a more detailed discussion of the interpretability of the proposed method. For instance, they do not discuss whether the low-rank components learned by the proposed method have any semantic meaning.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4