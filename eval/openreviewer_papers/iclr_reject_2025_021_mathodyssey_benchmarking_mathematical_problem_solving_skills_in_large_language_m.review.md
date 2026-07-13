# Review

## Summary
The paper introduces the MathOdyssey dataset, a benchmark designed to evaluate the mathematical problem-solving abilities of large language models (LLMs). The dataset encompasses a wide range of problems at various difficulty levels, from high school to university and olympiad levels, covering subjects such as algebra, number theory, geometry, and combinatorics. The authors conducted experiments with several LLMs, including GPT-4, GPT-3.5, and Llama-3, to assess their performance on this benchmark. The results indicate that while LLMs perform well on routine and moderately difficult tasks, they face significant challenges with olympiad-level problems and complex university-level questions. The paper also highlights a narrowing performance gap between open-source and closed-source models, emphasizing the ongoing need for research to enhance the mathematical reasoning capabilities of LLMs.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The MathOdyssey dataset is a significant contribution to the field. It provides a comprehensive collection of mathematical problems that can be used to evaluate and benchmark LLMs. The dataset's breadth, covering a wide range of difficulty levels and subjects, makes it a valuable resource for researchers.

2. The experiments conducted in the paper are thorough and well-structured. The authors evaluate multiple LLMs, including both open-source and closed-source models, using various prompting techniques. The results provide insights into the current capabilities and limitations of LLMs in mathematical problem-solving.

3. The paper is well-written and clearly presents the dataset, experimental setup, and results. The authors provide detailed explanations and examples, making it easy for readers to understand the content.

## Weaknesses
1. While the MathOdyssey dataset is a valuable contribution, the paper does not introduce any novel methods or approaches for improving the mathematical reasoning capabilities of LLMs. The experiments primarily focus on evaluating existing models using the new benchmark, without proposing new techniques or frameworks.

2. The paper lacks a comparison with other mathematical datasets or benchmarks. It would be beneficial to include a comparison to understand how the MathOdyssey dataset complements or improves upon existing resources. This could help in highlighting the unique aspects and advantages of the new dataset.

3. The experiments in the paper primarily focus on a few specific LLMs, such as GPT-4, GPT-3.5, and Llama-3. A broader evaluation involving a wider range of LLMs, especially smaller or less powerful models, would provide a more comprehensive understanding of the dataset's effectiveness and challenges. This could help in identifying the dataset's applicability to a broader range of models.

4. The paper does not provide any analysis of the errors made by the LLMs. A detailed error analysis could offer insights into the specific challenges faced by LLMs when solving mathematical problems, guiding future research directions and improvement strategies.

## Questions
1. How does the MathOdyssey dataset compare to other existing mathematical benchmarks in terms of its scope, difficulty, and originality? Are there any unique features or advantages that set it apart from other datasets?

2. The experiments primarily focus on a few LLMs. How do smaller or less powerful LLMs perform on the MathOdyssey dataset? Would the inclusion of such models provide a more comprehensive evaluation?

3. The paper does not provide an in-depth analysis of the errors made by the LLMs. Could the authors provide examples of common mistakes or patterns observed in the LLMs' solutions? How could such an analysis guide future research directions?

4. Are there any plans to expand the MathOdyssey dataset in the future? How could the dataset be enhanced to cover a wider range of mathematical concepts or problem-solving scenarios?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4