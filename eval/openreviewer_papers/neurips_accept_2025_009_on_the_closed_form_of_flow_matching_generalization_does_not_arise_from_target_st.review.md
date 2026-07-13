# Review

## Summary
This paper studies the generalization of flow matching models, i.e., why do flow matching models generalize well despite the risk of overfitting. The authors argue that the stochasticity of the conditional flow matching objective is not the main reason for generalization, contrary to a previous hypothesis. They show that the conditional and optimal velocity fields align closely in high dimensions and that the failure of the learned velocity field to match the optimal one is more important in explaining generalization. They propose a new training algorithm based on the optimal velocity field and show that it yields similar or better results than standard flow matching.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
This paper studies an important question, namely the generalization of flow matching models. The authors present a clear argument with well-designed experiments to support their claims. The presentation is clear and easy to follow. The proposed training algorithm based on the optimal velocity field is a nice contribution. Overall, this is a solid paper that makes an interesting contribution to the understanding and development of flow matching models.

## Weaknesses
I find the argument of the paper convincing. However, I think the title is slightly misleading. The authors show that the stochasticity of the objective is not the main reason for generalization, but they do not prove that it is not important at all. It would be more accurate to phrase the title as a question, e.g., "Does stochasticity of the loss drive generalization in flow matching?"

## Questions
1. In Figure 1a, what is the expected behavior in high dimensions? I guess the alignement should be close to 1 almost everywhere. What is the expected behavior close to $t=0$? 
2. In Figure 2, why is the training error increasing with the number of samples for $t\approx 0.15$? 
3. In Figure 3, the LPIPS distance drops sharply for $\tau>0.2$. Is there a reason for this? Is it related to the alignement between the conditional and optimal velocity fields around $t=0.4$?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4