# Review

## Summary
This paper proposes a framework, CASAK-V, to improve the efficiency of long-context LLM inference by dynamically generating sparse attention patterns and adaptively compressing the KV-cache. The authors leverage a pre-trained vision-language encoder-decoder transformer to identify sparse attention patterns and use a frequency-aware recency-based importance scoring for KV-cache compression. The evaluation results show that CASAK-V achieves minimal performance degradation on long-context tasks while reducing memory usage by 40%.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is well-motivated and supported by comprehensive experiments and analysis.
2. The paper is well-written and easy to follow.
3. The efficiency problem of long-context LLM inference is an important research direction.

## Weaknesses
1. The proposed method is complex and requires significant engineering efforts to implement. The MGM requires fine-tuning on a synthetic dataset, and the adaptive KV-cache compression requires periodic re-evaluation of importance scores, which can introduce non-trivial overhead.
2. The MGM is fine-tuned on a synthetic dataset generated from the LLM itself, which may limit the generalization of the proposed method to other LLMs.

## Questions
1. How does CASAK-V perform on other LLMs?
2. How does the fine-tuning of the MGM on a synthetic dataset generated from the LLM itself affect the generalization of the proposed method? Have you evaluated the performance of CASAK-V on other LLMs?
3. How does CASAK-V handle the trade-off between sparsity and accuracy? Is there an upper bound on the sparsity level that can be applied while maintaining a certain level of accuracy?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4