# Review

## Summary
This paper proposes FlowFit, a new diffusion-based generative model that enables single-step sampling. The core idea is a new formulation for flow modeling based on basis function fitting. FlowFit delivers fast, high-quality generation while substantially simplifying the training process, making it a practical and efficient diffusion-based method.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The writing is clear and easy to understand.
2. The method is simple and effective, and experiments demonstrate its superiority.

## Weaknesses
1. The order of the basis functions appears to be a crucial hyperparameter. The authors should provide more discussion and analysis on how to select this hyperparameter.
2. In the experiment, the authors only used a Polynomial basis. It would be beneficial to experiment with more types of basis functions to evaluate their performance and see if they can further improve the results.
3. In Table 1, it would be helpful to add a column to show the number of training steps for each method, not just the FID score. This would allow us to better understand the relationship between the number of training steps and the model performance.
4. In Line 209, the authors mention that they apply the Exponential Moving Average (EMA) of the model parameters to improve stability and performance. However, this is not a fair comparison, as other methods do not use EMA. The authors should provide results without using EMA to ensure a fair comparison.
5. The authors should provide more visualization results to better demonstrate the effectiveness of the proposed method.

## Questions
Please refer to the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4