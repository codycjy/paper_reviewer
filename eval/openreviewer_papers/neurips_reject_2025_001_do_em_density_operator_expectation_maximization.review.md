# Review

## Summary
The authors introduce an expectation maximization algorithm for density operators, and apply it to density operator models for classical data. The main idea is to use the Petz recovery map to perform the expectation step. The authors specialize the approach to classical data, where it becomes a classical expectation maximization algorithm, and apply it to a quantum-interleaved deep Boltzmann machine on the MNIST dataset.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The authors introduce a new expectation maximization algorithm for density operators, and show how it can be used to train density operator models for classical data. The approach is novel, and the theoretical results appear to be sound. The paper is generally well-written and clear. The authors also provide experimental evidence that their approach can be used to train a Boltzmann machine on the MNIST dataset, which is a significant achievement.

## Weaknesses
The paper has a few weaknesses that should be addressed. First, the authors do not provide a detailed discussion of the computational complexity of their algorithm. It would be helpful to know how the computational requirements of their approach compare to those of other methods for training density operator models. Second, the authors do not provide a detailed analysis of the performance of their algorithm on the MNIST dataset. It would be helpful to know how the algorithm converges and how well it is able to reconstruct the MNIST training images. Third, the authors do not provide a detailed discussion of the limitations of their approach. It would be helpful to know what assumptions are made by their algorithm and what potential drawbacks or limitations these assumptions may introduce.

## Questions
1. Can the authors provide a more detailed discussion of the computational complexity of their algorithm? How does the computational requirements of their approach compare to those of other methods for training density operator models?

2. Can the authors provide a more detailed analysis of the performance of their algorithm on the MNIST dataset? How well does the algorithm converge, and how well is it able to reconstruct the MNIST training images?

3. Can the authors provide a more detailed discussion of the limitations of their approach? What assumptions are made by the algorithm, and what potential drawbacks or limitations may result from these assumptions?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4