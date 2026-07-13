# Review

## Summary
The paper introduces CoBRA, a method for model editing that includes pruning and unlearning, which is the process of forgetting specific classes. The authors aim to address the challenge of editing models without access to training data or loss functions, which is a common scenario in real-world applications. CoBRA is based on the concept of HiFi components, which are identified using a heuristic called RowSum. The authors provide a theoretical analysis of the impact of batch normalization on the loss function during inference, leading to the development of BNFix, an algorithm to restore accuracy after editing. The experimental results demonstrate the effectiveness of CoBRA in achieving significant reductions in model parameters and FLOPS while maintaining performance.

## Soundness
3

## Presentation
2

## Contribution
3

## Strengths
The paper introduces a novel approach to model editing that does not require access to training data or loss functions, addressing a significant challenge in the field. The concept of HiFi components and the RowSum heuristic provide a new perspective on identifying important parts of the model. The theoretical analysis of batch normalization is a valuable contribution, offering insights into its role in the loss function during inference. The proposed CoBRA framework is versatile, encompassing both pruning and unlearning, making it applicable to a wide range of model editing tasks. The experimental results are impressive, showing substantial reductions in model size and computational complexity while maintaining performance. The method's ability to handle complex interconnections in neural networks, such as skip connections in ResNets, is a significant advantage.

## Weaknesses
The paper lacks a detailed discussion of the computational complexity of the proposed methods. While the experimental results demonstrate the effectiveness of CoBRA, the paper does not provide a comprehensive analysis of the time and memory requirements of the proposed algorithms. This information is crucial for assessing the practicality of the methods, especially for large-scale applications. The comparison with existing methods is limited to a few baselines. The paper could benefit from a more extensive comparison with a broader range of state-of-the-art methods in model editing and unlearning. This would provide a clearer picture of the advantages and limitations of CoBRA in relation to existing approaches. The experiments are primarily conducted on CIFAR-10 and CIFAR-100 datasets. While these datasets are commonly used, the generalizability of the results to other datasets and real-world scenarios is not fully explored. The paper could benefit from experiments on a more diverse set of datasets to demonstrate the robustness and applicability of CoBRA.

## Questions
The paper could benefit from a more detailed discussion of the limitations of the proposed methods, including the assumptions and constraints that may affect their applicability in real-world scenarios. The comparison with existing methods could be expanded to include a broader range of state-of-the-art techniques in model editing and unlearning. This would provide a more comprehensive evaluation of the proposed methods and highlight their advantages and limitations in relation to existing approaches. The experiments could be extended to include a more diverse set of datasets to demonstrate the robustness and generalizability of the proposed methods. Additionally, the paper could provide a more detailed analysis of the computational complexity and resource requirements of the proposed methods, which is crucial for assessing their practicality in large-scale applications.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4