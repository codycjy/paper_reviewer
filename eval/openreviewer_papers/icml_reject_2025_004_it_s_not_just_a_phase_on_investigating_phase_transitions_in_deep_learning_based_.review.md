# Review

## Summary
This paper presents a novel approach to side-channel analysis (SCA) by applying mechanistic interpretability (MI) to deep learning-based SCA models. The authors focus on understanding how neural networks learn to exploit side-channel information, particularly during phase transitions in training. By reverse-engineering features learned by the network, they retrieve secret masks, allowing a shift from black-box to white-box evaluations. The paper demonstrates this approach on three common SCA targets (CHES CTF, ESHARD, and ASCAD) and provides insights into the specific physical leakage exploited by neural networks.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper addresses a critical gap in the field of SCA by providing a mechanistic understanding of how deep learning models exploit side-channel information. This is crucial for developing more robust security evaluations and countermeasures.
2. The authors successfully retrieve secret masks and demonstrate the feasibility of moving from black-box to white-box evaluations, which has significant implications for improving the security of cryptographic implementations.
3. The paper provides detailed insights into the specific physical leakage exploited by neural networks, which can guide the design of more secure devices and algorithms.

## Weaknesses
1. The paper assumes that the attack has already succeeded and focuses on understanding the model's behavior after a successful attack. This assumption limits the practical applicability of the results, as it does not address the challenges of actually executing a successful attack. The authors should consider the entire attack process and how the proposed methods can be used to improve the attack's effectiveness and efficiency.
2. The authors should consider the impact of different leakage models on the results. Different devices may exhibit different leakage behaviors, and the paper should discuss how the proposed methods can handle variations in leakage models.
3. The paper focuses on a specific type of AES cipher and masking scheme. The authors should consider the generalizability of their results to other algorithms and different masking schemes.

## Questions
1. How can the proposed methods be extended to other types of cryptographic algorithms beyond AES?
2. How can the proposed methods handle variations in leakage models due to different devices?
3. Can the authors provide more details on the potential impact of their findings on the security of real-world devices and the development of more secure cryptographic implementations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4