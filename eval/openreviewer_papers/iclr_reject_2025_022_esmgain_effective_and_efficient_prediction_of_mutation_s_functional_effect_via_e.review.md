# Review

## Summary
The paper proposes a new method for predicting the functional effect of mutations. It first evaluates the shortcomings and potential of existing methods for both pathogenicity and functional effect prediction and then develops the optimal framework for ESM2-based functional effect prediction through detailed ablations of various fine-tuning strategies and prediction head architectures. Based on these insights, the authors propose the ESM-Effect framework, which achieves state-of-the-art (SOTA) performance on functional effect predictions outperforming multimodal competitors.

## Soundness
3

## Presentation
2

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The authors propose a benchmarking framework featuring robust test datasets and strategies.
3. The authors propose a new metric designed to emphasize prediction accuracy in challenging, non-clustered, and rare gain-of-function regions.

## Weaknesses
1. The authors should provide more details about the dataset, such as the distribution of labels (LoF, Neutral, GoF).
2. The authors should provide more details about the model, such as the number of parameters.
3. The authors should compare their method with more baselines, such as AlphaMissense.
4. The authors should report the performance of their method on different types of proteins (e.g., membrane protein, enzyme, etc.).
5. The authors should analyze the interpretability of their model.
6. The authors should discuss the limitations of their method.

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4