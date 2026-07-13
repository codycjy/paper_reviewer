# Review

## Summary
This paper studies the problem of generating a concise slate of statements that proportionally represents the full spectrum of user opinions. This problem is similar to committee elections, but unlike traditional settings, the candidate set comprises all possible statements of varying lengths, and so it can only be accessed through specific queries. The authors extend the framework in two fundamental ways, providing theoretical guarantees even in the face of approximately optimal queries and a budget limit on the overall length of the slate. Using GPT-4o to implement queries, they showcase their approach on datasets related to city improvement measures and drug reviews, demonstrating its effectiveness in generating representative slates from unstructured user opinions.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
1. The studied problem is interesting and important.
2. The paper is well-written and easy to follow.
3. The authors provide rigorous theoretical analysis for the proposed algorithm.
4. The authors conduct comprehensive experiments to evaluate the proposed method.

## Weaknesses
1. The running time of the proposed algorithm is quite high.
2. The technical novelty of the proposed algorithm is limited.

## Questions
1. The running time of the proposed algorithm is quite high. Can the authors provide a more detailed analysis of the running time of the proposed algorithm? How does the running time compare to other existing methods?
2. The technical novelty of the proposed algorithm is limited. Can the authors highlight the technical challenges and novelties of the proposed algorithm?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4