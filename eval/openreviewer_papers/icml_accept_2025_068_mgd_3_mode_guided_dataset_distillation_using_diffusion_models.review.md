# Review

## Summary
This paper proposes a mode-guided diffusion model for dataset distillation, which can leverage a pre-trained diffusion model without the need to fine-tune with distillation losses. The experiments demonstrate the effectiveness of the proposed method.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper is well-written and easy to follow.
2. The proposed method is interesting and novel.
3. The experiments are extensive and the results are promising.

## Weaknesses
1. The proposed method seems to be sensitive to the hyper-parameters. For example, the mode guidance scale $\lambda$ and the timestep $t_{stop}$. The authors should provide some ablation studies on these hyper-parameters.
2. The authors should provide more details about the mode discovery stage. For example, how to use the VAE encoder to capture the overall content of the image. In addition, the proposed method seems to be sensitive to the mode discovery algorithm. The authors should provide more discussion on this issue.
3. The authors should provide a more detailed analysis of the distilled dataset. For example, how many modes can the proposed method capture? Whether the proposed method can capture all the modes of the dataset?

## Questions
See the weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4