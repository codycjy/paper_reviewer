# Review

## Summary
This paper proposes a method to generate adversarial examples using counterfactual explanations. The approach aims to enhance the privacy of robust models by minimizing the generalization gap between adversarial and original examples. The authors evaluate their method on the MNIST dataset, comparing it to traditional adversarial example generation techniques.

## Soundness
1

## Presentation
1

## Contribution
2

## Strengths
The paper addresses an important challenge in machine learning security by exploring the connection between adversarial robustness and privacy.

## Weaknesses
- The paper's structure is disorganized, with an excessive focus on background information and a lack of clarity in presenting the proposed method. This makes it difficult for readers to understand the technical details and novelty of the approach.
- The experimental evaluation is limited to the MNIST dataset, which is a simple, low-resolution image classification task. This raises questions about the generalizability of the proposed method to more complex, real-world scenarios.
- The paper lacks ablation studies to validate the contribution of each component in the proposed method. This makes it unclear which aspects of the approach are effective and which are not.
- The paper does not provide any visual examples of the generated adversarial examples, which would help readers understand the practical implications of the proposed method.
- The paper's writing contains numerous grammatical errors, awkward phrasing, and unclear explanations, making it difficult to follow the arguments and methodology.

## Questions
- How does the proposed method perform on more complex datasets beyond MNIST?
- Can the authors provide more detailed ablation studies to validate the effectiveness of each component?
- Why were no visual examples of the generated adversarial examples provided?
- Can the authors clarify the novelty of their approach compared to existing methods that use counterfactual explanations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
1

## Confidence
5