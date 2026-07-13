# Review

## Summary
This paper introduces the phenomenon of feature absorption in sparse autoencoders (SAEs) for large language models (LLMs). Feature absorption occurs when a latent feature fails to activate on seemingly arbitrary tokens, while more specific latents absorb the feature. This happens when features form a hierarchy, like "starts with S" being absorbed into "short." The authors validate this phenomenon through experiments on hundreds of open-source SAEs and propose a metric to detect feature absorption. They argue that feature absorption is a significant obstacle to the practical application of SAEs, particularly in high-stakes classification tasks, and call for further research to address the fundamental theoretical issues before SAEs can be used for interpreting LLMs robustly and at scale.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper identifies a novel phenomenon, feature absorption, which is a significant contribution to the field of model interpretability.
- The authors provide empirical evidence through experiments on hundreds of open-source SAEs, validating the widespread occurrence of feature absorption.
- The proposed metric to detect feature absorption is a useful tool for researchers working with SAEs.
- The paper discusses the implications of feature absorption for the practical application of SAEs, highlighting the need for confidence in latent features, especially in high-stakes classification tasks.

## Weaknesses
- The metric used to detect feature absorption is not perfect and may underestimate the true level of feature absorption.
- The study primarily focuses on a specific task (predicting the first-letter of a single token) and model (Gemma-2-2B). It's unclear how generalizable the findings are to other models and tasks.
- While the authors acknowledge the limitations of their metric and the small number of non-JumpReLU SAEs trained, a more detailed discussion of the potential biases and limitations of their approach would strengthen the paper.

## Questions
- Have you tested your metric on any other models or tasks beyond Gemma-2-2B and the first-letter prediction task? If so, what were the results?
- How do you think feature absorption might affect the reliability of SAEs in high-stakes applications, such as bias detection or deceptive behavior identification?
- Are there any potential solutions or workarounds to mitigate the issue of feature absorption that you propose?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4