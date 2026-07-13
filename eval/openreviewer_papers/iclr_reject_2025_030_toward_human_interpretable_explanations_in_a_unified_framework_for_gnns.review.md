# Review

## Summary
The paper presents a method to explain Graph Neural Networks (GNNs) using small, connected, non-isomorphic induced subgraphs called graphlets and their associated orbits. The authors propose a unified framework, UO-Explainer, that provides both model-level and instance-level explanations. The method decomposes GNN weights into orbit units to identify important substructures contributing to predictions. The paper claims that UO-Explainer outperforms existing baselines in providing meaningful and interpretable explanations across synthetic and real-world datasets.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The use of graphlets and orbits as explanatory units is a fresh perspective in the field of GNN explainability.
2. The paper addresses both model-level and instance-level explanations, which is a significant contribution to the field.

## Weaknesses
1. The paper could provide more details on how the method performs on larger and more complex graphs.
2. The paper could benefit from a deeper discussion on the selection of graphlets and orbits and how different choices might affect the explanations.
3. The paper could provide more examples of how UO-Explainer helps domain experts in real-world applications.

## Questions
1. How does the method scale with the size and complexity of the input graph?
2. How sensitive is the method to the choice of graphlets and orbits? What are the implications of using different sets of graphlets and orbits?
3. Can the method be extended to other GNN tasks beyond node classification?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4