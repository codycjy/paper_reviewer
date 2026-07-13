# Review

## Summary
This paper studies the learning dynamics of recurrent neural networks (RNNs) on the streaming parity task, aiming to understand how neural networks can generalize infinitely from finite training experience. The authors propose a theory of algorithm development in RNNs, focusing on the construction of a finite automaton that reproduces the task. They identify a phase transition in the learning dynamics where the RNNs transition from a tree-fitting phase to a merging phase, resulting in perfect infinite generalization. The paper also discusses the implications of these findings for understanding generalization in neural networks and the development of computational algorithms.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides a detailed analysis of the learning dynamics of RNNs on the streaming parity task, offering insights into how neural networks can generalize beyond the training data. The authors propose a theory of algorithm development that is supported by empirical evidence.
2. The paper is well-structured and clearly written. The authors provide a clear explanation of the streaming parity task and the proposed theory of algorithm development.
3. The findings of this paper have implications for our understanding of generalization in neural networks. The discovery of a phase transition in the learning dynamics and the construction of a finite automaton that reproduces the task provides insights into how neural networks can learn computational algorithms.

## Weaknesses
1. The paper focuses on the streaming parity task, and it is unclear how well the proposed theory generalizes to other tasks.
2. The authors use deterministic finite automata (DFA) to interpret the recurrent neural network. However, it is worth noting that this method may not be applicable to more complex or continuous data settings.
3. The authors mention that the theory is not necessarily a realistic model of the complete learning dynamics and that higher-order local interactions, global interactions, inductive biases from architectural choices, regularization, and noise were ignored. These factors may have additional effects on algorithm development that are worth studying.

## Questions
1. Can the authors provide more examples or case studies to illustrate the practical implications of their theory?
2. How does the proposed theory of algorithm development compare to other existing theories or frameworks for understanding generalization in neural networks?
3. Are there any potential limitations or assumptions in the proposed theory that should be addressed?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4