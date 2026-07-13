# Review

## Summary
This paper proposes a method to improve code generation from natural language descriptions by leveraging execution feedback. The key idea is to frame the code generation task as an MDP, where the LLM is trained through RL to generate code that passes unit tests. The method is evaluated on CodeContests and shows substantial improvements over baselines. The paper also includes ablation studies and analysis of the inference-time behavior of the trained models.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The method is well-motivated and addresses an important challenge in code generation.
3. The experimental results are strong and demonstrate substantial improvements over baselines.
4. The analysis of inference-time behavior provides valuable insights into the capabilities of the trained models.

## Weaknesses
1. The method is evaluated on a single benchmark (CodeContests). Evaluating on multiple benchmarks would provide a more comprehensive assessment of the method's capabilities.
2. The paper does not include a comparison with some recent works on code generation, such as CodeGen and StarCoder.
3. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research.

## Questions
1. Have you considered evaluating the method on other code generation benchmarks, such as APPS or HumanEval?
2. How does the method compare to other recent approaches for improving code generation, such as CodeGen and StarCoder?
3. Can you provide more details on the computational resources required for training and evaluating the models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4