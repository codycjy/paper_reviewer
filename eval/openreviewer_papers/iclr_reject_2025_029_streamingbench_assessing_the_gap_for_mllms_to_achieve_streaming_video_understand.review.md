# Review

## Summary
This paper introduces a comprehensive benchmark designed to evaluate the streaming video understanding capabilities of MLLMs. The benchmark consists of 900 videos and 4300 human-curated QA pairs. The authors conduct experiments on 13 open-source and proprietary MLLMs and find that even the most advanced proprietary MLLMs like Gemini 1.5 Pro and GPT-4o perform significantly below human-level streaming video understanding capabilities.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The paper introduces a new benchmark for streaming video understanding. The benchmark is comprehensive, including 900 videos and 4300 QA pairs.
3. The authors conduct experiments on 13 open-source and proprietary MLLMs and provide a detailed analysis of the results.

## Weaknesses
1. The paper does not provide a detailed analysis of the impact of video length on model performance. It would be helpful to evaluate model performance on short videos (e.g., ≤ 5 seconds), medium-length videos (e.g., 5-15 seconds), and long videos (e.g., ≥ 30 seconds).
2. The paper does not provide a detailed analysis of the impact of audio on model performance. It would be helpful to evaluate the model's performance on videos with varying audio lengths, from no audio to very long audio.

## Questions
1. Does the performance of models decrease with the length of the video and the length of the audio?
2. What is the impact of video frame rate on model performance? What is the impact of different frame sampling strategies on model performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4