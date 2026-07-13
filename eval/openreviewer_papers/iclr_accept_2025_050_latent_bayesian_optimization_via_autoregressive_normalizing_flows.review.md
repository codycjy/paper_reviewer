# Review

## Summary
The paper introduces a new approach to latent Bayesian optimization (LBO) by using normalizing flows to establish a one-to-one mapping between the input space and the latent space, addressing the value discrepancy problem inherent in previous LBO methods. The proposed NF-BO framework incorporates an autoregressive normalizing flow model (SeqFlow) and a token-level adaptive candidate sampling strategy (TACS) to improve the efficiency and effectiveness of the optimization process. The authors validate their method through extensive experiments on molecule generation tasks, demonstrating superior performance compared to traditional and recent LBO approaches.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The use of normalizing flows for establishing a one-to-one encoding function from the input space to the latent space is a novel contribution that effectively addresses the value discrepancy problem.
- The paper provides a comprehensive experimental evaluation, including comparisons with several state-of-the-art LBO methods, demonstrating the advantages of the proposed approach.
- The introduction of TACS is a valuable addition, as it dynamically adjusts the sampling distribution based on token-level importance, which can lead to more efficient exploration and better optimization outcomes.

## Weaknesses
- The paper does not provide a detailed analysis of the computational complexity or runtime comparisons of the proposed method against existing LBO approaches.
- While the experiments are extensive, the paper could benefit from additional ablation studies to isolate the contributions of different components of the proposed method, such as the impact of the autoregressive flow model versus the TACS strategy.
- The paper could provide more insights into the interpretability of the learned latent space and how it relates to the original input space, which is important for understanding and trusting the optimization results.

## Questions
1. Can the authors provide more details on the computational complexity of NF-BO compared to other LBO methods? How does the runtime scale with the size of the input space and the number of iterations?
2. How sensitive is the performance of NF-BO to the choice of hyperparameters, such as the temperature parameter in TACS? Is there a systematic way to determine optimal hyperparameters?
3. Can the authors provide more insights into how the learned latent space is interpretable? Are there any visualizations or case studies that illustrate the relationship between latent variables and the original inputs?
4. How generalizable is the proposed approach beyond molecule generation tasks? Have the authors considered applications in other domains, such as materials design or protein engineering?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4