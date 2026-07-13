# Review

## Summary
This paper introduces the multi-marginal Schrödinger bridge matching framework, which aims to infer trajectories from population data with discrete time-sampled observations. The proposed algorithm is an extension of the iterative Markovian fitting algorithm, which is used for the standard Schrödinger bridge matching framework. The proposed algorithm is tested on synthetic and single-cell RNA sequencing data.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.

2. The proposed multi-marginal Schrödinger bridge matching framework is a natural extension of the standard Schrödinger bridge matching framework and has broad potential applications in biology and other fields.

3. The proposed algorithm shows strong performance on synthetic and real-world datasets, and the computational efficiency is impressive.

## Weaknesses
1. The proposed algorithm is an extension of the iterative Markovian fitting algorithm, which limits its methodological novelty. 

2. The proposed algorithm has only been tested on low-dimensional datasets, and its performance in high-dimensional settings remains untested.

3. The proposed algorithm assumes that the population data can be described by a low-dimensional representation (e.g., PCA), which may not hold in many real-world applications.

## Questions
1. How does the proposed algorithm perform on high-dimensional datasets? What are the limitations and challenges in scaling the algorithm to high-dimensional settings?

2. How does the choice of the bridge process (i.e., the reference dynamic) impact the performance of the proposed algorithm? Have the authors explored the use of different bridge processes, such as non-linear bridges or bridges with varying diffusion constants?

3. How does the proposed algorithm handle noisy or incomplete data? Are there any strategies that the authors employ to handle missing or noisy observations in the dataset?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4