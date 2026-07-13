# Review

## Summary
This paper introduces a new dataset, MathOdyssey, which contains 387 mathematical problems at three levels: Olympiad-level, High School, and University-level. The authors collected these problems from mathematics professionals, including high school educators, researchers, and university professors. The dataset contains a total of 387 problems, including 244 open-answer questions, 127 multiple-choice questions, and 16 true-false questions. The authors evaluated the performance of six LLMs on this dataset and found that all of them performed poorly on Olympiad-level problems. The authors released the dataset and the evaluation code.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The dataset contains a variety of problems at different levels and different subject areas. The problems are original and not sourced from previous datasets or textbooks, which reduces the risk of data contamination.

2. The authors evaluated the performance of six LLMs on this dataset, which provides a benchmark for future research.

## Weaknesses
1. The dataset is relatively small, with only 387 problems. This can limit the generalizability of the results and make it difficult to draw robust conclusions about the performance of LLMs on a wider range of mathematical problems.

2. The evaluation method is not very sophisticated. The authors used GPT-4 to assist in evaluating model accuracy, especially for open-answer questions. This can introduce some subjectivity and may not accurately reflect the true performance of the models.

3. The paper does not provide any in-depth analysis of the results. While the authors present the performance of the different models, they do not discuss the reasons behind the differences in performance or provide any insights into how the models could be improved.

## Questions
1. How did you verify the quality of the generated solutions? Were they all correct?

2. Have you considered using more sophisticated evaluation methods, such as using symbolic mathematics software to verify the correctness of the solutions?

3. Have you analyzed the errors made by the LLMs? Are there any common patterns or weaknesses that the models exhibit when solving these problems?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4