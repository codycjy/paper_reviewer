# Review

## Summary
This paper introduces MuLan, a training-free multimodal-LLM agent designed to progressively generate multi-object images with intricate planning and feedback control. MuLan leverages a large language model (LLM) to decompose a prompt into a sequence of sub-tasks, generating each object individually. Additionally, a vision-language model (VLM) provides feedback to the diffusion model to ensure each sub-task aligns with the original prompt, allowing for human intervention if needed. The results demonstrate that MuLan outperforms existing baselines in generating multiple objects and shows promise in collaborative human-AI scenarios.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is intuitive and well-motivated. It is a reasonable solution to decompose the generation of multi-object images into a sequential pipeline.
2. The proposed method demonstrates promising performance compared to the baselines.
3. The paper is well-written and easy to follow.

## Weaknesses
1. The proposed method requires multiple rounds of LLM and VLM inference, which may result in high latency. The authors should report the latency of their method and compare it with the baselines.
2. The proposed method relies on the output of the LLM, which may not be reliable in all cases. The authors should discuss the limitations of their method and report the failure cases.
3. The proposed method is only evaluated on two base models, SD1.4 and SDXL. The authors should evaluate their method on more base models, such as PixArt and SD3.
4. The authors should compare their method with more baselines, such as AnyDoor and Composable Diffusion.
5. The authors should also evaluate their method on T2I-CompBench to facilitate a more comprehensive comparison.

## Questions
Please see the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4