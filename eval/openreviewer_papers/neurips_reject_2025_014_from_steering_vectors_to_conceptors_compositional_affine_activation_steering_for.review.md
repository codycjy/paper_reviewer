# Review

## Summary
The paper introduces a framework combining conceptor theory with activation steering to control and understand the internal representations of large language models (LLMs). Using conceptors as soft projection matrices, the authors derive optimal steering functions and demonstrate their method's effectiveness through experiments on in-context learning tasks and alignment-related behaviors. The paper also explores compositional steering using Boolean operations over conceptors, showing improved performance compared to traditional vector combination methods.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper provides a solid theoretical foundation for the proposed framework, detailing the principles and deriving optimal steering functions.
2. The paper introduces a novel approach to activation steering by incorporating conceptor theory, offering a new perspective on controlling LLMs.
3. The paper demonstrates the effectiveness of the framework through experiments on various tasks and models, showcasing its practical applicability.

## Weaknesses
1. The paper lacks a comprehensive comparison with a broader range of existing methods, which could provide a more complete picture of the framework's relative performance.
2. The paper does not discuss the scalability of the proposed method to larger models or datasets, which is crucial for assessing its practical utility.
3. The paper does not provide a detailed analysis of the computational resources required for implementing the framework, which could be a significant limitation for practical applications.

## Questions
1. How does the proposed framework perform compared to other state-of-the-art methods in controlling LLMs, beyond the additive steering baseline?
2. Can the authors provide more insights into the scalability of their method to larger models and datasets? Have they tested the framework on more complex tasks or datasets?
3. What are the computational resource requirements for implementing the proposed framework, and how do they compare to existing methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4