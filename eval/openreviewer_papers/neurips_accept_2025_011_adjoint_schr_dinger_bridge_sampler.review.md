# Review

## Summary
This paper proposes a new diffusion sampler that employs simple and scalable matching-based objectives without the need to estimate target samples during training. The proposed method is based on Schrodinger bridge, which enhances sampling efficiency via kinetic-optimal transportation. Extensive experiments demonstrate the effectiveness of the proposed method.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The proposed method is based on Schrodinger bridge, which enhances sampling efficiency via kinetic-optimal transportation.
2. The authors provide theoretical analysis for the proposed method.
3. Extensive experiments demonstrate the effectiveness of the proposed method.

## Weaknesses
1. The proposed method is based on adjoint matching, which is proposed by [1]. Although the proposed method has its own advantages compared to [1], the novelty of the proposed method seems to be limited.
2. The proposed method requires alternating optimization, which may be time-consuming.

## Questions
1. The authors mention that the proposed method can solve the non-memoryless condition. However, it seems that the experiments are still based on the memoryless condition, such as the Gaussian prior. Can the authors provide some experiments based on non-memoryless condition?
2. The authors mention that the proposed method can solve the non-memoryless condition. However, it seems that the proof of Theorem 3.2 still requires the memoryless condition. Can the authors provide the proof without the memoryless condition?
3. The proposed method requires alternating optimization, which may be time-consuming. Can the authors provide the running time of the proposed method and compare it with other methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4