# Review

## Summary
The authors propose a new framework for federated learning based on generalized variational inference. The framework is designed to be robust to model misspecification, which is a common issue in both frequentist and Bayesian federated learning approaches. The authors provide theoretical analysis to demonstrate the convergence and robustness properties of the framework. The effectiveness of FedGVI is evaluated through experiments on synthetic and real-world datasets, showing improved robustness and predictive performance compared to existing methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed framework is novel and addresses an important issue in federated learning.
- The paper provides a solid theoretical analysis of the framework, including proofs of convergence and robustness properties.
- The authors evaluate their approach on both synthetic and real-world datasets, demonstrating its effectiveness.

## Weaknesses
- The paper does not provide a detailed analysis of the computational complexity of FedGVI, which could be a limitation for large-scale problems.
- The experiments could be expanded to include more diverse datasets and models to further demonstrate the generalizability of the approach.

## Questions
- Can the authors provide more insights into the computational complexity of FedGVI and how it scales with the number of clients and model size?
- How does the choice of divergence function in the GVI objective affect the performance of FedGVI in practice? Is there a recommended choice?
- The paper mentions that FedGVI can be extended to handle non-IID data distributions across clients. Can the authors elaborate on how this extension would work in practice?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4