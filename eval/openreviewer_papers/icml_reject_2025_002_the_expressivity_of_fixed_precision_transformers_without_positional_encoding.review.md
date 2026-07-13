# Review

## Summary
The paper investigates the expressivity of Transformers when constrained by fixed-precision float arithmetic, specific assumptions about query-key parameters, and the presence or absence of positional encoding. The authors find that under these constraints, Transformers are limited to recognizing finite or co-finite languages, a proper subclass of regular languages. The study highlights the gap between theoretical models and practical implementations, suggesting that real-world Transformers function more like efficient lookup tables.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-organized, with a clear presentation of the problem, methodology, and findings. The logical flow and use of technical terms are appropriate for the audience.
2. The paper addresses an important gap in the literature by focusing on the practical constraints of Transformer models, which are often overlooked in theoretical studies.
3. The findings have practical implications for the design and implementation of Transformer models in real-world applications.

## Weaknesses
1. The paper could benefit from a more detailed discussion of the practical implications of the findings, including potential limitations and challenges in applying the results to real-world scenarios.
2. The paper does not provide a comprehensive comparison with existing methods or approaches, which could strengthen the argument for the proposed method.
3. The paper could benefit from a more detailed discussion of the limitations of the study, including the assumptions made and the potential impact on the generalizability of the findings.

## Questions
1. How do the findings of this study compare to existing research on the expressivity of Transformers? Are the results consistent with previous findings, or do they provide new insights?
2. What are the practical implications of the findings, and how can they be applied in real-world scenarios? Are there any potential challenges or limitations to implementing the proposed approach?
3. How generalizable are the findings of the study? Are there any assumptions made that could limit the applicability of the results to other contexts or scenarios?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4