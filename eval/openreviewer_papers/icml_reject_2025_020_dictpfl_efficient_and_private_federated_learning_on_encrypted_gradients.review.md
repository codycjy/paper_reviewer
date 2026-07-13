# Review

## Summary
This paper presents DictPFL, a novel framework for efficient and privacy-preserving federated learning (FL) using homomorphic encryption (HE). The framework introduces two key modules, Decompose-for-Partial-Encrypt (DePE) and Prune-for-Minimum-Encrypt (PrME), to address the communication and computational overheads associated with HE in FL. DePE decomposes model weights into a static dictionary and a trainable lookup table, while PrME optimizes this further by pruning the lookup table parameters based on a shared gradient history across clients. The authors demonstrate that DictPFL significantly reduces communication overhead and speeds up training compared to fully encrypted and selectively encrypted methods, while maintaining privacy guarantees.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The combination of DePE and PrME is novel and addresses the dual challenges of efficiency and privacy in HE-based FL.
2. The paper provides extensive experimental results across multiple datasets and models, demonstrating the effectiveness of DictPFL in various settings.
3. The authors conduct thorough ablation studies to analyze the impact of different hyperparameters, which is valuable for practical implementation.

## Weaknesses
1. The paper does not provide sufficient details on how the dictionary D is initialized and updated. More information is needed on how the static dictionary is created and whether it needs to be updated during training.
2. The paper lacks a formal security analysis or proof to support the privacy claims. A more rigorous treatment of the security guarantees, possibly including a threat model and security proofs, would strengthen the paper.
3. The paper does not discuss the potential for a "dictionary attack" where an adversary reconstructs the static dictionary D, which could compromise privacy.

## Questions
1. How is the static dictionary D initialized and updated during training? Does it need to be transmitted between clients and the server?
2. How does the framework handle the potential for a dictionary attack where an adversary attempts to reconstruct the static dictionary D?
3. What are the specific HE scheme and cryptographic parameters used in the implementation? Are these parameters sufficient to provide 128-bit security as claimed?
4. How does the framework handle client dropout or asynchronous participation, which is common in FL? Does this affect the pruning consistency?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4