# Review

## Summary
This paper proposes a discrete spatial diffusion model (DSD) that maintains mass conservation during image generation. DSD is suitable for applications that require strict mass preservation, such as scientific data. The model achieves this by using a forward process based on random walks, which preserves mass in both forward and reverse processes. DSD is evaluated on standard benchmarks and specific scientific data, such as materials microstructure.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- DSD is suitable for applications requiring strict mass conservation, such as scientific data, where traditional diffusion models fall short.
- The model is evaluated on both standard benchmarks (MNIST and CelebA) and real scientific data (e.g., materials microstructure, rock microstructures, and lithium-ion electrodes).
- The authors provide the code, enabling reproducibility and further exploration of DSD.

## Weaknesses
- The novelty of DSD is limited, as it primarily modifies the forward process by adding constraints to the existing discrete diffusion framework.
- The paper lacks comparisons with other discrete diffusion models, such as those based on Markov chains, which would help to better position DSD within the broader landscape of discrete diffusion models.
- The evaluation on standard benchmarks (MNIST and CelebA) is limited, with minimal comparisons to other methods. Expanding these experiments to include a wider range of datasets and comparisons would strengthen the empirical validation.
- DSD is not compared to continuous diffusion models on standard tasks, which would provide a more comprehensive assessment of its performance.

## Questions
- How does DSD compare to other discrete diffusion models, such as those based on Markov chains, in terms of performance and suitability for scientific applications?
- Can DSD be extended to handle other types of constraints beyond mass conservation, and if so, how would this be achieved?
- How does DSD perform on standard image generation tasks compared to state-of-the-art continuous diffusion models?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4