# Review

## Summary
This paper proposes a method for model editing, including pruning and unlearning, in the data-free regime. The authors introduce the concept of HiFi components, which are identified using a proposed RowSum heuristic and are crucial for predicting the model's output. They develop the CoBRA framework, which leverages HiFi components and BNFix to either retain or discard these components, restoring model performance without retraining. The proposed method achieves substantial reductions in FLOPs and parameters while maintaining accuracy.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper addresses a challenging problem in model editing, focusing on the data-free regime, which is less explored compared to scenarios with access to training data and loss functions.
2. The introduction of HiFi components and the RowSum heuristic provides a novel perspective on identifying important model components for predictions.
3. The paper provides a theoretical analysis of the impact of batch normalization parameters on loss function, leading to the development of BNFix for accuracy recovery.
4. The CoBRA framework is versatile, supporting both pruning and unlearning tasks, and demonstrates effectiveness across different datasets and architectures.

## Weaknesses
1. The method relies on distributional access to data, which may not always be practical. The authors could discuss alternative approaches or the feasibility of applying their method to models without batch normalization.
2. While BNFix is proposed as an alternative to retraining, its effectiveness may vary depending on the extent of model editing. More extensive experiments on larger models or more complex datasets could strengthen the claims.
3. The paper could benefit from a more detailed discussion of the computational costs associated with identifying HiFi components and applying BNFix, particularly for large-scale models.
4. The evaluation focuses on ResNet and VGG architectures. Including experiments on more recent architectures, such as Vision Transformers, would enhance the generalizability of the findings.

## Questions
1. How sensitive is the identification of HiFi components to the choice of distributional samples? Could the authors provide more insights or guidelines on selecting these samples?
2. Can the proposed method be extended to models without batch normalization or with different normalization techniques? If so, what modifications would be necessary?
3. How does the computational complexity of the proposed method compare to existing pruning and unlearning techniques, especially those requiring retraining?
4. The paper mentions that the method is effective when the number of classes is less than the width of the network. Could the authors elaborate on this limitation and potential strategies to mitigate it?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4