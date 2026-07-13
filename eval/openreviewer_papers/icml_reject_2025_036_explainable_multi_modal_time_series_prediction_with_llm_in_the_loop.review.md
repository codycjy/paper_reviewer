# Review

## Summary
The paper introduces TimeXL, a framework designed for explainable multi-modal time series prediction. It leverages a prototype-based encoder to generate preliminary predictions and explanations, which are then refined by a prediction LLM. The framework incorporates a reflection LLM to identify textual inconsistencies and a refinement LLM to iteratively enhance text quality and trigger retraining of the encoder, resulting in improved accuracy and interpretability.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow, with clear explanations of the framework components and their interactions.

2. The integration of a prototype-based encoder with LLM-driven refinement processes is a novel approach that enhances both prediction accuracy and interpretability.

3. The framework demonstrates significant improvements in AUC across multiple datasets, indicating robust performance.

4. The inclusion of human-centric explanations and the iterative refinement process adds value to the framework's applicability in real-world scenarios.

## Weaknesses
1. The framework's complexity, with multiple LLM components and iterative refinement, may lead to increased computational costs compared to simpler time series prediction models.

2. The effectiveness of the framework heavily relies on the quality of the textual data available, which may not always be readily accessible or of high quality in every application domain.

3. The framework's performance may be constrained by the limitations of the prototype-based encoder, which might not capture all relevant patterns in time series data.

4. The framework's ability to generalize across different domains and datasets is not fully explored in the paper, which may limit its applicability in diverse real-world scenarios.

## Questions
1. How does the computational cost of TimeXL compare to other state-of-the-art time series prediction methods, especially in real-time applications?

2. Are there specific types of time series or domains where TimeXL may underperform, and if so, what are the limitations?

3. How does the framework handle noisy or sparse textual data, and are there strategies to improve robustness in such cases?

4. Can the framework be extended to handle continuous-time series predictions, and if so, what modifications would be required?

5. How does the framework perform in scenarios with limited or no textual data available, and what alternatives are considered?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4