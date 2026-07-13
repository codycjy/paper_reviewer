# Review

## Summary
This paper studies the depth required to exactly compute the maximum of $d$ input in a ReLU neural network. While the exact computation of the maximum is still an open question, it is known that $\lceil \log_2(d+1) \rceil$ layers suffice to compute the maximum of $d$ inputs. The authors focus on a subclass of neural networks called $B_d^0$-conforming neural networks. This subclass of neural networks is defined by the requirement that the breakpoints of the neurons are of the form $x_i = x_j$ or $x_i = 0$. The authors show that $\Omega(\log \log d)$ layers are required to compute the maximum of $d$ input. This is proven by providing a recursive formula for the dimension of the space of $B_d^0$-conforming neural networks with $\ell$ layers. As a corollary of this result, the authors reprove the result of Hertrich et al. that the maximum of 4 input cannot be computed with 2 layers. Finally, the authors generalize their results to maxout neural networks showing that the upper bound on the depth required to compute the maximum of $l$ input is not tight for rank $(3,2)$ maxout neural networks.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
- The paper is very well-written. The authors did a good job explaining the relevant concepts from tropical geometry. The proofs are also well-explained.
- The results are interesting and relevant to the community. The authors provide new insights on the depth required to exactly compute the maximum of $d$ input. This is a well-motivated problem as understanding the exact representation power of neural networks is important for both theoretical and practical reasons. The results on the tightness of the upper bound for maxout networks are also interesting and show that the depth required to compute the maximum of $d$ input is still not well understood.
- The paper provides a new proof that the maximum of 4 input cannot be computed by a 2-layer $B_d^0$-conforming neural network. This result was previously only known by a computational proof.

## Weaknesses
- The results are limited to $B_d^0$-conforming neural networks. However, the authors acknowledge this limitation and provide arguments as to why studying this subclass of neural networks is interesting.

## Questions
- In the abstract, the authors mention that the results of Hertrich et al. are verified with a computational proof. What does this mean? Why can't this proof be formalized?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4