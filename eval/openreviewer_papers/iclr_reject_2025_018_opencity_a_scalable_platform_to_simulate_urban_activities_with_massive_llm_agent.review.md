# Review

## Summary
The paper presents OpenCity, a scalable simulation platform optimized for both system and prompt efficiencies. OpenCity introduces a LLM request scheduler to reduce communication overhead by parallelizing requests through IO multiplexing. Besides, they deisgn a "group-and-distill" prompt optimization strategy minimizes redundancy by clustering agents with similar static attributes.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper is well-written and easy to understand.
2. The paper proposes a high-performance platform OpenCity that introduces system-level LLM request scheduler and prompt-level “group-and-distill” strategy to reduce LLM agent simulation time. OpenCity maintains high fidelity in simulated behaviors while achieving an average 635x acceleration.

## Weaknesses
1. The paper lacks discussion on related work. For example, [1] also proposes a platform for urban simulation using LLMs.
2. The paper lacks ablation studies to prove the effectiveness of the proposed modules.
3. The paper lacks a comparison of the proposed platform with existing urban simulators, such as [1].
4. The paper lacks an evaluation of the accuracy of the proposed simulator. For example, how well does the simulator capture human mobility patterns compared to real-world data?

[1] UrbanSim: An Agent-Based Framework for Large-Scale Urban Simulation Using Large Language Models.

## Questions
Please refer to the Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4