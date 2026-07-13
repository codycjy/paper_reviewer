# Review

## Summary
This paper proposes a hypernetwork view of the multi-head attention mechanism. Based on this view, the authors propose a variant of linear attention, HYLA, which inserts a nonlinearity and a normalization layer into the value network of the hypernetwork. The authors test the compositional generalization of the proposed HYLA on two tasks: a fuzzy logic task and a symbolic Raven’s progressive matrices task. They show that the HYLA can outperform linear attention and softmax attention on these tasks.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
- The hypernetwork view of the attention mechanism is novel and interesting. It may provide further insights into the compositionality of the transformer models.
- The proposed HYLA is simple and effective on the tested tasks.

## Weaknesses
- The main weakness of this paper is the limited scope of the experiments. The authors only test the proposed HYLA on two small tasks. It is unclear if the advantage of the HYLA can be generalized to other tasks. In particular, the authors claim that their main motivation is to understand the compositionality of the transformer models. However, the tested tasks are not compositional in nature, and it is unclear how the proposed HYLA can improve the compositionality of the transformer models in real-world scenarios.

## Questions
- Can the authors test the HYLA on other tasks to show its general advantage over linear attention and softmax attention?
- Can the authors test the HYLA on tasks with real-world images instead of symbolic inputs? For example, the original Raven’s progressive matrices task.
- The authors mention that the HYLA can be extended to cross-attention. Can the authors test the HYLA on machine translation tasks and compare it with softmax attention, which is the mainstream approach for machine translation?
- Can the authors test the HYLA on language modeling tasks? Since language is compositional, it would be interesting to see if the HYLA can improve the language modeling performance.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4