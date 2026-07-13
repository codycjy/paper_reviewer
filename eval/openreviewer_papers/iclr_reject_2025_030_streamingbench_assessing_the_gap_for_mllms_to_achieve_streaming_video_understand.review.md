# Review

## Summary
This paper introduces a comprehensive benchmark, StreamingBench, for assessing the streaming video understanding capabilities of MLLMs. The benchmark consists of 900 videos and 4,300 human-curated QA pairs. The authors conduct experiments on StreamingBench with 13 open-source and proprietary MLLMs and find that even the most advanced proprietary MLLMs like Gemini 1.5 Pro and GPT-4o perform significantly below human-level streaming video understanding capabilities.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The benchmark is comprehensive, covering a wide range of real-world scenarios, and the questions are manually curated to ensure high relevance to streaming video scenarios.

## Weaknesses
1. While the paper presents a thorough evaluation of existing MLLMs on the benchmark, it does not include experiments with any streaming MLLMs, such as VideoLLM-online and Flash-VStream. This omission is significant, as it leaves unanswered the question of how well these models, which are designed for streaming video understanding, perform on the benchmark. Including these experiments would provide a more complete picture of the strengths and limitations of current MLLMs in this domain.
2. The paper does not provide any analysis of the impact of video length on model performance. This is a crucial aspect to consider, as the length of video content can significantly affect the understanding capabilities of MLLMs. A thorough analysis of how video length influences performance across different models would provide valuable insights into the limitations and potential areas for improvement in current MLLMs.

## Questions
Please see the weakness.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
5