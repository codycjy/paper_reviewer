# Review

## Summary
The paper introduces a new dataset, model, and benchmark aimed at advancing emotion understanding using multimodal large language models (MLLMs). The key contributions include:
1. MER-Caption Dataset: A large-scale dataset with over 115K samples featuring fine-grained emotion annotations, created using a model-led, human-assisted annotation strategy.
2. AffectGPT Model: A novel model architecture that enhances multimodal integration through pre-fusion operations, leading to improved performance in emotion recognition tasks.
3. MER-UniBench Benchmark: A comprehensive evaluation benchmark with tailored metrics for assessing multimodal emotion recognition tasks, supporting free-form, natural language outputs from MLLMs.
4. Experimental Results: Extensive evaluations demonstrate AffectGPT's superior performance across various emotion recognition tasks, highlighting the dataset's quality and the model's effectiveness.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a large-scale descriptive emotion dataset, MER-Caption, which addresses the lack of such resources in the community. The dataset's scale and the innovative annotation strategy are notable strengths.
2. The AffectGPT model is well-designed with pre-fusion operations that enhance multimodal integration, demonstrating significant performance improvements over existing models.
3. The paper provides a comprehensive benchmark, MER-UniBench, with tailored evaluation metrics suitable for the natural language output style of MLLMs, facilitating more accurate and nuanced emotion recognition assessments.
4. The experimental results are robust, showcasing the effectiveness of both the new dataset and model, with significant performance gains across various tasks, which underscores the practical impact of the contributions.

## Weaknesses
1. While the paper mentions a two-level filtering process for the dataset, more details on the criteria and methods used for filtering could strengthen the clarity and reliability of the dataset quality.
2. The paper could benefit from a more in-depth discussion on the limitations of the current approach and potential directions for future research, which would provide a more balanced perspective.

## Questions
1. Could you provide more details on the human prior-based model selection for the generation model and the rationale behind choosing SALMONN, Chat-UniVi, and GPT-3.5 for audio, video, and multimodal cue generation, respectively?
2. What are the specific criteria used for the low-level and high-level filtering processes, and how are these criteria determined?
3. How do you address potential biases in the dataset, and what steps are taken to ensure the diversity and representativeness of the emotion annotations?
4. Can you elaborate on the design choices made for the pre-fusion operations, and how these contribute to the overall performance of the AffectGPT model?
5. How does the AffectGPT model handle conflicting or complementary signals from different modalities (e.g., audio and video), and what is the impact on performance?
6. What are the computational requirements for training and deploying the AffectGPT model, and how do these compare to existing MLLMs?
7. How does the model perform across different types of emotional expressions, especially subtle or cultural nuances, and what are the limitations in this regard?
8. How does the AffectGPT model handle context-dependent emotional expressions, where the emotional state may change rapidly within a conversation or video?
9. What are the specific challenges encountered in the annotation process, and how are these overcome to ensure the quality and consistency of the emotion labels?
10. How does the AffectGPT model compare with other state-of-the-art models in terms of interpretability, and what methods are used to explain the model's decision-making process?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4