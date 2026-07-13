# Review

## Summary
The paper presents Highway Backpropagation, a method to accelerate training of neural networks with residual-like architectures by approximately computing the backpropagation gradient in parallel. The proposed method is derived from a decomposition of the gradient as the sum of gradients along all possible paths in the computational graph. The authors show empirically that their method can achieve significant speed-ups in training time with minimal performance loss.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
The paper is well written and the derivations are sound. The authors show that the proposed method can achieve significant speed-ups in training time with minimal performance loss.

## Weaknesses
The main weakness of this paper is that the proposed method is incremental and does not present enough novelty. The idea of approximating backpropagation by considering a limited number of paths in the computational graph has been explored before. The authors do not discuss how their method differs from previous work. In addition, the experimental evaluation is not exhaustive and does not compare the proposed method with other approximate backpropagation methods.

## Questions
1. How does the proposed method differ from other approximate backpropagation methods that consider a limited number of paths in the computational graph?
2. The authors show that the proposed method can achieve significant speed-ups in training time with minimal performance loss. However, is it possible to provide a theoretical bound on the performance loss as a function of the number of paths considered?
3. The experimental evaluation is not exhaustive. It would be useful to compare the proposed method with other approximate backpropagation methods on a wider range of neural network architectures and datasets.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4