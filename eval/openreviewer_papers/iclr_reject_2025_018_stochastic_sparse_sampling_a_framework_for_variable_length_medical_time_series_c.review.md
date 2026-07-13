# Review

## Summary
The paper proposes a stochastic sparse sampling strategy for the classification of variable length medical time series. The method randomly samples fixed size windows from the time series and classifies each window independently. The predicted class probabilities for each window are then aggregated using a convex combination to obtain the final class prediction for the time series. The method is applied to the task of seizure onset zone (SOZ) detection using iEEG data from four different medical centers. The method is shown to outperform multiple baselines including finite context models (trained on fixed length patches), infinite context models (e.g. ROCKET), and recurrent models (e.g. GRUs, LSTMs). The method is also shown to generalize well to unseen medical centers.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed strategy is novel and allows for the use of finite context models for variable length time series classification.
2. The method is shown to outperform multiple baselines on a challenging real world medical classification task.
3. The method is shown to generalize well to unseen medical centers.
4. The paper is well written and easy to follow.

## Weaknesses
1. There is no comparison with the simple baseline of averaging the class predictions from a finite context model (e.g. PatchTST) over all windows. This baseline would help establish the importance of the convex combination and calibration steps.
2. The paper does not discuss the computational requirements of the proposed method. It would be useful to compare the training and inference times of the proposed method with the baselines.
3. The paper does not discuss the impact of the choice of window size on the performance of the method. It would be useful to show how the performance of the method changes with different window sizes and compare it with the finite context baselines.

## Questions
1. How does the performance of the proposed method compare with the simple baseline of averaging the class predictions from a finite context model (e.g. PatchTST) over all windows?
2. What are the computational requirements of the proposed method? How do they compare with the baselines?
3. How does the performance of the method change with different window sizes?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4