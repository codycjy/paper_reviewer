# Review

## Summary
This paper proposes an efficient implementation of the $\alpha$-entmax attention, a class of sparse attention that generalizes the softmax attention. The authors introduce a hybrid Halley-bisection algorithm for faster empirical convergence and custom Triton kernels to exploit the inherent sparsity of $\alpha$-entmax. Experiments on encoder-only and decoder-only models show the effectiveness of the proposed method.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is effective and efficient, as shown by the experiments.

## Weaknesses
- The proposed method is only evaluated on smaller language models. It is unclear whether the method is effective and efficient on larger language models, e.g., those with 3B and 7B parameters.

## Questions
- How does the proposed method perform on larger language models, e.g., those with 3B and 7B parameters?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4