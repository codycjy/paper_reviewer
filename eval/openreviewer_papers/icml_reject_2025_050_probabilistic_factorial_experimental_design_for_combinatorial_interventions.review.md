# Review

## Summary
The paper introduces the probabilistic factorial experimental design, a method for optimizing dosage administration in experiments with interactive effects. This approach allows for scalable and unbiased testing of multiple treatments by applying random combinations to a group of units. The authors provide near-optimal experimental designs for both passive and active settings, demonstrating that a dosage of 1/2 for each treatment is optimal for estimating k-way interaction models. The study also explores extensions of the design problem, including constraints on limited supply and heteroskedastic multi-round noise, and validates the findings through simulations.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The probabilistic factorial design approach is innovative, offering a scalable and unbiased method for conducting experiments with multiple treatments and interactive effects.
2. The paper provides rigorous theoretical proofs for the optimality of the proposed designs, with clear mathematical formulations and detailed derivations.
3. The authors explore several practical extensions of the design problem, such as limited supply constraints and heteroskedastic multi-round noise, which are relevant in real-world scenarios.

## Weaknesses
1. While the paper provides theoretical guarantees for near-optimality, it lacks empirical validation on real-world datasets or experiments, which could strengthen the practical relevance of the proposed methods.
2. The probabilistic design assumes a product Bernoulli distribution for treatment combinations, which may not always align with practical constraints or the nature of the interventions being studied.
3. The computational complexity of the proposed methods, especially for the active setting, could be a concern for large-scale experiments, and the paper does not provide extensive discussion on scalability or practical implementation challenges.

## Questions
1. Can the authors provide empirical evaluations on real-world datasets to validate the performance of the proposed designs against existing methods?
2. How sensitive are the proposed designs to violations of the product Bernoulli distribution assumption in practical settings?
3. What are the computational scalability of the proposed methods, especially for large-scale experiments with higher-order interactions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4