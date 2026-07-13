# Review

## Summary
This paper proposes a novel approach called CODEI/O to improve the reasoning abilities of LLMs by training them to predict code inputs and outputs in pure natural language CoTs. The authors collect over 450K functions from various sources and transform them into a unified format, generating 3.5M training samples. They also introduce CODEI/O++, which incorporates multi-turn revisions based on code execution feedback. Experiments show that CODEI/O consistently outperforms existing baselines across various reasoning benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-structured and clearly written, with detailed explanations of the methodology and experiments.
2. The approach of using code input/output prediction to improve general reasoning capabilities is novel and well-motivated.
3. The experiments are comprehensive, covering a wide range of reasoning tasks and baselines.
4. The performance improvements demonstrated by CODEI/O across multiple benchmarks are significant and consistent.

## Weaknesses
1. The paper lacks a detailed analysis of potential data leakage between the training dataset and the evaluation benchmarks.
2. The two-stage training approach may be more complex to implement compared to single-stage training.
3. The approach is mainly tested on Python code. It's not clear how well it would generalize to other programming languages or non-code reasoning tasks.

## Questions
1. How do you ensure that the input/output prediction tasks adequately cover a diverse range of reasoning patterns?
2. Have you conducted any analysis to verify that the performance improvements are not simply due to data leakage?
3. How does the two-stage training approach affect the model's ability to learn other tasks compared to single-stage training?
4. Can you provide more details on the data sources and the process of transforming raw code files into the unified format?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4