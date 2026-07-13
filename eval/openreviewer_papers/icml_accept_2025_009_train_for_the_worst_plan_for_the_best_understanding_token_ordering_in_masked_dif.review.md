# Review

## Summary
This paper examines the impact of token ordering on training and inference in Masked Diffusion Models (MDMs). The authors provide theoretical and empirical evidence that MDMs train on computationally intractable subproblems compared to autoregressive models (ARMs). They also demonstrate that adaptive inference strategies can be used to avoid these hard problems during inference. The paper's main empirical result shows that a simple adaptive strategy improves the accuracy of MDMs on logic puzzles from < 7% to almost 90%, outperforming ARMs trained with teacher forcing.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a dual perspective on MDMs, highlighting the training complexity but also showing how adaptive inference can overcome it.
- The theoretical analysis is rigorous and well-supported by empirical evidence.
- The adaptive inference strategies proposed in this paper are simple yet effective, leading to significant performance improvements on logic puzzles.

## Weaknesses
- The paper focuses primarily on logic puzzles as the testbed. While these results are impressive, it remains uncertain how well these findings would generalize to more complex tasks, such as natural language generation.
- The comparison between MDMs and ARMs could be more comprehensive, particularly in terms of parameter count and training cost. The paper acknowledges that MDMs require training on exponentially more masking problems than ARMs but does not fully explore the implications of this difference in terms of computational resources and convergence rates.

## Questions
- Can the authors provide more insights into the generalizability of their results to other types of discrete data, such as text or biological sequences?
- How do the adaptive inference strategies proposed in this paper compare to other recent approaches for improving MDMs, such as those based on steerable filters or attention mechanisms?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4