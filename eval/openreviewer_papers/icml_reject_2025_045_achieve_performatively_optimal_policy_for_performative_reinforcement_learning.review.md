# Review

## Summary
The paper proposes a novel zeroth-order performative policy gradient (0-PPG) algorithm designed to achieve performatively optimal (PO) policies in performative reinforcement learning (RL) settings where the environment dynamics change in response to the deployed policy. The authors build on the framework introduced by [1], which only guarantees convergence to a performatively stable (PS) policy, by introducing a negative entropy regularizer in the value function. This regularizer allows the authors to derive new properties of the performative value function, including gradient dominance and a policy lower bound, which ultimately lead to the development of an algorithm capable of achieving global optimality. The theoretical contributions are supported by rigorous mathematical proofs and discussions that clarify the assumptions and limitations of the proposed approach.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper introduces a novel approach to performative RL by focusing on achieving performatively optimal policies, which go beyond the performatively stable policies previously addressed.
- The authors provide a comprehensive set of theoretical results, including gradient dominance and a policy lower bound, which are crucial for understanding the properties of the performative value function in the presence of an entropy regularizer.
- The 0-PPG algorithm proposed in the paper is a creative combination of existing ideas in RL and zeroth-order optimization, adapted to the specific challenges of performative RL.
- The work has significant implications for the field of performative RL, as it pushes beyond the existing state-of-the-art by offering a method to achieve global optimality.

## Weaknesses
- The paper does not provide empirical evaluations of the proposed 0-PPG algorithm. While the theoretical contributions are significant, empirical validation would strengthen the claims and demonstrate the practical effectiveness of the algorithm in achieving performatively optimal policies.
- The paper lacks a discussion of the limitations of the proposed approach. It would be beneficial to address any potential challenges or scenarios where the 0-PPG algorithm may not perform optimally, providing insights for future research and potential avenues for improvement.

## Questions
- Could you provide empirical results or simulations that demonstrate the performance of the 0-PPG algorithm in practice? This would help validate the theoretical claims and illustrate the algorithm's effectiveness in achieving performatively optimal policies.
- Can you discuss any potential limitations or challenges of the 0-PPG algorithm? Are there specific scenarios where the algorithm may not perform optimally, or particular environments where it may struggle compared to other approaches?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4