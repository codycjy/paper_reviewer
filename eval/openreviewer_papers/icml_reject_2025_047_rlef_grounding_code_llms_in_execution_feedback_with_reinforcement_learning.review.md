# Review

## Summary
This paper introduces RLEF, a novel method that teaches LLMs to iteratively improve code generation based on execution feedback. RLEF frames code generation as a multi-turn process, where the LLM generates code, receives execution feedback (e.g., error messages, unit test results) for each generation, and iteratively refines the solution until it passes all tests or reaches a specified turn limit. The authors apply RLEF to Llama 3.1 models (8B and 70B parameters) and evaluate them on CodeContests, HumanEval+, and MBPP+ benchmarks. Results show that RLEF significantly improves solve rates, reducing the sample budget required for inference, and generalizes well across different programming tasks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
* RLEF effectively leverages execution feedback for iterative code improvement, demonstrating substantial performance gains on competitive programming tasks.
* The method significantly reduces the sample budget required during inference, making it more efficient compared to previous approaches.
* RLEF generalizes well to different benchmarks (HumanEval+, MBPP+), suggesting broader applicability beyond the training domain.
* The paper provides detailed analysis of inference behavior, showing that RLEF-trained models can effectively utilize execution feedback for error correction and code refinement.

## Weaknesses
* The method requires access to unit tests or execution feedback during both training and inference, which may not always be available or practical.
* The paper does not extensively explore the sensitivity of the method to the quality or specificity of the feedback provided during training.
* The paper does not provide a detailed analysis of the computational cost of RLEF training and inference compared to other approaches.
* The paper does not extensively explore the potential for overfitting to the specific format and content of the training feedback.

## Questions
* How does the quality of execution feedback provided during training affect the performance of RLEF? Is the method sensitive to noisy or misleading feedback?
* What is the computational overhead of RLEF compared to other methods during both training and inference? How does this scale with model size and problem complexity?
* How does RLEF handle cases where public unit tests are not available or comprehensive? Can the method still provide benefits in such scenarios?
* How does RLEF compare to approaches that use feedback in a single-turn setup? Can the benefits of multi-turn feedback be effectively communicated in a single-turn framework?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4