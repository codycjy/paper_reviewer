# Review

## Summary
This paper proposes a set of algorithmic tasks that are designed to test the creative abilities of language models. The authors argue that these tasks require a "leap of thought" - a planning step that involves making connections between abstract concepts or constructing new patterns. The key contributions are:

1. A set of minimal algorithmic tasks that abstract real-world creative endeavors, focusing on combinational and exploratory creativity.
2. A novel evaluation metric to measure algorithmic creativity - coherence, originality, and diversity.
3. An analysis of how next-token learning fails to capture the leap of thought required for these tasks, while multi-token approaches and seed-conditioning can better elicit creative behavior.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a principled and controlled testbed for studying open-ended creativity in language models, with tasks that require higher-order reasoning and planning.
2. The analysis goes beyond correctness to examine diversity and originality, providing new arguments for moving beyond next-token learning.
3. The paper demonstrates that seed-conditioning can be as effective as (and in some cases better than) temperature sampling for eliciting randomness without sacrificing coherence.
4. The work provides empirical evidence that multi-token approaches like teacherless training and diffusion models are better suited for open-ended tasks than standard next-token learning.

## Weaknesses
1. The tasks are highly artificial and simplistic compared to real-world creative endeavors.
2. The evaluation metric is a simple form of in-distribution novelty, which may not fully capture human notions of creativity.
3. The analysis focuses on a limited range of model sizes and architectures, and it's unclear how well these findings would generalize.
4. The paper doesn't thoroughly examine the interaction between model scale and creative capabilities.

## Questions
1. How well do these findings generalize to larger models and different types of creative tasks?
2. Can the authors provide more insights into why seed-conditioning works so well, particularly for smaller models?
3. How sensitive are the results to the specific choice of tasks and hyperparameters?
4. What are the limitations of the evaluation metric in capturing human-like creativity?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4