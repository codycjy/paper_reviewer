# Review

## Summary
This paper introduces PRIMT, a novel framework for preference-based reinforcement learning (PbRL) that leverages foundation models (FMs) for multimodal synthetic feedback and trajectory synthesis. The framework addresses key challenges in PbRL, such as the reliance on extensive human input and the difficulties in resolving query ambiguity and credit assignment during reward learning. PRIMT employs a hierarchical neuro-symbolic fusion strategy to integrate the complementary strengths of large language models and vision-language models in evaluating robot behaviors. It also incorporates foresight trajectory generation to reduce early-stage query ambiguity and hindsight trajectory augmentation to improve credit assignment. The framework is evaluated on various tasks across different benchmarks, demonstrating superior performance compared to FM-based and scripted baselines.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper presents a novel approach to PbRL that leverages FMs in a unique way. The hierarchical neuro-symbolic fusion strategy for multimodal feedback integration is an innovative solution to address the limitations of single-modality evaluations.
2. The paper demonstrates rigorous methodology and thorough experimentation. The framework is evaluated on a diverse set of tasks and benchmarks, and the results are compared against multiple baselines, providing strong evidence for the effectiveness of PRIMT.
3. The paper is well-written and clearly structured. The authors provide detailed explanations of the methodology, including the mathematical formulations and algorithmic steps. The visualizations and figures aid in understanding the concepts and results.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational requirements and efficiency of PRIMT. Considering the potential use of large foundation models, it would be beneficial to discuss the computational costs and how they impact the scalability of the framework.
2. The paper could benefit from a more extensive discussion of the limitations and assumptions of the proposed framework. Are there specific scenarios or tasks where PRIMT may not perform as well? Are there any inherent assumptions in the methodology that may limit its applicability?
3. The paper could provide more details on the implementation and deployment of PRIMT, including any challenges faced during real-world deployment. This would be valuable for practitioners looking to adopt the framework.

## Questions
1. Can you provide more details on the computational requirements and efficiency of PRIMT? How does the use of large foundation models impact the scalability of the framework?
2. Are there specific scenarios or tasks where PRIMT may not perform as well? Can you discuss the limitations and assumptions of the proposed framework in more detail?
3. Can you provide more details on the implementation and deployment of PRIMT, including any challenges faced during real-world deployment?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4