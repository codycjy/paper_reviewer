# Review

## Summary
This paper focuses on the numerical precision of LLM inference, which is often neglected in evaluation practices. It reveals that the numerical precision, especially the non-associative nature of floating-point arithmetic under limited numerical precision, affects the reproducibility of LLM performance. The authors conduct extensive analysis on four LLMs and five benchmarks. They also propose an optimized inference pipeline that performs all computations in FP32 while retaining model weights in BF16 precision, which balances memory efficiency with numerical stability.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. This paper investigates the impact of numerical precision on the reproducibility of LLMs. The findings are interesting and may provide valuable insights for the LLM community.
2. The authors conduct extensive experiments to support their findings. The experimental design is reasonable.
3. The authors propose an optimized inference pipeline that balances memory efficiency with numerical stability.

## Weaknesses
1. The authors only evaluate the models with a maximum size of 8B. It would be better to include larger models (e.g., 32B or 65B) in the experiments to see if the same conclusions apply.
2. The authors only use the LiveCodeBench and math-related benchmarks in the experiments. It would be better to include more diverse benchmarks (e.g., GSM8K, MMLU) to see if the same conclusions apply.

## Questions
1. What about the impact of FlashAttention on the reproducibility of LLMs?
2. What about the impact of the KV cache on the reproducibility of LLMs?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4