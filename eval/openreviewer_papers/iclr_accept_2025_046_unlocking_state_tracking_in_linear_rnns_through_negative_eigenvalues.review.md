# Review

## Summary
This paper investigates the limitations of Linear Recurrent Neural Networks (LRNNs), such as Mamba and DeltaNet, in performing state-tracking tasks, particularly the parity task. The authors extend prior work by Sarrof et al. (2024) to show that LRNNs with state-transition matrices constrained to positive eigenvalues cannot solve parity. They further demonstrate that LRNNs require non-diagonal state-transition matrices with negative eigenvalues to solve modular counting tasks. To address these limitations, the authors propose extending the eigenvalue range from [0, 1] to [−1, 1], which improves the state-tracking capabilities of LRNNs. Experimental results show that this modification enables LRNNs to successfully perform parity and modular arithmetic tasks, with improvements in perplexity on code and math datasets. The work highlights the importance of negative eigenvalues and non-diagonal structures in enhancing the expressivity of LRNNs without compromising efficiency or training stability.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper provides a rigorous theoretical analysis, extending prior work by Sarrof et al. (2024) to non-diagonal LRNNs, and presents new results on the expressivity of products of generalized Householder matrices.
- The proposed modification of extending the eigenvalue range from [0, 1] to [−1, 1] is simple yet effective, improving the state-tracking capabilities of LRNNs.
- The experimental results demonstrate clear improvements in performance on state-tracking tasks, with consistent gains across different models and tasks.
- The paper is well-written and clearly presents the theoretical concepts, proofs, and experimental results.

## Weaknesses
- The theoretical expressivity results for LRNNs with multiple layers are still limited, and the paper does not provide a clear roadmap for extending these results to more complex tasks.
- The experimental results show mixed results when comparing models with different eigenvalue ranges on language modeling tasks, with improvements for code and math datasets but not for all tasks.
- The paper does not thoroughly discuss the potential trade-offs or limitations of allowing negative eigenvalues in LRNNs, such as potential impacts on training stability or convergence.

## Questions
- Can you provide more insights into the theoretical expressivity of LRNNs with multiple layers and how it relates to the number of layers needed to solve complex tasks?
- How does the proposed modification affect the training dynamics and stability of LRNNs? Have you observed any convergence issues or other challenges during training?
- How does the proposed modification impact the computational complexity and efficiency of LRNNs, especially for large-scale applications?
- Can you provide more details on the experimental setup, including hyperparameters, training procedures, and evaluation metrics used in the experiments?
- How do the results compare to other approaches that address state-tracking limitations, such as non-linear RNNs or hybrid architectures?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4