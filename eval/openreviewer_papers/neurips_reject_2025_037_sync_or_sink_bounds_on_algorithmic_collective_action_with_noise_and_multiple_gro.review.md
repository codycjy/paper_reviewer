# Review

## Summary
The paper studies the effect of noise on collective action in algorithmic systems. The authors derive bounds on the success rate of collective action, considering both feature-label and feature-only strategies, and explore the impact of noise through experiments.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper extends existing work on collective action to multiple distributions, which can model both coordination noise and multiple collectives.
2. The authors provide theoretical bounds for the success rate of collective action with multiple distributions and validate these bounds through experiments.
3. The paper discusses the trade-offs between collective size and noise, providing insights into how noise can significantly affect the success of collective action.

## Weaknesses
1. The theoretical framework and experimental setup are very similar to the previous work [HMMDZ23], which is also focused on collective action against algorithmic systems. The novelty of this paper is limited.
2. The paper assumes that the base distribution $P_0$ is independent of the signal set $\mathcal{X}_1$. However, in real-world scenarios, there may be correlations between the base distribution and the signal set. This assumption may not hold in many practical cases.
3. The paper only considers two distributions ($P_1$ and $P_2$), which may not fully capture the complexity of real-world scenarios where there can be multiple distinct collectives with different goals and strategies.

## Questions
1. How does the proposed framework handle cases where the base distribution $P_0$ is dependent on the signal set $\mathcal{X}_1$?
2. Can the theoretical bounds be extended to handle more than two distributions? If so, what are the challenges in extending the current bounds?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4