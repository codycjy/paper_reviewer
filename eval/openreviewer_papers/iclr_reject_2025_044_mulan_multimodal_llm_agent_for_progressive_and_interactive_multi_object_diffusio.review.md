# Review

## Summary
This paper presents a training-free paradigm for text-to-image generation using a multimodal-LLM agent. It effectively addresses the challenge of multi-object generation by employing a progressive approach with feedback control, which allows for better handling of spatial relationships and attribute bindings. The paper also introduces a strategy for multi-object occlusion in T2I generation, resulting in improved image quality and realism. Additionally, a dataset of prompts is curated to evaluate multi-object composition with spatial relationships and attribute bindings in T2I tasks, demonstrating the method's superior performance compared to existing controllable generation methods and general T2I generation methods.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well-written and easy to follow. The idea of progressively generating each object in the scene is interesting.
- The proposed method achieves good results in the evaluation.

## Weaknesses
- The proposed method requires multiple rounds of inference, which can be time-consuming.
- The paper lacks a comparison of inference times with other methods. Additionally, it would be beneficial to include a comparison with training-based methods such as GLIGEN, as the proposed approach appears to have a similar number of inference steps as GLIGEN's 2D layout.
- The paper does not provide a comparison with other methods for object occlusion, such as AnyDoor [1].
- The method may face difficulties when the generated object is partially visible or requires the generation of fine-grained details, as these can only be achieved by adjusting the size of the object. In such cases, the VLM may not be able to provide accurate feedback.

[1] Chen, Xi, et al. "Anydoor: Zero-shot object-level image customization." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

## Questions
- How does the proposed method perform in terms of inference time compared to other methods?
- How does the proposed method perform in terms of object occlusion compared to other methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4