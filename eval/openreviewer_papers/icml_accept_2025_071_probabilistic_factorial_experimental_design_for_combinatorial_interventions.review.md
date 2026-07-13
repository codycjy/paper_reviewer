# Review

## Summary
This paper studies the problem of optimal experimental design in the setting where each unit can receive a random combination of treatments. The paper first considers the setting where the experimenter chooses the dosages in a prospective fashion, without any data collection in prior rounds. It is shown that assigning a dosage of 1/2 to each treatment is near-optimal for estimating any k-way interaction model. The paper then considers the setting where the experimenter can collect data in multiple rounds and use the data collected in prior rounds to update the dosage design in the current round. It is shown that there exists a near-optimal dosage design that can be numerically optimized.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow. The problem studied in the paper is well-motivated and has important applications in biology.
2. The theoretical results are strong. The paper shows that in the passive setting, a dosage of 1/2 for each treatment is near-optimal for estimating any k-way interaction model. In the active setting, a near-optimal dosage design can be numerically optimized. The paper also explores several extensions of the design problem, such as constraints on limited supply and heteroskedastic multi-round noise.
3. The experiments validate the theoretical results and show the effectiveness of the proposed methods.

## Weaknesses
1. The paper assumes that the treatments are independently assigned to a group of units according to a prescribed dosage vector. This assumption may not hold in practice, as there may be interference or censoring effects between units.
2. The paper assumes that the outcomes are determined solely by the received treatment, which may not be true in practice. Incorporating covariate-based models would enable finer-grained personalized treatment-outcome predictions.

## Questions
1. How would the results change if there is interference or censoring effects between units?
2. How would the results change if the outcomes are determined by both the received treatment and unit-specific covariates?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4