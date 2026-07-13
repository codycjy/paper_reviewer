# Review

## Summary
The authors propose RAPTOR, a method that leverages pretrained 2D foundation models (DINOv2) to extract features from 2D slices of 3D volumes. These features are then spatially compressed using random projections. The authors evaluate their method on 10 diverse medical volume tasks, showing superior performance compared to other methods.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well written and easy to follow. The authors provide clear explanations of their method and the experimental setup.
- The authors provide a theoretical justification for their choice of random projections.
- The method is evaluated on a wide range of medical imaging tasks, demonstrating its versatility.

## Weaknesses
- The method relies on the assumption that the 2D slices are "smooth", which may not always be true in medical imaging.
- The method is evaluated on a fixed set of hyperparameters. It would be interesting to see how the performance varies with different choices of K.

## Questions
- How does the performance of RAPTOR vary with different choices of K?
- How well does the method generalize to other types of 3D data, such as point clouds or meshes?
- How sensitive is the method to the choice of the 2D foundation model?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4