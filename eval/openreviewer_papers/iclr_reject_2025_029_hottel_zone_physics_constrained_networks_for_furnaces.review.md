# Review

## Summary
This paper presents a novel approach to improve temperature profile prediction in furnaces using a physics-constrained neural network (PCNN) based on the Hottel Zone method. The authors reformulate the Hottel Zone Method’s Directed Flux Areas (DFAs) and Energy Balance (EB) equations in tensor format, enabling neural network training, and introduce a novel regularization technique that imbues the network with physics-awareness. The proposed method is evaluated on various neural network architectures, including MLP, LSTM, xLSTM, and KAN, and compared against existing methods.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper presents a novel integration of physics-based constraints into a neural network framework, specifically applied to furnace temperature profiling.
2. The authors provide a comprehensive evaluation of their method across multiple neural network architectures, demonstrating its effectiveness and robustness.
3. The proposed method shows significant improvements in prediction accuracy compared to traditional and other state-of-the-art methods.

## Weaknesses
1. The paper lacks a detailed discussion on the computational efficiency and scalability of the proposed method, particularly for large-scale industrial applications.
2. The authors do not provide a thorough sensitivity analysis of the hyperparameters used in the regularization terms, which could affect the model's performance.
3. The paper does not include a detailed comparison of the proposed method with physics-informed neural networks (PINNs) or other physics-constrained machine learning approaches.
4. The authors do not provide a clear discussion of the limitations of their work and potential areas for future research.

## Questions
1. How does the computational efficiency of the proposed method compare to traditional approaches, and how scalable is it for large-scale industrial applications?
2. Can the authors provide a more detailed sensitivity analysis of the hyperparameters used in the regularization terms, and how do these affect the model's performance?
3. How does the proposed method compare to physics-informed neural networks (PINNs) or other physics-constrained machine learning approaches in terms of accuracy and computational efficiency?
4. What are the limitations of the proposed method, and what are the potential areas for future research to further improve the accuracy and applicability of the method?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4