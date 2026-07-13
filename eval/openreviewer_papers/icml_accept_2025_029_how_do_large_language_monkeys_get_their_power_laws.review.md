# Review

## Summary
This paper examines the scaling behavior of inference compute, where the average success rate across tasks scales as a power law with the number of attempts. The authors show that for a fixed set of problems, the negative log of the average success rate should scale polynomially with the number of independent attempts. They demonstrate that this scaling behavior arises from the distribution of single-attempt success rates and that a heavy left tail in this distribution is necessary to observe power law scaling. They also propose a new estimator for predicting the power law exponent.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well written and provides a clear and compelling explanation for the observed scaling behavior of inference compute. The authors offer theoretical insights into why this scaling behavior emerges and propose a new estimator that improves the prediction of the scaling exponent. The findings contribute to a deeper understanding of scaling laws in language models and have practical implications for predicting model performance.

## Weaknesses
The authors demonstrate that the observed scaling behavior arises from the distribution of single-attempt success rates. However, they do not provide sufficient information on how this distribution is obtained or how it is related to the overall distribution of problems. This leaves questions about the generalizability of their findings. Additionally, while the proposed estimator outperforms the standard least-squares estimator, it is unclear how it compares to other existing estimators. Providing more context and comparison with alternative methods would strengthen the evaluation of the estimator's performance.

## Questions
1. Can you provide more details on how the distribution of single-attempt success rates is obtained? Is it based on real data from the problems used in inference compute scaling studies, or is it derived from a theoretical argument? How does this distribution relate to the overall distribution of problems?

2. The paper shows that a heavy left tail in the distribution of single-attempt success rates is necessary for power law scaling. Is it possible to estimate the left tail of the distribution from a small number of observations, and if so, how accurate would such an estimate be?

3. The proposed estimator outperforms the standard least-squares estimator in predicting the scaling exponent. How does it compare to other existing estimators, if any exist, or to alternative methods for predicting the scaling exponent?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4