# Review

## Summary
The paper presents a new method for computing a complete invariant of Euclidean graphs, which is also Lipschitz continuous with respect to the Euclidean ambient space. The invariant is based on the so-called "nested centered distribution" of the graph, which is essentially a tuple containing the distances of each vertex to the center of mass, as well as to two arbitrarily chosen reference vertices. The metric is based on the bottleneck distance between point clouds, and is also extended to a version that uses the Earth mover's distance. The method is applied to chemical data, and the computed invariants are shown to be useful for predicting the chemical element of a central atom in a molecule.

## Soundness
4

## Presentation
3

## Contribution
4

## Strengths
The paper presents a novel and elegant invariant for Euclidean graphs, which is also efficient to compute and Lipschitz continuous. The mathematical presentation is rigorous and well-structured. The paper is well-written and easy to follow.

## Weaknesses
The presentation of the experimental results could be improved. It is not clear what the purpose of the experiment is, and what the main conclusion is. It would be helpful to have a better discussion of the results, and how they relate to the main contribution of the paper.

## Questions
- I am not sure what the purpose of the experiment in Section 5 is. Is the main point just to illustrate that the invariant can distinguish different molecules? If so, this is not very clear from the presentation. It would be helpful to have a better discussion of the experimental setup, and what the main conclusions are.

- I am also not sure what the main conclusion is from Figure 3. It seems like the NBM is able to distinguish the two molecules, but it is not clear why this is important or interesting. It would be helpful to have a better explanation of why this experiment is relevant.

- In Table 4, what does "the k shortest distances" mean? Does it refer to the k nearest neighbors?

- In Table 4, what are the baseline methods that are being compared to? It would be helpful to have a better explanation of what the baselines are, and why they are relevant for comparison.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4