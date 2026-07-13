# Review

## Summary
This paper presents a method for learning a DFA that represents a set of human specifications, as well as DFAs for different skills. The human specification DFA is then used to check for compliance with the different learned skills. The method is evaluated on a set of Minecraft tasks, where the learned skills are used to solve tasks specified in natural language.

## Soundness
3

## Presentation
2

## Contribution
2

## Strengths
- The paper addresses an important problem of aligning LLM-based agents with human specifications.
- The method seems to be well-suited to the Minecraft setting, where the different skills are relatively atomic and well-defined, and the specifications can be formalized as DFAs.
- The paper presents a comprehensive evaluation of the method on a set of Minecraft tasks.

## Weaknesses
- The method seems to be limited to settings where the skills and specifications can be easily formalized as DFAs. It is not clear how it could be applied to more complex settings.
- The method requires a lot of interaction with the environment and with the LLM to collect counterexamples and refine the DFA. This seems like it would be very costly in terms of both time and money (if using an API-based LLM).
- The method does not seem to address the issue of LLM hallucinations, where the LLM may provide incorrect or misleading information. While the method can detect when the environment does not match the DFA, it cannot detect when the DFA does not match the intended specification.

## Questions
- How does the method handle ambiguous or underspecified natural language instructions? For example, what if the human specifies a constraint that is not related to the task, or that is only loosely related? How does the method determine whether the constraint is relevant or not?
- How does the method handle cases where the human specification is not formalizable as a DFA? For example, what if the human specifies a preference or a goal that cannot be precisely defined using a DFA?
- How does the method handle cases where the DFA for a skill is incorrect or incomplete? For example, what if the DFA misses some edge cases or fails to handle a particular input?
- How does the method handle cases where the LLM provides incorrect or misleading information? For example, what if the LLM suggests an incorrect or incomplete DFA, or fails to recognize a particular input?
- How does the method handle cases where the environment is non-deterministic or dynamic? For example, what if the environment changes or an unexpected event occurs while the agent is executing a skill?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4