# Review

## Summary
This paper explores the potential of scaling up inference-time computation in LLMs to improve their performance on challenging tasks. The authors propose and investigate two primary mechanisms for test-time computation scaling: (1) searching against dense, process-based verifier reward models (PRMs), and (2) updating the model's distribution over a response adaptively, given the prompt at test time. The effectiveness of these methods varies depending on the difficulty of the prompt, leading the authors to propose a "compute-optimal" scaling strategy that adaptively allocates test-time compute per prompt. This strategy significantly improves efficiency in test-time compute scaling for math reasoning problems, surpassing a best-of-N baseline by more than 4×. Additionally, in a FLOPs-matched evaluation, the authors demonstrate that test-time compute can outperform a 14× larger model on problems where a smaller base model achieves non-trivial success rates.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a thorough and systematic analysis of test-time computation scaling, covering multiple mechanisms and strategies. The authors present detailed experimental results and comparisons, offering valuable insights into the effectiveness of different approaches under varying conditions.
2. The concept of a "compute-optimal" scaling strategy is innovative and well-motivated. The authors' approach to adaptively allocate test-time compute per prompt shows promise in optimizing performance for individual queries.
3. The paper addresses an important question regarding the trade-offs between inference-time compute and model size. The findings suggest that test-time computation can be more effective than scaling model parameters in certain scenarios, which has significant implications for the future of LLM deployment and optimization.

## Weaknesses
1. The paper primarily focuses on math reasoning problems using the MATH dataset. While the results are promising, it's unclear how well these findings generalize to other types of tasks or domains. Additional experiments in diverse settings would strengthen the paper's claims.
2. The difficulty of the prompts used in the experiments is based on a model-specific metric. The authors use the base model's pass@1 rate to estimate question difficulty, which may not be universally applicable. Alternative measures of difficulty that do not rely on the base model's performance should be explored.
3. The proposed "compute-optimal" strategy relies on pre-computing the accuracy of different test-time compute approaches for various difficulty levels. This approach may not be practical in real-world scenarios where difficulty levels cannot be predetermined or where the model's performance may vary significantly from the precomputed estimates.

## Questions
1. How well do the proposed test-time computation scaling methods generalize to other types of reasoning tasks beyond math, such as logical reasoning or commonsense reasoning?
2. The paper compares test-time compute scaling to scaling model parameters. How does test-time compute scaling compare to scaling both model parameters and training data size?
3. The experiments use a FLOPs-matched comparison between test-time compute and pretraining. How does the performance compare if the compute budget is kept constant instead of matching FLOPs?
4. The "compute-optimal" strategy relies on pre-computed accuracy estimates for different difficulty levels. How robust is this strategy to changes in the model's performance or to new, unseen prompts that may fall outside the pre-computed difficulty bins?
5. The paper focuses on PaLM-2 models. How do the findings generalize to other LLM architectures?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4