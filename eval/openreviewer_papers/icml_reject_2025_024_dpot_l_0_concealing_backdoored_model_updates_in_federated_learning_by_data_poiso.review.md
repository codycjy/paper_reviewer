# Review

## Summary
This paper proposes a new backdoor attack, DP OTL0, which relies solely on data poisoning to inject backdoors into the global model. Unlike traditional static backdoor triggers, DP OTL0 dynamically optimizes the trigger pattern each round, ensuring that the malicious model updates closely resemble benign updates and thus evade detection. The authors demonstrate that DP OTL0 effectively bypasses state-of-the-art defenses across multiple datasets and model architectures.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. This paper proposes a new backdoor attack that relies solely on data poisoning, eliminating the need for model manipulation, which is more practical.

2. The paper provides a theoretical analysis of the attack.

3. The authors evaluate their method against a wide range of defenses.

## Weaknesses
1. The paper does not compare DP OTL0 with other advanced backdoor attacks, such as A3FL, which also optimizes triggers to bypass defenses.

2. DP OTL0 requires clients to have white-box access to the global model, which may not be feasible in real-world scenarios where model privacy is protected.

3. The paper does not discuss the scalability of the attack as the number of clients increases.

4. The paper does not evaluate the attack's performance when clients have heterogeneous data, which is a common scenario in federated learning.

## Questions
1. How does DP OTL0 compare to other advanced backdoor attacks, such as A3FL, in terms of attack effectiveness and efficiency?

2. How does the optimization process of DP OTL0 affect the convergence speed of the global model?

3. How does the performance of DP OTL0 degrade as the number of clients increases?

4. How does the performance of DP OTL0 degrade as the data heterogeneity among clients increases?

5. How can DP OTL0 be adapted to scenarios where clients have limited computational resources?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4