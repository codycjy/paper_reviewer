# Review

## Summary
The paper proposes an architecture for active inference agents that integrates a generative model with a policy network. The generative model is trained to predict a long horizon, and the policy network is optimized using the expected free energy (EFE). The authors evaluate their agent in a manufacturing simulation environment and compare it to a DQN baseline.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
The paper tackles the important problem of credit assignment in long-horizon tasks. The proposed architecture is interesting and novel. The experimental results are promising.

## Weaknesses
The paper is not well written. There are missing references (e.g., line 221) and figures (e.g., Figure 1). The notation is sometimes inconsistent (e.g., $Q_\phi(a_t)$ in line 152 and $Q_{\phi_a}(a_t)$ elsewhere). The related work section is very brief and does not adequately discuss how the proposed method relates to and differs from previous approaches.

The experimental evaluation is limited. There is only one baseline, and the experiments were run for a relatively small number of epochs.

## Questions
- How does the proposed method relate to and differ from previous approaches to credit assignment in long-horizon tasks?
- How does the agent perform if evaluated for more epochs?
- How does the agent perform in other long-horizon tasks?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4