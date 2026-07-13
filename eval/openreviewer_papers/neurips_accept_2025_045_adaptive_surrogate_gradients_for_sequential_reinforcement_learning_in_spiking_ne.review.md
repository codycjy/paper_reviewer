# Review

## Summary
This paper addresses two key challenges in applying Spiking Neural Networks (SNNs) to complex control tasks in energy-constrained robotics. The first challenge is the non-differentiability of spiking neurons, which necessitates surrogate gradients with unclear optimization properties. The second challenge is the stateful dynamics of SNNs, which require training on sequences, but are hindered by limited sequence lengths during the early training phase, preventing the network from bridging its warm-up period. To tackle these issues, the authors conduct a systematic analysis of surrogate gradient slope settings, revealing that shallower slopes increase gradient magnitude in deeper layers but reduce alignment with true gradients. In the context of reinforcement learning, they find no clear preference for fixed or scheduled slopes. However, in reinforcement learning, shallower slopes or scheduled slopes lead to a 2.1 times improvement in both training and final deployed performance. Building on these insights, the authors propose a novel training approach that leverages a privileged guiding policy to bootstrap the learning process while still exploiting online environment interactions with the spiking policy. When applied to a real-world drone position control task, this method achieves an average return of 400 points, significantly outperforming previous techniques such as Behavioral Cloning and TD3BC, which achieved at most -200 points under the same conditions. This research advances both the theoretical understanding of surrogate gradient learning in SNNs and the development of practical training methodologies for neuromorphic controllers in real-world robotic systems.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper demonstrates a high level of originality by addressing the non-differentiability of spiking neurons and the sequence length limitation in SNNs for reinforcement learning. It introduces a novel training approach that uses a privileged guiding policy to bootstrap the learning process while still allowing online environment interactions with the spiking policy. The quality of the research is evident in the systematic analysis of surrogate gradient slope settings and the subsequent development of an adaptive slope schedule. The paper is clearly written and well-structured, making it easy to follow the authors' thought process and methodology. The significance of the work lies in its potential impact on energy-constrained robotics, offering a promising solution that could revolutionize efficiency and enable native temporal processing.

## Weaknesses
The paper could benefit from a more detailed comparison with existing methods, including a clear discussion of the advantages and limitations of the proposed approach compared to other state-of-the-art techniques. While the experimental results are impressive, it would be valuable to see more extensive validation across a wider range of tasks and environments to demonstrate the generalizability of the method. Additionally, the theoretical analysis could be further strengthened by providing a more rigorous mathematical foundation for the adaptive slope scheduling approach.

## Questions
The paper is well-written and presents a novel approach to addressing challenges in Spiking Neural Networks for reinforcement learning. However, to further strengthen the contribution, the authors could provide more detailed comparisons with existing methods, including a clear discussion of the advantages and limitations of the proposed approach. Additionally, validating the method across a wider range of tasks and environments would enhance the generalizability of the results. Lastly, providing a more rigorous mathematical foundation for the adaptive slope scheduling approach would add depth to the theoretical analysis. With these enhancements, the paper would present a more comprehensive and impactful contribution to the field.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4