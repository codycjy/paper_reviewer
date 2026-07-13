# Review

## Summary
This paper introduces an unsupervised visual anomaly detection model for 3D CT images. The method is based on density estimation of learned feature maps. The authors propose to use self-supervised learning to train the feature extractor, replacing the common practice of using supervised pre-trained models. The authors also propose to use self-supervised learned features as conditions for the density model. The proposed method is compared with several anomaly detection methods on multiple medical datasets, showing superior performance.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The proposed method is well-motivated. The use of SSL feature extractor is a good alternative to supervised pre-trained models. 
- The paper is well-written and easy to follow.
- The proposed method is technically sound.
- The experiments are extensive and the results are promising.

## Weaknesses
- The paper is missing a related work section, which makes it hard to see how the proposed method fits in the literature and to identify the novelty of the method. 
- The novelty of the method is not clear. Using SSL feature extractor and self-supervised learned features as conditions are both common practices in many computer vision tasks. 
- The ablation study is not complete. It is not clear which part of the method contributes the most to the performance gains. 
- The method is only evaluated on CT images. It is not clear if the method is generalizable to other imaging modalities.

## Questions
- The authors should add a related work section to discuss how the proposed method fits in the literature and identify the novelty of the method. 
- The authors should add more ablation studies to analyze the contribution of each component of the method. 
- The authors should discuss the generalizability of the method to other imaging modalities. 
- The authors should discuss the limitations of the method.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4