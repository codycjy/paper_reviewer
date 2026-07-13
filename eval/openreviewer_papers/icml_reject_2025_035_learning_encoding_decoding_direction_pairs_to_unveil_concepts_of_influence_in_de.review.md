# Review

## Summary
This paper presents a method to identify important concepts in a deep neural network by learning encoding-decoding direction pairs in the network's latent space. The authors propose to learn these direction pairs in an unsupervised manner, extending previous work on concept activation vectors (CAVs) and pattern CAVs. The paper evaluates the method on synthetic data and the final convolutional layer of a ResNet18 trained on Places365, demonstrating its effectiveness in identifying meaningful concepts.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper tackles an important problem in explainability: identifying concepts that influence the predictions of a neural network. This is a crucial step towards understanding and improving deep learning models.
- The paper builds on top of previous work, extending the concept of CAVs to an unsupervised setting. This is a promising direction, as supervised methods are often not feasible in practice.
- The paper includes a detailed evaluation of the method on synthetic data and a real-world dataset (Places365). The results demonstrate the effectiveness of the method in identifying meaningful concepts.

## Weaknesses
- The paper's main contribution is the identification of concepts in an unsupervised manner. However, it is unclear how this approach compares to existing methods for concept-based explanations, such as those based on concept activation vectors (CAVs) or their extensions. A more thorough comparison to these methods would help to better understand the advantages and limitations of the proposed approach.
- The paper evaluates the method on a single network (ResNet18) and a single dataset (Places365). It would be valuable to see how the method generalizes to other networks and datasets, especially larger-scale datasets such as ImageNet.
- The paper does not include a user study to evaluate the usefulness of the identified concepts from the perspective of a human interpreter. This would provide valuable insights into the practical utility of the method.

## Questions
- How does the proposed unsupervised method compare to existing concept-based explanation methods, such as CAVs or pattern CAVs? A more detailed comparison would help to better understand the advantages and limitations of the proposed approach.
- Can you provide more details on the scalability of the method? How does the runtime of the method scale with the size of the network and the dataset?
- Have you considered evaluating the method on larger-scale datasets, such as ImageNet? This would provide valuable insights into the generalization of the method to larger datasets.
- How do you ensure that the identified concepts are meaningful and relevant? Have you conducted any user studies to validate the usefulness of the concepts from the perspective of a human interpreter?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4