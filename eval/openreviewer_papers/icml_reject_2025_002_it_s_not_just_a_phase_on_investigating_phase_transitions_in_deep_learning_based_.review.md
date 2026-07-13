# Review

## Summary
This paper explores the application of mechanistic interpretability (MI) in side-channel analysis (SCA), particularly focusing on deep learning-based approaches. The authors reverse engineer features learned by neural networks during phase transitions, aiming to understand how these models exploit side-channel information to recover secret data. They propose a method to move from black-box to white-box evaluations by retrieving secret masks from model outputs. The study investigates the behavior of neural networks trained on side-channel data, even without access to masking randomness, and provides insights into the specific physical leakage exploited by these models.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper presents a novel application of mechanistic interpretability in the challenging context of side-channel analysis, which is not commonly explored.
2. The authors provide a clear methodology for understanding how neural networks learn to exploit side-channel information, which can be valuable for both attack and defense strategies in SCA.
3. The study offers insights into the phase transition behavior of neural networks in SCA, contributing to a deeper understanding of model training dynamics.

## Weaknesses
1. The paper lacks a thorough comparison with existing methods, making it difficult to assess the novelty and effectiveness of the proposed approach.
2. The methodology assumes that the attack has already succeeded and focuses on understanding the model's behavior rather than improving attack performance or developing more effective countermeasures.
3. The paper does not provide a detailed analysis of the computational complexity or scalability of the proposed method, which could be a limitation for practical applications.

## Questions
1. How does the proposed MI approach compare with other interpretability methods or even non-interpretability-based approaches in the context of SCA?
2. Can the insights gained from understanding how the model learns to exploit side-channel information be used to develop more effective countermeasures or improve the security of cryptographic implementations?
3. What are the computational requirements and scalability of the proposed method, especially when applied to more complex SCA scenarios or larger datasets?
4. How does the approach handle variations in the quality and complexity of side-channel data, and what are the implications for its robustness and reliability?
5. Are there any potential biases or limitations in the methodology that could affect the generalizability of the findings, and how are these addressed?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4