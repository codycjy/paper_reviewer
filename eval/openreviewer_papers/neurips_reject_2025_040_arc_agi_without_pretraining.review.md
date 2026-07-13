# Review

## Summary
The paper introduces CompressARC, a model that solves ARC-AGI puzzles without any pretraining by minimizing the description length (MDL) during inference time. CompressARC can solve 20% of evaluation puzzles and 34.75% of training puzzles by leveraging MDL's generalization abilities. The model's architecture is specifically designed for the puzzle task and requires 2000 steps per puzzle to achieve optimal performance. The paper also provides a case study on "Color the Boxes" puzzle and analyzes the model's behavior and decision-making process.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper presents a novel approach to solving ARC-AGI puzzles by using MDL and inference time learning, which is different from traditional methods that rely on pretraining.
2. The paper provides a detailed explanation of the MDL principle and how it can be used for solving ARC-AGI puzzles. The paper also includes a thorough literature review on related work.
3. The paper includes a comprehensive evaluation of the model's performance on both training and evaluation sets, as well as a case study to provide insights into the model's behavior.

## Weaknesses
1. The paper does not provide a clear explanation of how MDL can be applied to other tasks or domains beyond ARC-AGI puzzles. The paper also does not discuss the limitations of MDL or potential challenges in applying it to more complex tasks.
2. The paper does not provide a comparison with other methods or approaches for solving ARC-AGI puzzles, such as those presented in previous research or other competing models.
3. The paper does not provide a detailed analysis of the computational resources required to run CompressARC, such as memory or processing time, or how they compare to other methods.
4. The paper does not provide a clear explanation of the role of each layer in the model's architecture and how they contribute to the overall performance. The paper also does not provide a detailed analysis of the model's sensitivity to hyperparameters or other training settings.

## Questions
1. How can the MDL principle be applied to other tasks or domains beyond ARC-AGI puzzles? What are the potential challenges or limitations?
2. How does CompressARC compare to other methods or approaches for solving ARC-AGI puzzles in terms of performance, computational resources, or efficiency?
3. Can you provide a more detailed analysis of the model's sensitivity to hyperparameters or other training settings? How do these affect the model's performance and generalization abilities?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4