# Review

## Summary
This paper studies self-improvement in language models through a theoretical lens. The authors frame self-improvement as a "sharpening" process, where the model uses its own outputs as verification to improve its generation capabilities. They explore two main algorithms: SFT-Sharpening and RLHF-Sharpening. The paper establishes theoretical bounds, showing that SFT-Sharpening is minimax optimal under certain conditions, while RLHF-Sharpening can improve upon SFT by leveraging online exploration. Empirical results support the theoretical findings, demonstrating that sharpening can significantly improve inference-time performance across various tasks and models.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper introduces a novel theoretical framework for understanding self-improvement in language models through the concept of sharpening.
- The authors provide rigorous theoretical analysis, establishing bounds and optimality conditions for the proposed algorithms.
- The paper successfully connects theoretical findings to practical improvements in model performance across various tasks and models.

## Weaknesses
- The paper primarily focuses on the log-probability as the self-reward function, which is a simplified case compared to more complex self-reward functions used in practice.
- The empirical validation is limited to a few tasks (e.g., MATH, GSM8K, ProntoQA) and model-dataset pairs. Broader empirical evaluations across more diverse tasks and models would strengthen the claims.
- While the paper demonstrates improvements, it would benefit from a more comprehensive comparison with other state-of-the-art self-improvement methods beyond the basic baselines provided.

## Questions
- How do the theoretical guarantees translate to more complex self-reward functions that are used in practice?
- Can the authors provide more insights into the practical implications of the theoretical bounds, especially regarding the sample complexity?
- How do the proposed methods compare to other recent self-improvement approaches in terms of computational efficiency and performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4