# Review

## Summary
This paper studies the problem of aggregating statements from a set of users. The authors propose an algorithm that produces a slate of statements that represents the users' opinions in a proportional way. The algorithm is implemented using LLMs and tested on real-world datasets.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well-written and the problem is well-motivated. The theoretical results are interesting and the experiments are convincing.

## Weaknesses
I think that the authors should have included a discussion about the computational complexity of the algorithm. It seems to me that the algorithm is quite complicated and its running time is not guaranteed. It would be useful to have a more detailed analysis of the algorithm's complexity and a discussion about its running time.

## Questions
1. What is the computational complexity of the algorithm?
2. How do you determine the length of the statements in the slate? Is this done automatically or do you need to specify it beforehand?
3. How do you handle the case where the statements are too long and do not fit within the budget?
4. How do you ensure that the statements in the slate are diverse enough? Is there a risk of having too similar statements in the slate?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4