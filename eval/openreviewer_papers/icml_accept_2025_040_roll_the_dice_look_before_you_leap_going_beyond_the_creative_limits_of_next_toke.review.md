# Review

## Summary
The paper proposes a set of synthetic tasks to evaluate the "algorithmic creativity" of LLMs, which is defined as the ratio of unique and coherent generated outputs. The paper argues that next-token learning is myopic and that multi-token approaches are better at solving the proposed tasks. The paper also proposes a new method to increase the algorithmic creativity called seed-conditioning, which is shown to be comparable to temperature sampling.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper proposes a new set of synthetic tasks to evaluate the "algorithmic creativity" of LLMs. The tasks are designed to require a "leap of thought" and are used to argue that next-token learning is myopic and that multi-token approaches are better at solving the proposed tasks.
- The paper proposes a new method to increase the algorithmic creativity called seed-conditioning, which is shown to be comparable to temperature sampling.

## Weaknesses
- The paper does not provide a clear definition of creativity, which makes it difficult to understand what the paper is trying to measure and evaluate. Creativity is a complex and multi-faceted construct that has been debated and defined in various ways by scholars from different fields. It is important to have a clear definition of creativity that guides the design of the tasks and the evaluation of the models.
- The tasks proposed in the paper seem to be too simplistic and may not capture the complexity of real-world creative tasks. Creativity involves a wide range of cognitive processes, including idea generation, evaluation, and selection, which may not be fully captured by the proposed tasks. The tasks may be too easy or too specific, which may not provide a challenging enough benchmark for evaluating the creativity of LLMs.
- The paper does not provide a clear evaluation framework to assess the creativity of LLMs. The paper proposes a metric called algorithmic creativity, which is defined as the ratio of unique and coherent generated outputs. However, this metric may not fully capture the complexity of creativity, as it does not take into account the quality or the novelty of the generated outputs. A more comprehensive evaluation framework would involve assessing the creativity of LLMs in terms of their ability to generate novel and valuable ideas, to build upon existing knowledge, and to think outside the box.

## Questions
- How is the algorithmic creativity metric different from simply measuring the diversity of the generated outputs?
- How does the proposed method of seed-conditioning compare to other methods for increasing the diversity and creativity of LLMs, such as prompt engineering, chain-of-thought reasoning, or self-reflection?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4