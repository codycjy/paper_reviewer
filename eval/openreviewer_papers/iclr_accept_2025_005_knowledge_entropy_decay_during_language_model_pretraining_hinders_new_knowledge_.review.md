# Review

## Summary
This paper introduces the concept of "knowledge entropy" to quantify how broadly a language model integrates its stored knowledge during pretraining. The authors argue that as pretraining progresses, models tend to use a narrower set of memory vectors, leading to lower knowledge entropy and impaired ability to acquire new knowledge. They support this with experiments showing that models in the final stages of pretraining exhibit higher forgetting rates and lower knowledge acquisition compared to mid-stage models.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The introduction of knowledge entropy provides a new perspective on how models integrate knowledge during pretraining. This concept could have broader applications in understanding model behavior.
- The paper presents a clear narrative with well-defined hypotheses and experiments to support them. The resuscitation experiment is particularly clever and provides strong evidence for the knowledge entropy claims.
- The authors provide a thorough analysis across multiple dimensions (knowledge entropy, attention entropy, next-token prediction entropy) to support their claims.
- The paper is well-written and easy to follow, with clear explanations of the methodology and results.

## Weaknesses
- While the resuscitation experiment shows promise, it's a somewhat crude method and doesn't fully restore the model's plasticity. More sophisticated methods for modifying parameters could yield better results.
- The paper focuses on OLMo models, so it's unclear if these findings generalize to other architectures. More experiments across different model types would strengthen the claims.
- The paper doesn't explore how to effectively identify the "mid-point" in pretraining where models strike a good balance between knowledge retention and acquisition. More work is needed to develop methods for identifying this optimal point.

## Questions
- Have you tried more sophisticated methods for resuscitating inactive memory vectors? How do they compare to the simple scaling approach?
- How do your findings generalize to other language model architectures? Have you done any preliminary experiments to test this?
- What methods do you propose for identifying the optimal "mid-point" in pretraining for different model architectures?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4