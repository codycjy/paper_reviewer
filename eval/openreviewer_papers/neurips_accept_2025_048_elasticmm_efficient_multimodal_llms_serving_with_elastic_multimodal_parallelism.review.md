# Review

## Summary
The paper presents a new system design for serving multimodal large language models. The main idea is to separate the system into two-level hierarchies, where the first is the modality level and the second is the stage level. The modality level is designed to handle the load imbalance between text and multimodal requests, while the stage level is designed to handle the load imbalance within each modality. The paper also presents several optimization techniques to reduce the overhead of vision encoding and improve the system throughput. The evaluation results show that the proposed design outperforms existing systems, including vLLM and DistServe.

## Soundness
3

## Presentation
2

## Contribution
2

## Strengths
+ Multimodal LLM is a hot research area. The paper studies an important and timely problem of serving multimodal LLMs. 

+ The proposed design is a reasonable extension of existing systems. The paper also presents several practical optimizations to improve the performance.

+ The evaluation results show that the proposed design outperforms existing systems.

## Weaknesses
- The proposed design is a straightforward extension of existing systems, specifically vLLM and DistServe. While this is not necessarily a bad thing, it limits the technical novelty of the paper. 

- The evaluation results are not comprehensive enough. For example, it is unclear how the proposed design performs under different request distributions. The paper only considers two datasets, VisualWebInstruct and ShareGPT-4o, which may not be representative enough. It would be better if the paper could provide more extensive evaluation results, such as those under different request distributions and system workloads.

## Questions
- What is the system overhead of the proposed optimizations? For example, how does the asynchronous encoding affect the system throughput?

- How does the proposed design perform under different request distributions and system workloads?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4