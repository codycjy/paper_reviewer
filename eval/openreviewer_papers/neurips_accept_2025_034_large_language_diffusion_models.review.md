# Review

## Summary
This paper presents a new diffusion-based model for text generation called LLaDA. LLaDA is trained using a masked diffusion process where tokens are masked independently with probability t. The model is trained using maximum likelihood estimation and the loss is an upper bound on the negative log-likelihood. The authors train LLaDA from scratch in a pretraining and SFT paradigm, and find that it achieves competitive performance with autoregressive models on various tasks, including in-context learning and instruction-following. LLaDA also performs well on reversal reasoning tasks, where autoregressive models typically struggle.

## Soundness
3

## Presentation
4

## Contribution
4

## Strengths
- This paper presents a significant contribution to the field of language modeling by introducing a new diffusion-based model that can be trained from scratch using standard pretraining and SFT techniques. The model achieves competitive performance with state-of-the-art autoregressive models on various tasks, including in-context learning and instruction-following, while also exhibiting unique capabilities such as bidirectional modeling and enhanced robustness. 
- The paper provides a comprehensive evaluation of the model's performance on a wide range of tasks, including language understanding, math, code, and Chinese. The authors also conduct ablation studies to analyze the impact of different components of the model, such as the masked diffusion process and the remasking strategy during sampling. 
- The paper is well-written and easy to follow. The authors provide clear explanations of the model's architecture, training procedure, and evaluation methodology. They also include detailed descriptions of the datasets used for training and evaluation, as well as the evaluation protocols followed. 
- The work has the potential to inspire further research into diffusion-based language models, leading to the development of even more advanced models with improved performance and capabilities.

## Weaknesses
- The paper does not provide a detailed analysis of the computational efficiency of LLaDA compared to autoregressive models. While it mentions that LLaDA is less efficient during training, it does not provide a comprehensive analysis of the trade-offs between training time, model size, and performance for LLaDA and autoregressive models. 
- The paper does not provide a detailed analysis of the impact of different hyperparameters on LLaDA's performance, such as the number of sampling steps, the mask ratio, and the learning rate. While it mentions that the authors "made several necessary modifications" to the hyperparameters compared to autoregressive models, it does not provide a comprehensive analysis of how these hyperparameters affect LLaDA's performance and convergence. 
- The paper does not provide a detailed analysis of the impact of different components of the model on LLaDA's performance, such as the use of different attention mechanisms or position embeddings, or the incorporation of special techniques during training. While it mentions that LLaDA does not use a causal mask and incorporates a forward data masking process, it does not provide a comprehensive analysis of how these components affect LLaDA's performance and convergence.

## Questions
- How does the computational efficiency of LLaDA compare to autoregressive models during training and inference? What are the trade-offs between model size, training time, and performance for LLaDA and autoregressive models?
- How do different hyperparameters, such as the number of sampling steps, the mask ratio, and the learning rate, affect LLaDA's performance and convergence? How did the authors determine the optimal values for these hyperparameters?
- How do different components of the model, such as the use of different attention mechanisms or position embeddings, or the incorporation of special techniques during training, affect LLaDA's performance and convergence? How does LLaDA compare to autoregressive models in terms of the types of data and tasks that it can effectively handle?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4