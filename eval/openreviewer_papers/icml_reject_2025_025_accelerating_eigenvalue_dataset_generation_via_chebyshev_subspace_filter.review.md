# Review

## Summary
This paper presents a method to accelerate the generation of eigenvalue datasets. The proposed method, Sorting Chebyshev Subspace Filter (SCSF), leverages the similarities between operators to reduce redundant computations. SCSF employs truncated fast Fourier transform (FFT) sorting to group operators with similar eigenvalue distributions and uses a Chebyshev subspace filter to exploit eigenpairs from previously solved problems. The paper claims that SCSF achieves up to a 6× speedup compared to various numerical solvers.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The proposed method addresses an important problem in scientific computing, which is the high computational cost of generating eigenvalue datasets. The method offers a promising approach to reduce the computational redundancy in eigenvalue dataset generation.

2. The use of truncated FFT sorting and the Chebyshev subspace filtered iteration is a novel approach to solving the operator problem sequentially. This approach takes advantage of the inherent similarities between operators to accelerate the solution process.

3. The experimental results demonstrate the effectiveness of the proposed method. The paper reports a significant speedup compared to various numerical solvers, which validates the practicality of the method.

## Weaknesses
1. The paper lacks a detailed discussion of the limitations of the proposed method. It would be helpful to address any potential drawbacks or scenarios where the method may not perform as well.

2. The paper could benefit from a more detailed comparison with other state-of-the-art methods for eigenvalue problems. While the experimental results show a speedup compared to numerical solvers, it would be useful to compare the method with other data-driven approaches or hybrid methods to provide a more comprehensive evaluation.

## Questions
1. How does the performance of SCSF vary with different matrix dimensions? Are there any scalability issues for very large matrices?

2. Can the proposed method be extended to other types of eigenvalue problems, such as non-self-adjoint operators?

3. How sensitive is the performance of SCSF to the choice of hyperparameters, such as the degree of the Chebyshev polynomial?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4