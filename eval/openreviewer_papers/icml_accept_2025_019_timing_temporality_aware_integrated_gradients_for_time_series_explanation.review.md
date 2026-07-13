# Review

## Summary
The paper proposes two novel evaluation metrics for time series explainability, Cumulative Prediction Difference (CPD) and Cumulative Prediction Preservation (CPP). It also proposes a novel time series explainability method, Time Series Integrated Gradients (TIMING), which builds on top of the existing Integrated Gradients (IG) method. The paper demonstrates the effectiveness of TIMING through experiments on both synthetic and real-world datasets, showing that it outperforms existing time series explainability baselines.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper proposes two novel evaluation metrics for time series explainability, Cumulative Prediction Difference (CPD) and Cumulative Prediction Preservation (CPP), which address the limitations of existing evaluation metrics.
- The paper proposes a novel time series explainability method, Time Series Integrated Gradients (TIMING), which enhances the classical IG method by incorporating temporal awareness.
- The paper demonstrates the effectiveness of TIMING through experiments on both synthetic and real-world datasets, showing that it outperforms existing time series explainability baselines.
- The paper provides a comprehensive review of related work on time series explainability, highlighting the gaps that the proposed method addresses.
- The paper provides a detailed description of the proposed method, including its mathematical formulation and algorithm, making it easy to understand and implement.

## Weaknesses
- The paper does not provide a detailed analysis of the computational complexity of the proposed method, which could be a concern for large-scale datasets.
- The paper does not provide a detailed analysis of the sensitivity of the proposed method to its hyperparameters, which could affect its performance in practice.
- The paper does not provide a detailed comparison of the proposed method with other state-of-the-art time series explainability methods, such as MILLETS [1] and TimeMIL [2].
- The paper does not provide a detailed analysis of the interpretability of the proposed method, which is an important aspect of explainability.

References:

[1] Inherently Interpretable Time Series Classification via Multiple Instance Learning. In ICLR 2024.

[2] TimeMIL: Advancing Multivariate Time Series Classification via a Time-Aware Multiple Instance Learning. To appear in ICML 2024.

## Questions
- Can you provide a more detailed analysis of the computational complexity of the proposed method, including its runtime and memory requirements?
- Can you provide a more detailed analysis of the sensitivity of the proposed method to its hyperparameters, such as the number of segments and the minimum and maximum segment lengths?
- Can you provide a more detailed comparison of the proposed method with other state-of-the-art time series explainability methods, such as MILLETS and TimeMIL?
- Can you provide a more detailed analysis of the interpretability of the proposed method, including how it can help users understand and trust the predictions of time series models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4