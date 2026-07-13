# Review

## Summary
The authors present a foundation model for multi-modal wearable sensor data. They use a channel-aware attention mechanism to encode the time-series data. The model is trained in a self-supervised manner and can be used in a zero-shot setting. The authors show results on 18 downstream tasks across 11 datasets.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper is well written and easy to follow
- The authors have done a great job in summarizing the related work
- The authors have done an extensive evaluation of their model on various downstream tasks

## Weaknesses
- The paper lacks novelty. The authors have used the standard masked auto-encoder framework with minor modifications. 
- The authors have not compared their model with existing multi-modal foundation models like TimeMixer and Chronos. 
- The authors have not provided an ablation study of the different components of their model. 
- The authors have not provided details about the hyperparameter tuning of their model and the baselines. 
- It is unclear how the authors have used the baseline models for the multi-modal datasets. 
- The improvements of the proposed model over the baselines are marginal.

## Questions
- What is the rationale behind using the continuous wavelet transform? Have the authors experimented with other time-frequency representations like the short-time Fourier transform? 
- The authors mention that they have used the [CLS] token as a liaison token. Have they experimented with other tokens? 
- How does the proposed model compare to other multi-modal foundation models? 
- What is the computational complexity of the proposed model? 
- How have the authors tuned the hyperparameters of their model and the baselines?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4