# Review

## Summary
The paper proposes a formal definition of deception within the framework of partially observable Markov decision processes (POMDPs). The authors quantify deception in terms of the actor's beliefs, actions, and utility, framing it as a regret problem. The paper aims to align the formal definition with human intuition through experiments and user studies.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
- The paper addresses an important and timely topic as AI systems become more integrated into daily life.
- The formal definition of deception through regret theory in POMDPs is a novel approach that could have implications for AI alignment and deception detection.
- The authors attempt to validate their definition through human intuition, which is crucial for ensuring that AI systems operate in ways that are morally and ethically acceptable to humans.

## Weaknesses
- The paper's formal definition of deception as regret in POMDPs is an interesting idea, but it doesn't fully account for the complexity of human intuition when it comes to deception. The authors acknowledge that their definition might not capture all nuances of deceptive behavior, particularly in cases where the speaker's actions unintentionally lead to good outcomes.
- The paper uses a simplified POMDP model for exposition, which may not capture the full complexity of real-world interactions. The model assumes a naive listener who does not expect deception, which may not reflect how humans approach interactions in real life.
- The experiments are limited to three scenarios, which may not be sufficient to generalize the findings. Additionally, the scenarios are relatively simple and do not fully explore edge cases or more complex forms of deception.
- The paper does not compare its definition with existing philosophical or psychological definitions of deception. A comparison could have helped to highlight the novelty and limitations of the proposed definition.

## Questions
- How does the proposed definition handle cases where the speaker's actions are unintentionally deceptive, but still lead to negative outcomes for the listener?
- How does the formalism scale to more complex scenarios, especially those involving multi-turn conversations or longer-term interactions?
- How does the proposed definition compare with existing definitions in philosophy or psychology? Are there specific limitations in the formalism that prevent it from capturing aspects of deception that are widely recognized in these disciplines?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4