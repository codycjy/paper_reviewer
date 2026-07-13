# Review

## Summary
This paper presents a novel approach to improving the sample efficiency of reinforcement learning (RL) algorithms through the integration of weight normalization (WN) with batch normalization (BN) within the CrossQ framework. The authors address the challenge of training instability at high update-to-data (UTD) ratios, which is critical for scaling RL methods to real-world applications where data collection is costly or limited. By applying WN to the first two linear layers of CrossQ’s neural networks, the authors aim to stabilize the effective learning rate and mitigate the loss of plasticity that often occurs with increasing UTD ratios. The proposed method is evaluated on 25 complex continuous control tasks from the DeepMind Control Suite and MyoSuite, demonstrating robust performance and scalability without the need for drastic interventions like network resets.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper provides a thorough empirical analysis of CrossQ’s behavior at higher UTD ratios, identifying specific challenges such as rapid weight norm growth and unstable training dynamics. This diagnostic approach offers valuable insights into the limitations of existing methods and sets a solid foundation for the proposed enhancements.

2. The integration of WN with BN is well-motivated and grounded in theoretical principles, particularly the concept of effective learning rate (ELR) stabilization. The authors effectively connect their approach to established theories in neural network optimization, providing a clear rationale for why WN should improve CrossQ’s scalability.

3. The experimental evaluation is comprehensive, covering a diverse set of tasks that include complex environments like humanoid and dog locomotion. The results demonstrate that CrossQ + WN achieves competitive or superior performance compared to state-of-the-art baselines while maintaining simplicity and avoiding the need for drastic interventions like network resets.

## Weaknesses
1. The theoretical justification for WN could be strengthened by more explicitly connecting the empirical observations of weight norm growth to the theoretical implications of scale invariance. 

2. The authors do not thoroughly analyze the potential trade-offs introduced by WN, such as any impact on convergence speed or final performance with very high UTD ratios. 

3. The paper could benefit from a more detailed comparison with other normalization techniques, particularly layer normalization (LN), to better understand the specific advantages of WN in this context.

## Questions
1. The paper would benefit from a more detailed analysis of the computational overhead introduced by WN, particularly in comparison to the baseline CrossQ method. Could the authors provide a quantitative analysis of the additional computational cost incurred by implementing WN, and discuss any potential trade-offs between performance improvement and computational efficiency?

2. The authors should provide a more detailed comparison with other normalization techniques, particularly layer normalization (LN), to better understand the specific advantages of WN in this context. Could the authors include a comparative analysis of BN, WN, and LN in the proposed framework, highlighting the specific benefits of WN in stabilizing training and improving scalability?

3. While the paper demonstrates strong performance on continuous control tasks, it would be valuable to see how the proposed method generalizes to other RL domains such as discrete action spaces or tasks with visual inputs. Could the authors discuss the potential challenges and advantages of applying CrossQ + WN to these different types of tasks, and outline any additional experiments that could help assess its broader applicability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4