# Review

## Summary
This paper introduces formal definitions for watermarking and adversarial defense algorithms, then proves that for any learning task, at least one of the following three conditions holds: (1) there exists a watermarking algorithm, (2) there exists a robustness algorithm, or (3) there exists a transferable attack. The authors then provide instantiations of each of these three conditions, and show that condition (3) implies the existence of a cryptographic primitive.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
- The paper is clearly written, with the main theorem and its proof sketch presented in an accessible way. The proofs in the appendix are also clearly written.
- The paper initiates the formal study of the relationship between watermarking and adversarial robustness.

## Weaknesses
- The paper lacks a conclusion section. It would be good to include some discussion of the implications of the main theorem and the constructions in the paper.
- The paper does not include any experiments. While this is a theoretical paper, it would be helpful to include some empirical results to demonstrate the effectiveness of the constructions in the paper.
- The paper does not provide any new practical algorithms. While the paper proves the existence of various algorithms, it does not provide explicit algorithms or pseudocode for implementing them. This makes it difficult for practitioners to apply the results of the paper in practical scenarios.

## Questions
- The paper states that the purpose of the watermark is to detect whether a model was trained using a stolen copy of the original model. However, in practice, watermarking algorithms are often used for other purposes, such as detecting whether a model was trained on human-generated data or AI-generated data. How do the results of this paper apply to these alternative uses of watermarking?
- The paper focuses on formalizing the relationship between watermarking and adversarial robustness. What are the implications of the main theorem for the practice of AI safety? How can the results of this paper inform the development of more robust and secure AI systems?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4