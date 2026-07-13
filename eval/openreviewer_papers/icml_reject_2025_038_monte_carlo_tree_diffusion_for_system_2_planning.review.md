# Review

## Summary
The paper proposes Monte Carlo Tree Diffusion (MCTD), a framework that combines the strengths of diffusion models and Monte Carlo Tree Search (MCTS) to improve planning in long-horizon tasks. MCTD integrates the adaptive search of MCTS with the generative capabilities of diffusion models, allowing it to iteratively refine and evaluate partially denoised plans. The framework employs three key innovations: Denoising as Tree-Rollout, Guidance Levels as Meta-Actions, and Jumpy Denoising as Fast Simulation. Experimental results demonstrate that MCTD outperforms baseline methods in challenging tasks, achieving higher-quality solutions as inference-time computation increases.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper introduces a novel approach that combines diffusion models with Monte Carlo Tree Search (MCTS), leveraging the strengths of both. This integration is innovative and addresses limitations of both individual methods.
- The paper is well-structured and clearly written, making it easy to follow the proposed methodology and experimental results.
- The paper demonstrates the effectiveness of MCTD through extensive experiments on various challenging tasks. The empirical results are impressive, showing that MCTD outperforms existing approaches in long-horizon tasks, achieving superior scalability and solution quality.

## Weaknesses
- The paper does not provide a detailed analysis of the computational complexity of MCTD. While it mentions that MCTD is computationally expensive, a more thorough analysis or comparison with baseline methods in terms of computational resources would be beneficial.
- The paper could benefit from a more detailed discussion on the limitations of MCTD and potential directions for future research. This would provide a clearer perspective on the framework's applicability and potential improvements.

## Questions
- How does the computational complexity of MCTD compare to the baseline methods, especially in large-scale search spaces? Are there any optimizations that can be applied to improve its efficiency?
- Can MCTD be extended to other types of planning tasks beyond the ones tested in the paper? If so, what modifications would be necessary?
- How does MCTD handle the trade-off between exploration and exploitation, and is there a systematic way to adjust this balance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4