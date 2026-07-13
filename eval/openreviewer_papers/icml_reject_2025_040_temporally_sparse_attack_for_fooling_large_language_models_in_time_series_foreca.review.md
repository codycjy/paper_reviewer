# Review

## Summary
The paper introduces a novel attack method for LLM-based time series forecasting models. The authors propose a temporally sparse attack (TSA) that aims to deceive these models by perturbing only a limited number of time steps in the input data. The authors model the attack as a cardinality-constrained optimization problem and employ a subspace pursuit method to efficiently generate sparse perturbations. The paper demonstrates the effectiveness of TSA on various LLM-based forecasting models across different datasets, showing that even minimal perturbations can significantly degrade the models' performance.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper introduces a novel approach to attacking LLM-based time series forecasting models by proposing the temporally sparse attack (TSA). This method is innovative as it allows for effective model deception with minimal perturbations, focusing on a select few time steps rather than the entire input series.
- The authors provide a thorough evaluation of TSA across multiple LLM-based forecasting models (e.g., LLMTime, TimeGPT, TimeLLM) and diverse datasets (e.g., ETTh1, Weather, IstanbulTraffic). This comprehensive testing demonstrates the robustness and generalizability of the proposed method.
- The paper is well-structured and clearly written. The authors effectively explain the motivation behind TSA, the technical details of the method, and the results of the experiments.

## Weaknesses
- While the paper demonstrates the effectiveness of TSA, it does not provide a comparison with other state-of-the-art attack methods for time series forecasting models. Including such a comparison would strengthen the paper's contributions and provide a clearer understanding of how TSA performs relative to existing techniques.
- The paper focuses on LLM-based forecasting models, but it does not explore how TSA performs against non-LLM models. This omission limits the understanding of the method's applicability and effectiveness across different types of forecasting models.
- The authors propose an autocorrelation-based detection method as a potential defense against TSA. However, this method is only briefly discussed and not thoroughly evaluated within the paper. A more detailed exploration of this defense mechanism, including its effectiveness and limitations, would enhance the paper's contributions.
- The paper does not provide a detailed analysis of the computational cost associated with TSA. Understanding the computational requirements for implementing TSA, especially in real-time scenarios, is important for assessing its practical applicability.

## Questions
- Can you provide more details on the computational cost of TSA, especially in the context of real-time applications?
- Have you considered evaluating TSA against non-LLM forecasting models to assess its broader applicability?
- Can you provide a more detailed analysis of the proposed autocorrelation-based detection method as a defense against TSA? Specifically, what are its effectiveness and limitations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4