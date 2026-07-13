# Review

## Summary
This paper presents a method for blind face restoration. The authors propose to inject semantic prior into the diffusion model before performing degradation removal. The proposed method is evaluated on both synthetic and real-world datasets and achieves promising results.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is evaluated on both synthetic and real-world datasets and achieves promising results.

## Weaknesses
1. The authors claim that existing methods risk discarding subtle but crucial cues from already limited LQ inputs. However, there is a lack of evidence to support this claim. It is unclear what cues are being discarded and why the proposed method is able to retain these cues.
2. The authors should provide more details about the VLM used in the proposed method. What is the specific model and how is it trained?
3. The proposed method is compared with several existing methods, but some recent methods are missing, such as [1] and [2].
4. The authors should also evaluate the proposed method on the CelebA-Dataset and FFHQ-Dataset used in CodeFormer.
5. The authors should conduct more ablation studies to further analyze the proposed method. For example, what is the impact of the number of tokens used in the degradation mapper?

[1] Scaling up to excellence: Practicing model scaling for photo-realistic image restoration in the wild, CVPR 2024.

[2] Visual style prompt learning using diffusion models for blind face restoration, 2024.

## Questions
Please see the weaknesses above.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4