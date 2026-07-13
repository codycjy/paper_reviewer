# Review

## Summary
This paper explores the interplay between adversarial robustness and watermarking within machine learning models. The authors propose a formal framework that connects these two concepts, suggesting that for any given learning task, one of three scenarios must hold: a watermarking scheme is effective, the model is adversarially robust, or a transferable attack exists. They provide a construction demonstrating the existence of transferable attacks and show that such attacks are equivalent to the cryptographic primitive of pseudorandom generation.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper is well-organized and clearly written, with rigorous definitions and theorems that are accessible and engaging. The authors present a compelling and novel connection between adversarial robustness and watermarking, supported by well-crafted examples that clarify the theoretical points. The formal results are particularly intriguing, as they offer a fresh perspective on the relationship between cryptography and adversarial robustness.

## Weaknesses
The paper’s primary limitation lies in its lack of a concrete application to modern machine learning models. The authors focus on formal results, but the implications for practical implementations of watermarking and adversarial defenses remain unclear. For example, while the authors suggest that transferable attacks might be challenging to execute in real-world settings, they do not provide sufficient evidence or discussion to support this claim. This leaves the paper’s relevance to practical AI security unaddressed, which could be crucial for applications in security and privacy.

## Questions
1. How do the authors envision their results being applied to real-world scenarios involving modern machine learning models? Are there specific use cases where the proposed framework could be particularly relevant?

2. The paper mentions that transferable attacks might be difficult to implement in practice. Could the authors elaborate on this point? What challenges do they anticipate, and how might these impact the practical application of their findings?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4