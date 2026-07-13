# Review

## Summary
This paper proposes DeFoG, a graph generative model that disentangles sampling from training, enabling a broader design space for optimization. DeFoG employs a discrete flow-matching formulation that respects graph symmetries. The authors theoretically relate training loss to sampling algorithms, showing DeFoG's ability to replicate ground truth distributions. They also explore DeFoG's design space and propose sampling methods that improve performance and reduce refinement steps. Experiments demonstrate state-of-the-art results across various datasets, with DeFoG outperforming diffusion-based models with only 5-10% of their sampling steps.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel graph generative framework that disentangles training and sampling, addressing inefficiencies in existing graph diffusion models and achieving state-of-the-art performance.

2. The authors provide a solid theoretical foundation for their disentangled formulation, explicitly relating training loss to sampling algorithms and demonstrating that DeFoG faithfully replicates the ground truth graph distribution.

3. The paper thoroughly explores DeFoG's design space, proposing novel sampling methods that significantly improve performance and reduce the required number of refinement steps.

## Weaknesses
1. The performance of DeFoG may heavily depend on the specific configurations and hyperparameters chosen for each dataset, which could limit its generalizability and require extensive tuning for new applications.

2. While the paper demonstrates strong performance on the evaluated datasets, it is unclear how well DeFoG would generalize to other types of graph structures or more complex real-world applications.

3. The paper focuses on achieving state-of-the-art performance, but it does not thoroughly discuss the interpretability or explainability of the generated graphs, which are important aspects in many practical applications.

## Questions
1. How does DeFoG handle extremely large graphs, and what are the scalability challenges?

2. How sensitive is DeFoG to the choice of hyperparameters, and is there an easy way to optimize them for different datasets?

3. How does DeFoG compare to other graph generative models in terms of computational efficiency and resource requirements?

4. Can DeFoG be extended to handle directed graphs or graphs with different types of edges?

5. How does DeFoG perform in scenarios where the graph structures are highly variable or dynamic?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4