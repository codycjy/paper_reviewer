# Review

## Summary
This paper introduces the Sorting Chebyshev Subspace Filter (SCSF) algorithm to accelerate eigenvalue data generation, addressing a key limitation of neural eigenvalue methods: the need for large amounts of labeled data. SCSF leverages similarities between operators using truncated fast Fourier transform (FFT) sorting and constructs a Chebyshev subspace filter to reduce redundant computations. Experimental results show that SCSF achieves up to a 6× speedup compared to various numerical solvers.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The authors present a novel approach to accelerating eigenvalue data generation, which is a significant contribution to the field.
2. The paper provides a thorough explanation of the SCSF algorithm, including its theoretical foundations and implementation details.
3. The experimental results demonstrate substantial speedups over existing methods, highlighting the practical applicability of the proposed approach.

## Weaknesses
1. While the paper discusses the speedup achieved by SCSF, it would be beneficial to provide a more detailed analysis of the trade-offs involved, particularly in terms of accuracy and memory usage.
2. The paper could benefit from a more extensive comparison with additional baseline methods to further establish the superiority of SCSF.
3. The paper could provide more details on the sensitivity of SCSF to its various parameters and how to tune them for different scenarios.

## Questions
1. How does the performance of SCSF scale with the size of the dataset, and are there any limitations on the maximum size of the dataset that can be effectively handled?
2. Could the authors provide more details on the robustness of SCSF to noise in the eigenvalue distributions of the operators?
3. How does SCSF perform on datasets with varying levels of heterogeneity in the eigenvalue distributions of the operators?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4