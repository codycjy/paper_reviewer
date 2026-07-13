# Review

## Summary
The paper presents two novel methods, Bi-Models Training (BMT) and Multi-Models Training (MMT), aimed at achieving exact federated unlearning (FU) while maintaining good post-unlearning performance. Traditional methods like retraining from scratch (RfS) ensure exact FU by restarting the federated learning process, but they suffer from poor initial performance after unlearning. BMT and MMT address this issue by leveraging existing client knowledge to improve the initial aggregated model post-unlearning.

BMT maintains isolated copies of local models, which are then used to initialize the global model after unlearning. MMT builds on BMT by training sub-federated learning models on disjoint subsets of clients to capture the joint influence of multiple clients. This approach reduces the "double influence" problem and improves the initialization of the aggregated model.

The authors validate the effectiveness of these methods through experiments on various real-world datasets, including vision and language tasks, demonstrating their superiority over RfS and other baselines in terms of accuracy and convergence speed after unlearning.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed methods ensure exact federated unlearning while maintaining better post-unlearning performance than traditional methods like retraining from scratch. This is particularly important in practical applications where model deployment cannot be delayed.
2. The experimental results demonstrate the effectiveness of BMT and MMT across various datasets and tasks, including vision datasets (MNIST, FashionMNIST, CIFAR-10, CIFAR-100) and language tasks. The methods consistently outperform baselines in terms of accuracy and convergence speed after unlearning.
3. The paper addresses a timely and important issue in federated learning, as the need for exact unlearning increases due to privacy regulations and the right to be forgotten.

## Weaknesses
1. The paper could benefit from a more detailed comparison with existing federated unlearning methods, particularly in terms of computational overhead and scalability. While the authors mention some methods, a deeper analysis of how BMT and MMT compare in terms of resource requirements and scalability, especially for large-scale deployments, would strengthen the paper.
2. The paper assumes that clients are equally likely to request unlearning, which may not reflect real-world scenarios. The authors could explore how the methods perform under non-uniform unlearning probabilities and provide strategies to optimize performance in such cases.
3. While the methods are validated on various datasets, the paper could benefit from experiments on more diverse and complex models, such as large language models, to further demonstrate the scalability and generalizability of BMT and MMT.

## Questions
1. How do BMT and MMT compare to other exact federated unlearning methods in terms of computational overhead and scalability, especially for large-scale deployments?
2. How do BMT and MMT perform under non-uniform unlearning probabilities? Are there strategies that can be implemented to optimize performance in such cases?
3. Have the authors considered testing BMT and MMT on more complex models, such as large language models, to further demonstrate their scalability and generalizability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4