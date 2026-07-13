# Review

## Summary
This paper introduces a novel Cross-Domain Distillation (CDD) framework for Fully Unsupervised Anomaly Detection (FUAD), which is a practical extension of Unsupervised Anomaly Detection (UAD) that detects anomalies without any labels, even when the training set may contain anomalous samples. The authors pioneer the introduction of the Knowledge Distillation (KD) paradigm based on the teacher-student framework into the FUAD setting. However, traditional KD methods risk enabling the student to learn the teacher's representation of anomalies, thereby resulting in poor anomaly detection performance. To address this issue, the authors propose a novel Cross-Domain Distillation (CDD) framework based on the reverse distillation (RD) paradigm. The proposed method achieves significant performance improvements over the baseline on the MVTec AD and VisA datasets, validating its effectiveness under the FUAD setting.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The authors pioneer the introduction of the Knowledge Distillation (KD) paradigm based on the teacher-student framework into the Fully Unsupervised Anomaly Detection (FUAD) setting.
2. The authors propose a novel Cross-Domain Distillation (CDD) framework based on the reverse distillation (RD) paradigm, which addresses the issue of traditional KD methods enabling the student to learn the teacher's representation of anomalies.
3. The proposed method achieves significant performance improvements over the baseline on the MVTec AD and VisA datasets, validating its effectiveness under the FUAD setting.

## Weaknesses
1. The novelty of the paper is limited, as the proposed method is an incremental improvement based on Reverse Distillation (RD) [1].
2. The proposed method is not compared with state-of-the-art methods such as MSFlow [2] and Real-IAD [3].
3. The proposed method is only validated on the MVTec AD and VisA datasets, which are relatively small datasets. The performance of the method on larger datasets such as Real-IAD [3] and VisA++ [4] is not explored.
4. The proposed method is not evaluated on the Real-IAD dataset under the no-overlap setting.
5. The proposed method is not evaluated on the PRO metric on the Real-IAD dataset under the no-overlap setting.
6. The proposed method is not evaluated on the PRO metric on the VisA dataset under the no-overlap setting.
7. The paper does not discuss the limitations of the proposed method.
8. The paper does not discuss the computational efficiency of the proposed method.
9. The paper does not discuss the scalability of the proposed method to larger datasets or more complex scenarios.
10. The paper does not discuss the generalizability of the proposed method to other types of anomaly detection tasks or datasets.

[1] Hui Deng, Xin Li: Anomaly Detection via Reverse Distillation From One-Class Embedding. CVPR 2022: 9737-9746
[2] Yize Zhou, Xiatian Zhu, Jie Song, Feng Shen, Hanjiang Lai: MSFlow: Multiscale Flow-Based Framework for Unsupervised Anomaly Detection. IEEE Trans. Neural Netw. Learn. Syst. 2024
[3] Chuan Wang, Wenhai Zhu, Bing-Bing Gao, Zhenguo Gan, Jie Zhang, Zhengong Gu, Song Qian, Mingchen Chen, Liang Ma: Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection. CVPR 2024: 22883-22892
[4] Jiaxuan Pang, Wenhai Zhu, Shengyu Huang, Chuan Wang, Song Qian, Mingchen Chen, Liang Ma: Multi-View Anomaly Detection: Towards Enhanced Realism and Generalizability. CoRR abs/2407.15161 (2024)

## Questions
See Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4