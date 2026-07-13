# Review

## Summary
This paper proposes a new LoRA-based fine-tuning method for multimodal large language models (MLLMs). The authors identify that current efficient multimodal fine-tuning methods often overlook the intrinsic differences of multimodal scenarios and do not fully utilize all modalities. To address this issue, they introduce a multimodal-aware efficient fine-tuning strategy called MokA, which compresses unimodal information using modality-specific parameters while explicitly enhancing cross-modal interaction. The authors conduct extensive experiments covering three representative multimodal scenarios (audio-visual-text, visual-text, and speech-text) and multiple large language model (LLM) backbones (LLaMA2/3, Qwen2, Qwen2.5-VL, etc.). The results consistently demonstrate the efficacy and versatility of the proposed method. Ablation studies and efficiency evaluations further validate the effectiveness of MokA.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. This paper introduces a novel fine-tuning method, MokA, which is specifically designed for multimodal large language models (MLLMs). It addresses the limitations of current efficient multimodal fine-tuning methods by considering the intrinsic differences of multimodal scenarios and fully utilizing all modalities.

2. The authors conduct extensive experiments covering three representative multimodal scenarios (audio-visual-text, visual-text, and speech-text) and multiple large language model (LLM) backbones (LLaMA2/3, Qwen2, Qwen2.5-VL, etc.). The results consistently demonstrate the efficacy and versatility of the proposed method.

3. Ablation studies and efficiency evaluations further validate the effectiveness of MokA. The paper provides a thorough analysis of the proposed method, including its strengths and weaknesses, as well as suggestions for future research directions.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational efficiency of MokA. While it mentions a slight increase in inference latency compared to standard LoRA, a more comprehensive evaluation of the computational cost and scalability of MokA would be beneficial.

2. The paper could benefit from a more detailed comparison with other multimodal learning methods. While it compares MokA with LoRA and its variants, a comparison with other state-of-the-art multimodal learning methods would provide a better understanding of the advantages and limitations of MokA.

## Questions
1. How does MokA compare to other state-of-the-art multimodal learning methods in terms of computational efficiency and scalability?

2. Have you considered extending MokA to handle more than three modalities? What challenges do you anticipate in such extensions, and how might the method need to be adapted?

3. How does MokA perform when dealing with noisy or incomplete data in any of the modalities? Does the performance degrade significantly, and are there any strategies to mitigate such issues?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4