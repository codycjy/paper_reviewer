# Review

## Summary
This paper proposes a novel online algorithm, iterative Nash policy optimization (INPO), to learn the Nash policy of a two-player game modeling the LLM alignment problem. The algorithm is based on the classical no-regret learning algorithm, online mirror descent (OMD), and enjoys both the iteration complexity and last-iterate convergence. Experiments show that the proposed method outperforms previous online RLHF algorithms.

## Soundness
4

## Presentation
3

## Contribution
4

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is novel, with both theoretical guarantees and empirical improvement over previous methods.

## Weaknesses
1. The proposed method is similar to Nash-MD, DNO and SPPO, which also formulate the LLM alignment problem as a two-player game and use no-regret learning to learn the Nash policy. The differences are not fully discussed in the paper.
2. The proposed method assumes access to the exact preference signals, while previous methods such as SPPO only assume access to the win rate of two responses. This assumption limits the applicability of the proposed method.
3. The proposed method does not explicitly consider the generalization problem, while previous methods such as DNO and SPPO use explicit generalization bounds. This may affect the generalization performance of the proposed method.

## Questions
1. How does the proposed method differ from Nash-MD, DNO and SPPO? What are the advantages of the proposed method over these methods?
2. How does the proposed method perform when there is noise in the preference signals? How does the noise level affect the performance of the proposed method?
3. How does the proposed method perform on tasks other than language tasks, such as vision tasks? How does the proposed method compare to other methods on these tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4