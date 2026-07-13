# Review

## Summary
This paper studies the learning dynamics of linear RNNs (LRNNs). The authors first derive the energy function of LRNNs and show that the dynamics follow gradient descent on this energy function. They then derive an exact solution of the input-output connectivity modes. To study the learning dynamics of recurrent modes, they take a local approximation. They also derive the neural tangent kernel (NTK) for finite-width LRNNs. Finally, they demonstrate the generalizability of their results by applying the theoretical framework to describe the behavior of LRNNs trained on sensory integration tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well-written and easy to follow. The learning dynamics of linear RNNs have not been theoretically studied before, so this paper fills a gap in the literature. The theoretical results are interesting and could be relevant for both deep learning and neuroscience.

## Weaknesses
My main concern is the gap between the assumptions made in the theoretical analysis and the real-world applications of linear RNNs. The authors make three assumptions (page 3), and Assumptions 1 and 2 are particularly restrictive. It would be helpful if the authors could provide more justification for these assumptions, especially for Assumption 2, which seems quite strong. For example, can the authors explain why the left and right eigenvectors of the input-output correlation matrix are constant over time? The authors cite Saxe et al. (2014, 2018) as precedence, but in these papers, the singular value decomposition (SVD) is used for the feedforward weight matrix, not the input-output correlation matrix.

The authors also mention that their theoretical framework can be applied to explain the behavior of LRNNs performing sensory integration tasks, but they do not provide any details. It would strengthen the paper if they could include a more detailed explanation of how their theory relates to this application.

## Questions
1. Can the authors provide more justification for Assumptions 1 and 2? Specifically, why are the left and right eigenvectors of the input-output correlation matrix constant over time? 

2. Can the authors include a more detailed explanation of how their theory can explain the behavior of LRNNs performing sensory integration tasks?

3. In Figure 2, the authors show that the blue curve converges to a smaller solution but is initially learned faster than the orange curve. Can they provide more insight into why this happens? What are the implications of this finding for the learning dynamics of LRNNs?

4. In Figure 3, the authors show that inverse-exponential and exponential task dynamics yield unstable solutions. Can they provide more insight into why this is the case? What are the implications of this finding for the training of LRNNs on real-world tasks?

5. In Figure 4, the authors show that there is a rapid phase transition of connectivity mode values as the recurrent computation increases. Can they provide more insight into why this happens? What are the implications of this finding for the understanding of LRNNs?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4