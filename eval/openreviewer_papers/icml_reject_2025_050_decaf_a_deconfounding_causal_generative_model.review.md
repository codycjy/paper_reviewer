# Review

## Summary
The paper presents a novel approach to causal inference with latent confounders, allowing the estimation of causal queries (including counterfactuals) using only observational data, the causal graph, and a single amortized training process. It addresses the limitations of existing methods that assume causal sufficiency or are tailored to specific queries. The proposed method, Decaf, outperforms existing approaches on the Ecoli70 dataset and demonstrates flexibility in handling complex causal graphs with multiple hidden confounders. The paper also provides theoretical results on identifiability of causal queries and empirical validation through semi-synthetic experiments.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper's main strengths lie in its theoretical contributions and empirical validation. It provides a solid theoretical foundation for the identifiability of causal queries, extending existing results to include counterfactual queries. The empirical results on the Ecoli70 dataset demonstrate the effectiveness of Decaf in handling complex causal graphs with multiple hidden confounders. The flexibility of Decaf in handling different types of causal queries and its ability to outperform existing approaches are particularly noteworthy.

## Weaknesses
The paper has several weaknesses that should be addressed. Firstly, the assumption of completeness for the proxies is a strong one, and the authors do not provide any guidance on how to verify this assumption in practice. This makes it difficult to apply the method to real-world problems. Secondly, the empirical validation is limited to a single dataset (Ecoli70). The paper would be strengthened by including experiments on additional datasets with different characteristics. Thirdly, the computational complexity of the method is not discussed, which is an important consideration for large-scale problems. Lastly, the paper could benefit from a more thorough discussion of the limitations of the proposed approach and potential directions for future research.

## Questions
1. How can the completeness assumption be verified in practice? Are there any tests or metrics that can be used to assess whether this assumption is satisfied?
2. Have you considered the sensitivity of Decaf to model misspecification? How robust is the method to violations of the assumptions made about the data-generating process?
3. Can you provide more details on the computational complexity of Decaf? How does the training time and inference time scale with the number of variables and the complexity of the causal graph?
4. Have you considered the interpretability of the results produced by Decaf? How easy is it to extract meaningful insights from the model outputs?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4