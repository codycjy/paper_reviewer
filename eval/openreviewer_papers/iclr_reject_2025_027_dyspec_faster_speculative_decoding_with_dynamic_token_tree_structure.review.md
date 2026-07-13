# Review

## Summary
This paper presents a novel speculative decoding algorithm called DYSPEC, which utilizes a dynamic token tree structure to enhance inference speed and scalability. Unlike previous methods that rely on fixed token tree structures, DYSPEC dynamically expands the token tree based on the draft model’s distribution, employing a greedy strategy to prioritize tokens with higher acceptance probabilities. This dynamic approach is shown to optimize the acceptance rate and reduce latency across various datasets and model sizes. Specifically, on the Llama2-70B model, DYSPEC achieves a 9.1× improvement in throughput and a 9.4× reduction in latency.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel dynamic token tree structure that adapts based on the draft model’s distribution, improving the acceptance rate and overall efficiency of speculative decoding.
2. The authors provide a solid theoretical basis for their approach, demonstrating that DYSPEC can achieve optimal results under mild assumptions.
3. The paper includes extensive empirical evaluations across multiple datasets and model sizes, showing consistent improvements over existing methods.

## Weaknesses
1. The paper lacks a detailed comparison with other dynamic tree-based methods, such as EAGLE-2 and Recurrent Drafter.
2. The authors do not provide sufficient evidence to support Hypothesis 1. More experiments are needed to validate this assumption across different datasets and model architectures.
3. The paper does not discuss the potential for integrating DYSPEC with other speculative decoding techniques, such as batch inference or multi-draft model approaches.

## Questions
1. How does DYSPEC compare to other dynamic tree-based methods in terms of implementation complexity and performance across different model sizes?
2. Can you provide additional experiments to further validate Hypothesis 1, especially in cases where the draft and target distributions diverge significantly?
3. How might DYSPEC be combined with or enhanced by other speculative decoding techniques, such as batch inference or the use of multiple draft models?
4. How does the performance of DYSPEC vary with different draft model qualities and sizes? Is there a point at which the dynamic tree structure no longer provides significant benefits?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4