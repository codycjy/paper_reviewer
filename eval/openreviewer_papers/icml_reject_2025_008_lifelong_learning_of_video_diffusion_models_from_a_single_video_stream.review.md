# Review

## Summary
This paper explores the possibility of learning video diffusion models from a single, continuous video stream in a lifelong learning setting. The authors demonstrate that training video diffusion models in this way can be as effective as standard offline training, given the same number of gradient steps. They also introduce three new datasets specifically designed for evaluating lifelong video model learning.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The paper is well-written and easy to follow. The authors clearly explain their motivation, methodology, and results, making it accessible to a wide range of readers.

2. The paper introduces three new datasets, which contribute to the field by providing a way to evaluate lifelong video model learning.

## Weaknesses
1. The paper's technical contribution appears limited, as it primarily focuses on applying the continual learning technique of experience replay to video diffusion models without introducing any new methods. This may not offer significant insights beyond the existing literature on continual learning and video generation.

2. The experimental results are not sufficiently convincing. Firstly, the paper lacks a comparison with other continual learning methods, which would provide a more comprehensive evaluation of the proposed approach. Secondly, the datasets used in the experiments are all synthetic or simple, which may not adequately represent real-world scenarios.

## Questions
1. The paper lacks a comparison with other continual learning methods. Could the authors include such a comparison in future work?

2. The datasets used in the experiments are all synthetic or simple. Could the authors consider using more complex datasets in future work?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4