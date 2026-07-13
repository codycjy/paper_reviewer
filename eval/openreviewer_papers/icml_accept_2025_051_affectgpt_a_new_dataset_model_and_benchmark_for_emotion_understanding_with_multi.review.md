# Review

## Summary
This paper aims to advance the emotional understanding capabilities of multimodal large language models (MLLMs) through the introduction of a new dataset, model, and benchmark. The authors propose MER-Caption, a large-scale dataset featuring over 115,000 samples with fine-grained emotion labels. They also develop AffectGPT, a model designed to enhance multimodal integration using pre-fusion operations. Additionally, they present MER-UniBench, a comprehensive benchmark for evaluating multimodal emotion recognition (MER) tasks. The paper reports extensive experimental results demonstrating the effectiveness of AffectGPT across various MER tasks and provides resources to advance research in emotion understanding.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper introduces a novel dataset, MER-Caption, which is the largest descriptive emotion dataset to date, featuring over 115,000 samples with fine-grained emotion categories. This dataset addresses a significant gap in the current community, which lacks large-scale datasets with intensive, descriptive emotion annotations.

2. The authors develop AffectGPT, a new model designed to enhance multimodal integration using pre-fusion operations. This model demonstrates robust performance across various MER tasks, outperforming existing MLLMs.

3. The paper presents MER-UniBench, a unified benchmark with tailored evaluation metrics for typical MER tasks. This benchmark provides a comprehensive framework for evaluating the performance of MLLMs in emotion understanding.

## Weaknesses
1. The paper could benefit from a more detailed comparison with existing datasets and models in the field. While Table 1 provides a summary of existing emotion datasets, a more in-depth comparison highlighting the specific advantages and limitations of MER-Caption would strengthen the contribution.

2. The paper mentions that the AffectGPT model uses pre-fusion operations to enhance multimodal integration but does not provide a detailed explanation of these operations. More technical details and an ablation study on the impact of pre-fusion operations would be beneficial.

3. The paper could address potential biases in the dataset, especially since it is generated from a model-based crowdsourcing technique. A discussion on the potential biases in the data and how they are mitigated would enhance the reliability of the dataset.

## Questions
1. Can you provide more technical details about the pre-fusion operations used in the AffectGPT model? How do these operations enhance multimodal integration?

2. How does the AffectGPT model handle modality conflict, where inconsistencies or contradictions arise between different modalities?

3. What are the potential biases in the MER-Caption dataset, and how are they mitigated?

4. Can you provide more details on the two-level filtering process used to enhance the label quality of the MER-Caption dataset?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4