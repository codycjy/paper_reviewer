# Review

## Summary
This paper studies the problem of generalization to unseen data in recurrent neural networks. In particular, the authors focus on the streaming parity task, where the network must learn the parity of the number of 1s in a sequence of bits. The authors find that as the network trains, its hidden states transition from a tree-like structure to a simpler automaton structure that can generalize to longer sequences than seen during training. The authors also provide a simplified mathematical model of the dynamics of this state transition, and show that the time it takes for the network to transition to the simplified automaton structure has a phase transition in terms of initial weight magnitude and training set size.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The paper is clearly written, and the main claims are well supported by the experiments.
- The authors provide a novel mathematical model of the dynamics of state merging, and show that this model makes experimentally testable predictions.
- The paper makes a number of connections to relevant literature, both in machine learning and neuroscience.
- The problem of generalization to unseen data is highly relevant to the ICLR community.

## Weaknesses
- The paper focuses on the streaming parity task, but it is unclear how well the results will generalize to other tasks. While the authors do show preliminary results on modular subtraction in Transformers, it would be interesting to see a more thorough investigation of how the state merging dynamics depend on the task.
- The mathematical model of the merging dynamics is only loosely connected to the actual network architecture used in the experiments. It would be interesting to see how well the predictions of the model hold up when applied to the actual network.

## Questions
- How well do the results from the mathematical model hold up when applied to the actual network used in the experiments? For example, do the states that merge have similar effective learning rates in the model and the network?
- How do the results depend on the task? For example, do other simple tasks like modular addition/subtraction show the same state merging dynamics? Does the task need to have a finite automaton solution, or can it have an infinite automaton solution (e.g. the Collatz conjecture)?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4