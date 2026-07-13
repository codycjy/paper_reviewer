# Review

## Summary
This paper proposes a new gating update mechanism for MoE-based meta-learning, which is suitable for the scenario of generalizing to different dynamical systems. The authors use k-means clustering to get the labels for the gating network, and then solve the least square problem to get the optimal weights. The authors test the proposed method on several ODE benchmarks, as well as some other datasets.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The authors provide a new gating update mechanism for MoE-based meta-learning, which seems to be more suitable for the scenario of generalizing to different dynamical systems.
2. The authors provide a detailed description of the proposed method, and the paper is easy to follow.
3. The authors test the proposed method on several ODE benchmarks, as well as some other datasets.

## Weaknesses
1. The motivation of this paper is not clear. The authors claim that the existing MoE-based meta-learning methods are not suitable for generalizing to different dynamical systems, but do not provide a detailed explanation of the problem. It is not clear why the existing methods are not suitable and what difficulties they will meet. This part is important since it is the key to the proposed method.
2. The proposed method is not well-motivated. The authors claim that the existing MoE-based meta-learning methods are not suitable for generalizing to different dynamical systems because of the gradient-based gating update mechanism. However, they do not provide a detailed explanation of the problem. Why will the gradient-based gating update mechanism meet difficulties in this scenario? The authors should provide some theoretical or empirical analysis to support their claim.
3. The authors do not provide a detailed explanation of why the proposed k-means and least squares-based gating update mechanism is suitable for the scenario of generalizing to different dynamical systems. Why can the proposed method overcome the difficulties met by the gradient-based gating update mechanism? The authors should provide some theoretical or empirical analysis to support their claim.
4. The experiments are not sufficient. The authors only test the proposed method on some ODE benchmarks, but do not provide a comparison with other MoE-based meta-learning methods on these benchmarks. It is not clear how the proposed method performs compared with the existing methods.
5. The authors do not provide a detailed analysis of the experimental results. Why does the proposed method perform well on some datasets but not on others? What are the reasons behind the experimental results? The authors should provide some theoretical or empirical analysis to support their claims.

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4