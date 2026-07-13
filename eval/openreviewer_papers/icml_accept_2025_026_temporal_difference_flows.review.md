# Review

## Summary
This paper introduces a novel approach to learning Geometric Horizon Models (GHMs) using flow-matching and diffusion techniques. The authors present a range of methods, including TD-CFM, TD-CFM(C), TD$^2$-CFM, TD-DD, and TD-DD, which leverage the structure of the Bellman equation to improve the accuracy and stability of GHMs, particularly for long-horizon predictions. The paper includes theoretical analyses and empirical evaluations across multiple domains, demonstrating the effectiveness of the proposed methods in comparison to existing models like GANs and VAEs.

## Soundness
4

## Presentation
3

## Contribution
3

## Strengths
- The paper presents a novel application of flow-matching and diffusion models to the problem of long-horizon predictive modeling in reinforcement learning, which is an innovative contribution to the field.
- The theoretical analysis is rigorous and well-supported, providing a solid foundation for the proposed methods and their potential advantages.
- The empirical evaluation is comprehensive, covering a variety of domains and metrics to thoroughly assess the performance of the proposed models.
- The paper is well-structured and clearly written, making it accessible to readers with a background in reinforcement learning and generative modeling.

## Weaknesses
- The paper does not provide a detailed discussion on the computational complexity of the proposed methods, which could be an important consideration for practical applications.
- While the empirical evaluation is comprehensive, it could benefit from including more diverse and complex environments to further demonstrate the robustness and generalizability of the proposed methods.
- The paper does not thoroughly discuss the limitations of the proposed methods or potential areas for future research, which could provide valuable insights for further exploration in this area.

## Questions
1. What are the key limitations of the proposed methods, and how might they be addressed in future research?
2. How does the computational complexity of the proposed methods compare to existing approaches, and what are the practical implications for deployment in real-world applications?
3. Can the proposed methods be extended to more complex environments or tasks beyond those evaluated in the paper, and what challenges might arise in such extensions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4