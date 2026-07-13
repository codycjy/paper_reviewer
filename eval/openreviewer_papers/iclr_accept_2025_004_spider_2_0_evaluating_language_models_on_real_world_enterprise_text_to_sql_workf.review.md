# Review

## Summary
The paper introduces Spider 2.0, a new benchmark for evaluating language models on real-world enterprise text-to-SQL tasks. Spider 2.0 includes 632 complex workflow problems derived from real-world use cases, featuring databases with over 1,000 columns and diverse operations from data transformation to analytics. Unlike previous benchmarks, Spider 2.0 challenges models to interact with complex SQL environments, process long contexts, understand intricate reasoning, and generate multi-step SQL queries. The evaluations reveal significant room for improvement, with the best-performing code agent framework achieving only 21.3% success rate. This highlights the complexity and realism of Spider 2.0 compared to traditional text-to-SQL benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper introduces a new benchmark, Spider 2.0, that addresses the real-world complexities of enterprise text-to-SQL workflows, such as handling diverse database systems and SQL dialects, and performing data transformations.
- The paper provides a comprehensive dataset with 632 workflow problems derived from real-world use cases, featuring large databases and complex SQL queries, which is a significant contribution to the field.
- The paper includes detailed evaluations of state-of-the-art language models, revealing the challenges and limitations of existing models in handling real-world enterprise text-to-SQL tasks, which provides valuable insights for future research.
- The paper conducts a thorough error analysis, identifying specific challenges such as schema linking, dialect function usage, and intricate query planning, which helps in understanding the complexities of the tasks.

## Weaknesses
- The paper does not provide a detailed comparison with previous text-to-SQL benchmarks, making it difficult to assess the specific improvements and challenges posed by Spider 2.0 compared to existing datasets.
- The paper could benefit from a more in-depth analysis of the specific SQL constructs and database features that are most challenging for language models, which could guide future research and model development.

## Questions
- Can you provide more detailed comparisons with previous benchmarks, such as Spider 1.0 and BIRD, to highlight the specific differences and challenges of Spider 2.0?
- Can you provide more insights into the most common SQL constructs and database features that language models struggle with, and how these relate to the performance on Spider 2.0?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4