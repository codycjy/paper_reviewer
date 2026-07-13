# Review

## Summary
This paper examines the impact of token ordering on training and inference in masked diffusion models (MDMs). The authors theoretically and empirically demonstrate that MDMs train on computationally intractable subproblems compared to autoregressive models (ARMs). They also show that adaptive inference strategies can be used to sidestep these hard problems, leading to significant performance improvements. The main contributions of this paper are:
- Providing theoretical and empirical evidence that MDMs train on hard masking problems.
- Demonstrating that adaptive inference strategies can be used to sidestep the hard problems encountered during MDM training.
- Showing that MDMs with adaptive inference can outperform ARMs on logic puzzles like Sudoku, even outperforming ARMs with 7× as many parameters and that were explicitly trained via teacher forcing to learn the right order of decoding.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper provides a thorough analysis of the impact of token ordering on training and inference in MDMs, with both theoretical and empirical evidence.
- The authors propose and evaluate several adaptive inference strategies, including Top-K and Top-K probability margin, and show their effectiveness in improving MDM performance.
- The paper demonstrates that MDMs with adaptive inference can outperform ARMs on logic puzzles, which is a novel and significant finding.
- The paper is well-organized and clearly written, with detailed explanations of the methodology and results.

## Weaknesses
- The paper focuses primarily on logic puzzles as the evaluation task, and it is unclear how well the adaptive inference strategies would generalize to other types of tasks.
- The paper does not provide a detailed analysis of the computational complexity of the adaptive inference strategies compared to vanilla MDM inference.
- The paper does not provide a detailed analysis of the impact of the adaptive inference strategies on the diversity of the generated samples.

## Questions
- Can you provide more insights into why MDMs with adaptive inference outperform ARMs on logic puzzles, despite ARMs being trained with teacher forcing to learn the right order of decoding?
- How well do the adaptive inference strategies generalize to other types of tasks beyond logic puzzles? Have you evaluated them on any other tasks?
- What is the computational complexity of the adaptive inference strategies compared to vanilla MDM inference? How does it affect the training and inference time?
- How does the adaptive inference strategies affect the diversity of the generated samples? Have you evaluated the diversity of the generated samples with and without the adaptive inference strategies?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4