# Review

## Summary
The paper investigates the knowledge of language encoded in neural language models by training language models on strings matching certain regular expressions and then recovering the knowledge in the form of finite automaton using the proposed LaMFA method. The empirical results on regular languages of varying complexity show that the proposed method can extract DFA that consistently replicate the performance of the original language model. Moreover, the extracted DFAs exhibit enhanced generalization capabilities.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
The paper is well-written and easy to follow.

The proposed method is novel and interesting.

The empirical results on regular languages of varying complexity show that the proposed method can extract DFA that consistently replicate the performance of the original language model. Moreover, the extracted DFAs exhibit enhanced generalization capabilities.

## Weaknesses
The paper lacks a discussion of the limitations of the proposed method.

The paper lacks a discussion of the potential applications of the proposed method.

The paper only evaluates the proposed method on regular languages of varying complexity, which may not reflect its performance on more complex languages or real-world data.

The paper only evaluates the proposed method on two architectures, LSTM and GPT, which may not reflect its performance on other architectures.

## Questions
What are the limitations of the proposed method?

What are the potential applications of the proposed method?

How does the proposed method perform on more complex languages or real-world data?

How does the proposed method perform on other architectures?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4