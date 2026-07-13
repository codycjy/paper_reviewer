# Review

## Summary
The paper introduces Dyspec, a faster speculative decoding algorithm that dynamically builds a token tree. The method is based on the correlation between the draft distribution and the acceptance rate. Dyspec uses a greedy strategy to dynamically expand the token tree at run time to maximize the expected length of predicted sequences. The authors provide theoretical proofs and empirical results showing that Dyspec achieves optimal results and outperforms existing methods in terms of throughput and latency. The paper also discusses the overhead of token tree construction and proposes a method to reduce it using a threshold-based approach.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper provides a theoretical proof of the optimality of the proposed method under mild assumptions.
2. The paper introduces a novel dynamic token tree structure that can be adapted to different query distributions, improving the acceptance rate and speedup compared to fixed tree structures.

## Weaknesses
1. The paper does not provide a detailed comparison with other dynamic tree-based speculative decoding methods, such as EAGLE-2 and Recurrent Drafter.
2. The effectiveness of the dynamic token tree structure may be limited in scenarios where the draft model's predictions do not closely match the target model's output, which could lead to suboptimal performance.
3. The paper does not discuss the potential for integrating the proposed method with other speculative decoding techniques, such as batch speculative decoding.
4. The paper does not provide a detailed analysis of the sensitivity of the method to different hyperparameters, such as the draft temperature and the maximum draft token tree size.

## Questions
1. How does Dyspec compare to other dynamic tree-based speculative decoding methods like EAGLE-2 and Recurrent Drafter in terms of acceptance rate and speedup?
2. What are the limitations of the dynamic token tree structure, and how does it perform in scenarios where the draft model's predictions do not closely match the target model's output?
3. How can the proposed method be integrated with other speculative decoding techniques, such as batch speculative decoding, to further enhance inference performance?
4. How sensitive is the method to different hyperparameters, such as the draft temperature and the maximum draft token tree size, and how can these be optimized for different use cases?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4