# Review

## Summary
The paper proposes a new approach to time series modelling based on the flow-based generative models (FBGMs) framework. The authors generalize the key elements of FBGMs, stochastic interpolation and the Markovian projection, to the time series setting. This yields a family of latent probabilistic forecasters that contains a discrete time counterpart of FBGMs for time series. The paper demonstrates that the models inherit the convenient theoretical properties of FBGMs while being easy to work with in practice.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and the proposed method is well-motivated.
- The authors provide a detailed and thorough theoretical analysis of the proposed method.

## Weaknesses
- The experimental results are limited to synthetic datasets. It would be beneficial to include real-world datasets, such as the ones used in [1, 2].
- The authors do not compare their method with other state-of-the-art time series models, such as [1, 2].
- The authors do not provide a complexity analysis of the proposed method.

[1] Kollovieh, M., Ansari, A. F., Bohlke-Schneider, M., Zschiegner, J., Wang, H., & Wang, Y. B. (2023). Predict, refine, synthesize: Self-guiding diffusion models for probabilistic time series forecasting. Advances in Neural Information Processing Systems, 36, 28341-28364.

[2] Hu, Y., Wang, X., Wu, L., Zhang, H., Li, S. Z., Wang, S., & Chen, T. (2024). FM-TS: Flow Matching for Time Series Generation. arXiv preprint arXiv:2411.07506.

## Questions
- Can the authors provide experimental results on real-world datasets?
- Can the authors compare their method with other state-of-the-art time series models?
- Can the authors provide a complexity analysis of the proposed method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4