# Review

## Summary
This paper proposes a new framework, MASS, for optimizing the prompts and topologies of multi-agent systems (MAS). The authors first conduct an in-depth analysis of the design space and reveal that prompts play a critical role in building effective MAS. Based on this, they propose MASS, which efficiently exploits the MAS design space by interleaving its optimization stages from local to global, from prompts to topologies, over three stages. The experiments demonstrate that MASS-optimized MAS outperform existing alternatives by a substantial margin. The authors also provide design principles behind building effective MAS.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The paper provides an in-depth analysis of the design factors that influence the performance of MAS, highlighting the importance of prompts.

2. The paper proposes a novel multi-stage optimization framework, MASS, that automates the optimization of MAS by efficiently searching within a pruned design space.

3. The experiments demonstrate that MASS-optimized MAS outperform existing manual and automated approaches across a wide range of tasks.

4. The authors provide valuable design principles and guidelines for building effective MAS, which can benefit future research and development in this field.

## Weaknesses
1. The proposed MASS framework is only tested on specific LLMs (Gemini 1.5 and Claude 3.5), and it is unclear how well it generalizes to other LLMs or models.

2. The paper does not provide a detailed analysis of the computational resources required for implementing MASS, such as inference time, memory usage, and API costs.

3. The paper does not provide a detailed analysis of the potential risks and limitations of using MASS, such as potential biases, errors, or ethical considerations.

## Questions
1. How well does the MASS framework generalize to other LLMs or models not included in the experiments?

2. What are the computational resources required for implementing MASS, such as inference time, memory usage, and API costs?

3. What are the potential risks and limitations of using MASS, such as potential biases, errors, or ethical considerations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4