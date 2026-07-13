# Review

## Summary
This paper introduces CacheFlow, a flow-based method for human motion prediction that achieves fast inference by precomputing and caching the results of an unconditional generative model. The method maps historical motion trajectories to a Gaussian mixture model, enabling efficient conditional prediction. CacheFlow demonstrates significant speed improvements over previous methods while maintaining accuracy.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The paper is well-written and easy to follow.
- The proposed method is novel and technically sound.
- The experiments are comprehensive and the results are promising.

## Weaknesses
- The authors should provide a more detailed analysis of the computational efficiency and scalability of CacheFlow. How does the method perform with larger datasets or more complex motion patterns? Are there any trade-offs between speed and accuracy?
- The authors should include a comparison of CacheFlow with other state-of-the-art methods on the AMASS dataset.
- The authors should provide a more in-depth discussion of the potential real-world applications of CacheFlow, such as in robotics or VR. How could the method be integrated into these systems and what kind of improvements could it bring?

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4