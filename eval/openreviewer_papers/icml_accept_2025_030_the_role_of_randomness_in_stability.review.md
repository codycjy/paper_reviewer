# Review

## Summary
The paper studies the connection between the randomness complexity of replicable learning and globally stable learning. The main result is a “weak-to-strong” boosting theorem: the randomness complexity of a task is closely tied to the best replication probability of any deterministic algorithm solving it, the “global stability” of the task. This is further extended to a connection between the randomness complexity of differentially private learning and global stability. The authors also study the randomness complexity of agnostic PAC learning, showing that a class has bounded randomness complexity iff it has finite Littlestone dimension.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper gives a nice connection between the randomness complexity of replicable learning and globally stable learning, and extends it to a connection between the randomness complexity of differentially private learning and global stability. These connections are interesting and useful. The paper is generally well-written and easy to follow.

## Weaknesses
The technical novelty is somewhat limited. The proofs of the main results rely heavily on the results and techniques of prior works, e.g., (Dixon et al., 2023), (Canonne et al., 2024), (Bun et al., 2023), (Chase et al., 2023). The results are interesting and important, but I feel that the paper lacks some new ideas and techniques in the proof.

## Questions
Is it possible to extend the results to a connection between the randomness complexity of replicable/DP learning and global stability for general statistical tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4