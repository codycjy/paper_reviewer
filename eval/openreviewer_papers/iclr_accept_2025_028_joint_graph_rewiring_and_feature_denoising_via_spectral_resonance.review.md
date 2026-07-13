# Review

## Summary
The paper presents an algorithm for jointly denoising graph structures and node features to improve node classification in GNNs. The proposed method, JDR, aligns the leading spectral spaces of the graph and feature matrices, aiming to handle graphs with multiple classes and varying levels of homophily or heterophily. Theoretical justification and empirical evidence support the effectiveness of JDR, showing it outperforms existing rewiring methods on both synthetic and real-world tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The method is well-motivated and justified.
- The proposed method is novel and effective.
- The experiments are comprehensive.

## Weaknesses
- The method requires access to node features, which may not always be available.
- The paper does not include a discussion on the robustness of JDR to different types and levels of noise in the graph structure and features.

## Questions
- How robust is JDR to different types and levels of noise in the graph structure and features?
- How does JDR perform on graphs with extremely high dimensions? Is there a limit on the dimensionality that JDR can handle efficiently?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4