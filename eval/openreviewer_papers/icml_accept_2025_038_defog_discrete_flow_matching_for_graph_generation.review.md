# Review

## Summary
This paper introduces DeFoG, a discrete flow-matching framework for graph generation. By decoupling training and sampling, DeFoG enables flexible sampling and achieves state-of-the-art performance on synthetic and molecular datasets, outperforming diffusion-based models with significantly fewer sampling steps.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-organized and easy to follow.
2. The authors provide a thorough theoretical analysis of the proposed method.

## Weaknesses
1. The proposed method is an application of discrete flow matching (DFM) [1] to graph generation, which limits its technical novelty. DFM has already been applied to other domains, such as protein co-design [1] and image generation [2]. The authors should clarify the unique challenges and contributions of applying DFM to graph generation.
2. The authors should include a comparison with CatFlow [3], a flow-based graph generation method that is currently not benchmarked. CatFlow also decouples training and sampling and allows for flexible sampling.
3. The authors should benchmark the proposed method on large molecule generation benchmarks, such as Guacamol [4] and MOSES [5].
4. The authors should provide a time complexity analysis of the proposed method and compare its running time with existing methods.

References:

[1] Generative Flows on Discrete State-Spaces: Enabling Multimodal Flows with Applications to Protein Co-Design. ICML 2024.

[2] Scaling Rectified Flow Transformers for High-Resolution Image Synthesis. ICML 2024.

[3] Variational Flow Matching for Graph Generation. NeurIPS 2024.

[4] Guacamol: benchmarking models for de novo molecular design. Journal of Chemical Information and Modeling, 2019.

[5] Molecular sets (moses): a benchmarking platform for molecular generation models. Frontiers in Pharmacology, 2020.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4