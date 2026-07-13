# Review

## Summary
The paper presents a method for extracting finite automata from language models trained on regular languages. The method works by clustering the hidden states of the model and then using the clusters to construct a finite automaton. The authors demonstrate the effectiveness of the method on five regular languages, showing that the extracted automata can replicate the performance of the original model and even exhibit better generalization capabilities.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper presents a novel method for extracting finite automata from language models trained on regular languages. This approach allows for a better understanding of how language models encode knowledge and compress statistical regularities and patterns inherent in language.
- The authors conduct experiments on five regular languages with varying complexity, providing insights into the behavior of language models when applied to regular languages. The results demonstrate that context dependency is the dominant factor in language modeling complexity, which offers new perspectives on regular language complexity and the expressiveness of language models.

## Weaknesses
- The paper's scope is limited to regular languages, which are a fundamental concept in theoretical computer science but do not directly align with practical applications in natural language processing (NLP). While the findings provide insights into the behavior of language models on regular languages, it is unclear how these results can be generalized to more complex natural languages.
- The paper focuses on relatively small-scale language models compared to the state-of-the-art models in current NLP research. It is unclear how the proposed method would perform with larger models, and whether the findings would still be valid. This limits the potential impact and applicability of the research.
- The paper does not provide a comparison with other methods for extracting finite automata from language models or RNNs. It would be valuable to see how the proposed method compares with existing approaches in terms of accuracy, efficiency, and scalability. Without such comparisons, it is difficult to assess the relative strengths and weaknesses of the proposed method.

## Questions
- How do the findings on context dependency and regular language complexity relate to the behavior of language models on natural languages? Can the results be generalized to more complex linguistic structures and ambiguities present in natural language?
- What are the limitations of the proposed method for extracting finite automata from language models? How does the method perform with larger models or more complex regular languages? Are there any scalability issues or computational bottlenecks?
- How does the proposed method compare with other existing approaches for extracting finite automata from language models or RNNs? Can the authors provide empirical comparisons in terms of accuracy, efficiency, and scalability?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4