# Review

## Summary
This paper proposes a new state-space model based on forced harmonic oscillators. The authors present two different discretization schemes for the underlying continuous-time ODE system: implicit and implicit-explicit. Both methods preserve the stability of the dynamics and allow for efficient computation via parallel scans. The authors demonstrate the effectiveness of their method on various time series tasks, including long-range classification, regression, and forecasting.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and the experimental setup.
2. The proposed method is novel and well-motivated. The use of forced harmonic oscillators as the basis for a state-space model is a departure from the more common approaches based on diagonal linear systems or coupled oscillators.
3. The authors provide a theoretical analysis of the stability properties of their method, which is a key requirement for any state-space model. They also demonstrate the universality of their method, which means it can approximate any continuous and causal operator between time-varying functions to a desired accuracy.

## Weaknesses
1. The authors could provide more details on the computational complexity of their method, especially when compared to other state-space models. This would help readers better understand the trade-offs involved in using their method.
2. The authors could provide more details on the sensitivity of their method to the choice of hyperparameters, especially the timestep parameter Δt. This would help readers better understand the robustness of their method and how to tune it for different applications.
3. The authors could provide more details on the interpretability of their method. For example, they could discuss how the different components of their method relate to different frequencies or time scales in the input data. This would help readers better understand how their method works and how to use it for different applications.

## Questions
1. How does the choice of the timestep parameter Δt affect the performance of your method? Is there a recommended range for this parameter, and how sensitive is your method to its value?
2. How does your method compare to other state-space models in terms of computational complexity and memory usage? Can you provide a detailed comparison of these aspects for different methods?
3. How does your method handle different types of input data, such as periodic, aperiodic, or noisy time series? Can you provide examples or case studies that illustrate the performance of your method on different types of input data?
4. How does your method handle different lengths of input sequences? Can you provide experiments or case studies that demonstrate the performance of your method on sequences of varying lengths, including very long sequences?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4