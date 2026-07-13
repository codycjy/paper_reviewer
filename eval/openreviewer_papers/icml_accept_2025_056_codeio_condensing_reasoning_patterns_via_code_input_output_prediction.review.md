# Review

## Summary
The paper presents a novel approach to improving the reasoning capabilities of LLMs by training them to predict code inputs and outputs in natural language chain-of-thought (CoT) rationales. The authors introduce the CODEI/O dataset, which condenses diverse reasoning patterns from code into a format that enhances LLMs' ability to generalize across various reasoning tasks. They also propose CODEI/O++, an enhanced version that utilizes code execution feedback for multi-turn revisions, further improving model performance. Experimental results demonstrate that these approaches lead to consistent improvements across multiple reasoning benchmarks.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel way to improve reasoning in LLMs by leveraging code execution as a form of supervision. This is a fresh perspective that goes beyond traditional text-based supervision, exploiting the structured nature of code to enhance reasoning capabilities.
2. The creation of the CODEI/O dataset, which is large-scale and diverse, is a significant contribution. It provides a rich source of training data that captures a wide range of reasoning patterns, which can be used to improve performance on various reasoning tasks.
3. The experimental results are comprehensive, covering a wide range of reasoning benchmarks. The results demonstrate consistent improvements across these benchmarks, indicating the effectiveness of the proposed approach in enhancing reasoning capabilities.

## Weaknesses
1. While the paper demonstrates the effectiveness of CODEI/O on various reasoning tasks, it would be beneficial to see how it performs on more complex, real-world reasoning tasks, such as legal reasoning or medical decision-making. This would help in understanding its applicability in more sensitive domains.
2. The paper could benefit from a more detailed discussion on the limitations of the proposed approach. For instance, are there certain types of reasoning tasks or code structures where CODEI/O does not perform as well? Addressing these limitations would provide a more balanced view of the approach's capabilities.

## Questions
1. How does the performance of LLMs trained with CODEI/O compare to those trained with traditional text-based supervision on more complex reasoning tasks, such as legal reasoning or medical decision-making?
2. Can you provide more insights into the limitations of the CODEI/O approach? Are there specific types of reasoning tasks or code structures where it does not perform as well?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4