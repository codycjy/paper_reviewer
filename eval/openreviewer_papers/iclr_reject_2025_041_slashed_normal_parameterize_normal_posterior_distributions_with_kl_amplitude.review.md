# Review

## Summary
This paper proposes a novel parameterization for the normal posterior distribution in variational inference, called Slashed Normal. The key innovation is introducing a new activation function, stdplus, which allows direct control over the KL divergence between the posterior and prior by connecting it to the L2 norm of the neural network output. The authors demonstrate how this parameterization provides theoretical insights into posterior collapse and can mitigate it in practice, while also enabling explicit control over the KL divergence term that is often only indirectly controlled in VAEs through hyperparameters like β.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The theoretical foundation is strong, with clear mathematical derivations connecting the KL divergence to the proposed parameterization. The authors provide rigorous proofs for their claims and demonstrate how the Slashed Normal parameterization relates to existing approaches like Residual Normal and the Information Bottleneck.
2. The experiments are well-designed, with clear ablation studies showing the impact of different normalization schemes and their effects on model performance. The authors evaluate their approach on both classification tasks (MNIST and CIFAR10) and generative modeling (LSTM VAEs), demonstrating its versatility.
3. The proposed stdplus activation function addresses a real practical issue in VAE training - the numerical instability often caused by the log and exp operations in the KL divergence term. The authors provide a detailed algorithm for computing stdplus and show its superior performance compared to traditional activation functions through careful analysis of the derivative behavior.

## Weaknesses
1. The motivation for the Slashed Normal parameterization could be more clearly articulated. While the theoretical benefits are well-explained, it's less clear why this specific parameterization would be advantageous in practical applications compared to other approaches for controlling the KL divergence. The paper would benefit from more concrete examples of scenarios where this parameterization provides clear advantages over existing methods.

2. The experimental evaluation, while thorough in its ablation studies and theoretical analysis, could be expanded to include more diverse datasets and model architectures. The authors primarily focus on classification tasks (MNIST and CIFAR10) and simple generative models (LSTM VAEs). Including experiments on more complex datasets (e.g., ImageNet) and architectures (e.g., transformer-based VAEs) would strengthen the paper's claims about the parameterization's versatility and robustness.

3. The computational overhead introduced by the stdplus function is not adequately addressed. The authors mention that 4-5 iterations are required for float64 precision, but don't discuss the impact on training time or memory usage compared to standard exponential or softplus functions. Providing empirical benchmarks showing the computational cost would help readers assess the practical feasibility of using this parameterization in large-scale applications.

## Questions
1. Could the authors provide more concrete examples of practical scenarios where the Slashed Normal parameterization offers clear advantages over existing methods for controlling the KL divergence in VAEs? This would help better motivate the approach for a broader audience.

2. How does the computational overhead of the stdplus function compare to standard activation functions like exponential or softplus in terms of training time and memory usage? Are there any scenarios where the additional cost is prohibitive?

3. The paper focuses on classification and simple generative modeling tasks. Could the authors provide more extensive experiments on more complex datasets and architectures to demonstrate the parameterization's versatility and robustness?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4