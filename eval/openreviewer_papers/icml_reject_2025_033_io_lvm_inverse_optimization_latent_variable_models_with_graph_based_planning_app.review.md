# Review

## Summary
This paper proposes IO-LVM, a latent variable model for constrained optimization problems, which utilizes a COP solver within the generative process to ensure the feasibility of the generated samples. The authors validate IO-LVM on synthetic and real-world datasets, demonstrating its effectiveness in capturing underlying COP cost structures and identifying solutions associated with different agents or conditions.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. This paper is well-written and easy to follow.
2. The paper introduces IO-LVM, a novel approach for learning latent representations of COP costs, which can recover observed path distributions without making assumptions about inferred paths.

## Weaknesses
1. The novelty of this paper is limited. The IO-LVM proposed in this paper is a simple combination of existing methods, including VAE and FY loss.
2. The experimental results are not convincing. The authors only compare IO-LVM with VAE, without comparing it to other state-of-the-art methods mentioned in the related work section.

## Questions
1. Why is the perturbed Fenchel-Young loss used instead of the original Fenchel-Young loss?
2. Can the authors provide more details on how IO-LVM ensures the generation of feasible solutions?
3. Can the authors compare IO-LVM with other state-of-the-art methods mentioned in the related work section?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4