# Review

## Summary
This paper proposes a simple yet effective training-free method, MARINE, to reduce the object hallucination problem of LVLMs. MARINE integrates object-level information from various image-grounded models into LVLMs' text generation process. Experimental results show that MARINE reduces object hallucination across multiple LVLMs and outperforms existing fine-tuning-based methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The method is simple yet effective, and the paper is easy to follow.
2. MARINE can be easily integrated into various LVLMs.
3. The experimental results show that MARINE outperforms existing fine-tuning-based methods.

## Weaknesses
1. The proposed method relies on the accuracy of the image-grounded models. However, these models may also produce hallucinations. It is unclear how MARINE mitigates hallucinations when the image-grounded models are unreliable. Additionally, there is no discussion on how to select reliable image-grounded models for MARINE.
2. MARINE introduces additional vision models during inference, increasing computational costs and inference time. The authors should provide a detailed analysis of the latency and costs associated with different image-grounded models.
3. There is a lack of discussion on the limitations of the proposed method.

## Questions
1. In Table 1, the performance of MARINE with LLaVA is significantly better than that of other methods. However, with LLaVA-v1.5 and mPLUG-Owl2, the performance of MARINE is similar to or worse than that of other methods. Could you explain this phenomenon?
2. The hallucination problem also exists in image captioning. Does MARINE perform well in this task?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4