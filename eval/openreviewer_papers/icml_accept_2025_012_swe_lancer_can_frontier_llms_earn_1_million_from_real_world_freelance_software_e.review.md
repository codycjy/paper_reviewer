# Review

## Summary
The paper introduces a new benchmark for SWE tasks, with a unique focus on management tasks, and tasks that require end-to-end testing. The benchmark also has a unique focus on real-world tasks, with real-world payoffs. The paper shows that current LLMs perform poorly on the benchmark.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
- The paper presents a novel benchmark for SWE tasks. The benchmark has a unique focus on management tasks and on end-to-end testing, which are both very important for real-world software engineering. 
- The benchmark has a unique focus on real-world tasks, with real-world payoffs. 
- The paper shows that current LLMs perform poorly on the benchmark, which points to opportunities for future research. 
- The paper is very well-written, with a clear and concise explanation of the benchmark and the evaluation.

## Weaknesses
- The benchmark only uses tasks from one company, Expensify. While the company seems to be large and diverse, it would be beneficial to include tasks from other companies as well. This would help to ensure that the benchmark is representative of a wide range of real-world software engineering tasks, and it would also help to reduce the risk of the benchmark being biased towards the specific company used. 
- The benchmark does not include any tasks related to security, which is an important aspect of software engineering. 
- The benchmark does not include any tasks related to infrastructure engineering, such as refining Kubernetes cluster architectures or debugging pod failures, node crashes, or networking problems. These types of tasks are an important part of software engineering in practice, but they are not covered by the benchmark. 
- The paper does not provide a detailed analysis of the performance of the models on different types of tasks within the benchmark. For example, it would be helpful to see how well the models perform on different levels of tasks, such as bug fixes versus new feature implementations, or on different domains such as web applications versus mobile applications. 
- The paper does not provide a detailed analysis of the errors made by the models. For example, it would be helpful to see the most common types of errors made by the models, the difficulty of the tasks that the models failed, and any patterns or trends in the errors.

## Questions
- How do you plan to address the limitations of the benchmark, such as the lack of security-related tasks and infrastructure engineering tasks? Do you have plans to expand the benchmark to include these types of tasks in the future?
- Can you provide a more detailed analysis of the performance of the models on different types of tasks within the benchmark? For example, how well do the models perform on different levels of tasks, such as bug fixes versus new feature implementations, or on different domains such as web applications versus mobile applications?
- Can you provide a more detailed analysis of the errors made by the models? For example, what are the most common types of errors made by the models, what are the difficulty levels of the tasks that the models failed, and are there any patterns or trends in the errors?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4