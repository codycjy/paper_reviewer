# Review

## Summary
This paper studies the bit-rate (or rate) of sparse autoencoder (SAE) codes, in which a sparse vector $y$ of $k$ non-zero components in $[N]$ is mapped to a vector $x = Fy$ of length $d$ through a fixed dictionary $F$ of column vectors $f_1,\dots,f_N$, where the vector $x$ is then used as a linear superposition code for $y$.

The authors focus on the case where $y$ is uniformly distributed over all $k$-element subsets of $[N]$ and $F$ is a Rademacher dictionary, in which case the one-step decoding algorithms (such as threshold decoding and top-$k$ decoding) require a certain minimum value of $d$ to correctly decode $y$ from $x$. The authors derive a lower bound on this minimum value of $d$, in terms of $k$ and $N$, and show that this lower bound is empirically close to the actual minimum value of $d$ required by one-step decoding algorithms.

The authors then compare this rate (in bits per dimension) with the rate of the basis pursuit decoding algorithm, in which $y$ is recovered by solving a convex program to minimize $\|x - Fy\|_2^2$ subject to $\|y\|_1 \leq c$ for some constant $c$. Empirically, the basis pursuit decoding algorithm requires a significantly lower rate (in bits per dimension) than the one-step decoding algorithms.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The authors provide a clear and well-written explanation of the problem of superposition coding and the bit-rate required for correct decoding. The authors also provide a clear and well-written explanation of the basis pursuit decoding algorithm and how it compares to the one-step decoding algorithms.

## Weaknesses
The main weakness of this paper is that the contribution is not significant enough to justify publication at ICLR. The authors provide a lower bound on the bit-rate required for correct decoding by one-step decoding algorithms, and show that this bound is empirically close to the actual bit-rate required. However, the authors do not provide an upper bound on the bit-rate required, or any concrete results on the performance of the basis pursuit decoding algorithm.

The authors also do not provide any experimental results on the performance of the one-step decoding algorithms on real-world data, or any theoretical analysis of the bit-rate required for correct decoding by these algorithms on real-world data. This makes it difficult to assess the practical significance of the results presented in this paper.

## Questions
- The authors claim that the basis pursuit decoding algorithm requires a significantly lower rate (in bits per dimension) than the one-step decoding algorithms. However, the empirical results presented in Figure 5 only show that the basis pursuit decoding algorithm requires a lower rate than the top-$k$ decoding algorithm. Is there any theoretical justification for why the basis pursuit decoding algorithm should require a lower rate than the threshold decoding algorithm? If so, it would be helpful for the authors to include a brief discussion of this in the paper.
- In lines 324-326, the authors claim that the crosstalk term $\xi_i$ behaves like a Gaussian random variable with variance $k\gamma_i$. Is there any theoretical justification for why the crosstalk term should behave like a Gaussian random variable? If so, it would be helpful for the authors to include a brief discussion of this in the paper.
- In lines 332-333, the authors claim that the probability of tail events for the different variables $\xi_i$ are "sufficiently independent". What does this mean? It would be helpful for the authors to provide a more precise statement of this claim, and to explain why it is justified.
- In lines 348-350, the authors claim that the values $\gamma_i(F)$ governing the scale of crosstalk suffered by matched filters can't be made significantly smaller than $1/d$ when $d \leq N$ for small $\epsilon$. Is there any theoretical justification for why this is true? If so, it would be helpful for the authors to include a brief discussion of this in the paper.
- In lines 375-376, the authors claim that the vector $y$ can be recovered from its image $Fy$ under a random projection by a certain convex optimization problem so long as $d \geq \kappa(\epsilon)N$ for some constant $\kappa(\epsilon)$. Is there any reference or proof that the authors can cite to support this claim?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4