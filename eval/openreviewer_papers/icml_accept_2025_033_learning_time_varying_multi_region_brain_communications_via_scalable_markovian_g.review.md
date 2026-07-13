# Review

## Summary
This paper introduces the Adaptive Delay Model (ADM), a framework for learning time-varying communication patterns between multiple brain regions from neural recordings. The model combines Gaussian Processes (GPs) with State Space Models (SSMs) to capture dynamic interactions with time-varying temporal delays. ADM uses parallel scan inference algorithms to achieve efficient scaling to large datasets. The authors validate the model on synthetic data and real-world neural recordings, demonstrating its ability to uncover both directional and temporal dynamics of neural communication.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-organized and clearly written, with detailed explanations of the methodology and results.
- The ADM model addresses a significant gap in current methods by enabling the discovery of time-varying communication patterns between brain regions, which is crucial for understanding dynamic neural processes.
- The use of parallel scan algorithms significantly reduces computational complexity from $O(T^3)$ to $O(\log T)$, making the model scalable to large neural datasets with long recording durations.
- The model is validated on both synthetic data and real-world neural recordings, demonstrating its effectiveness in capturing biologically relevant communication patterns.

## Weaknesses
- While the model shows good performance on the tested datasets, it is unclear how well it would generalize to different types of neural recordings or more complex cognitive states.
- The model assumes a specific factor analysis structure for the relationship between latent variables and observed data, which may not hold in all neural recording scenarios.
- The model's performance is sensitive to the choice of hyperparameters, such as the order of the SSM, which may require careful tuning for different datasets.

## Questions
- How does the model handle cases where the latent dynamics evolve in a non-linear fashion, and are there plans to extend the model to capture more complex interactions?
- Can the model be extended to capture directional communication patterns between regions that are not directly connected or that have indirect communication pathways?
- How does the model perform when applied to neural recordings from different species or brain regions involved in different cognitive functions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4