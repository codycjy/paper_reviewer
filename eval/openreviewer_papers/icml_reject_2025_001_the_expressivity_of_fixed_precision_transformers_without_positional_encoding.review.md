# Review

## Summary
The paper investigates the expressivity of fixed-precision Transformers, particularly focusing on their capability to recognize formal languages under various constraints. It makes two main contributions: (1) It demonstrates that Transformers, operating under fixed-precision arithmetic, finite decoding steps, and without positional encoding, are limited to recognizing only finite or co-finite languages. (2) It shows that with fixed-precision arithmetic and absolute positional encoding, Transformers can recognize any cyclic language. These findings highlight the fundamental limitations imposed by fixed-precision arithmetic and suggest that practical Transformers may be essentially restricted to recognizing finite languages, functioning more like efficient lookup tables.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow. 
- The topic of studying the expressivity of Transformers is interesting and relevant to the community.
- The authors provide rigorous proofs to support their theoretical findings.

## Weaknesses
- The paper makes a strong assumption that the Transformer operates under fixed-precision floating-point arithmetic, which is not always the case in practice. 
- The authors provide no experiments to support their theoretical findings.
- The paper does not discuss how the fixed-precision assumption affects the Transformer's performance on real-world tasks, such as language modeling or machine translation.
- The paper does not provide any practical guidance on how to overcome the limitations imposed by fixed-precision arithmetic.

## Questions
- How do the authors' findings on the limited expressivity of fixed-precision Transformers relate to the practical successes of Transformers in real-world applications, such as language modeling and machine translation?
- Can the authors provide any experimental results to support their theoretical findings?
- Are there any practical implications of the authors' findings for the design and implementation of Transformer models in practical applications?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4