# Review

## Summary
This paper proposes a new method to address the issue of hallucination in LVLMs. The method uses the output of grounding models as additional information to guide the generation process of LVLMs, which can mitigate hallucination without the need for additional training. The paper demonstrates the effectiveness of this method on several benchmarks.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper is clearly written and easy to understand.
2. The proposed method is simple and effective, and does not require additional training or API calls.
3. The paper provides a comprehensive evaluation of the method on multiple benchmarks and models.

## Weaknesses
1. The method proposed in this paper is too simple. It basically describes the objects detected by the grounding model in the prompt, which is equivalent to manually filtering out the hallucinated content. It is not surprising that this method can improve the performance on the CHAIR and POPE benchmarks. However, this method may not work well on other benchmarks that are not related to object hallucination, and may even damage the performance of LVLMs. For example, the method may reduce the hallucination of LVLMs on the LLaVA-QA90 benchmark, but the performance of LVLMs on other benchmarks such as MMBench and MME may decline.
2. The method proposed in this paper is similar to the method of using prompts to constrain LVLMs. The difference is that the prompt in this paper is dynamically generated based on the output of the grounding model. Therefore, the authors should compare this method with the baseline of directly using manually designed prompts to constrain LVLMs, such as the prompts in Table 19. If the performance of this method is similar to that of manually designed prompts, then this method is not as good as the method of using the output of the grounding model to constrain LVLMs, because the latter is more flexible and does not require manual design.
3. The method proposed in this paper is only applicable to the issue of object hallucination in LVLMs, and cannot solve other types of hallucinations. Moreover, the performance of this method on object hallucination may be due to the fact that the grounding model can only detect objects. If the grounding model is replaced with a model that can detect more visual concepts, such as a large multimodal model, can the performance be further improved? If so, does this mean that the reason for the hallucination of LVLMs is that the visual model is not powerful enough?

## Questions
See weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4