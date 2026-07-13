# Review

## Summary
The paper extends the concept of Linear Mode Connectivity (LMC) from permutations to a broader set of symmetries, including permutations, semi-permutations, orthogonal transformations, and general invertible maps. This generalization allows for the discovery of low- and zero-barrier linear interpolation paths between independently trained Vision Transformers and GPT-2 models. The framework also extends to multi-model and width-heterogeneous settings, enabling alignment across different architectures.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper introduces a unified framework that broadens the definition of LMC to include various symmetries beyond permutations. This generalization is novel and addresses limitations of previous approaches.
- The paper provides empirical evidence of low- and zero-barrier linear interpolation paths between independently trained Vision Transformers and GPT-2 models. This is a significant finding, suggesting that the loss landscape of these models is more connected than previously thought.
- The framework extends to multi-model and width-heterogeneous settings, allowing for alignment across different architectures. This has implications for model merging and ensemble methods.
- The paper is well-written and provides a clear explanation of the proposed framework, the symmetries it includes, and the empirical results.

## Weaknesses
- The paper focuses primarily on empirical evidence of LMC for Vision Transformers and GPT-2 models. While this is a strong empirical contribution, the lack of theoretical proof or formal analysis limits the strength of the claims.
- The framework assumes that the models being aligned have been trained on the same task. It is not clear how well the methods would generalize to models trained on different tasks, which is a more common scenario in practice.
- The paper does not thoroughly discuss the computational complexity of the proposed methods, especially for the learned matching approach. The optimization process may be computationally intensive, which could limit the practical applicability of the methods.
- The paper could benefit from a more detailed comparison with other model alignment and LMC techniques in the literature. While it mentions some existing methods, a comprehensive comparison would help to better position the proposed framework.

## Questions
- How does the proposed framework perform when applied to models trained on different tasks? Have you explored any preliminary investigations in this direction?
- Can you provide more insights into the computational complexity of the learned matching approach? How does it scale with the size of the models and the number of iterations?
- How does the proposed framework compare to other state-of-the-art model alignment and LMC techniques in terms of accuracy and computational efficiency?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4