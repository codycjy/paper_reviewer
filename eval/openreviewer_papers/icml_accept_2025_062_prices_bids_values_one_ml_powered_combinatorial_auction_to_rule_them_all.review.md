# Review

## Summary
This paper studies the design of iterative combinatorial auctions (ICAs). The main challenge in this domain is that the bundle space grows exponentially in the number of items. To address this, recent work has proposed machine learning (ML)-based preference elicitation algorithms that aim to elicit only the most critical information from bidders to maximize efficiency. However, while the SOTA ML-based algorithms elicit bidders’ preferences via value queries, ICAs that are used in practice elicit information via demand queries. In this paper, the authors introduce a novel ML algorithm that provably makes use of the full information from both value and demand queries, and they show via experiments that combining both query types results in significantly better learning performance in practice.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
This paper is well written. The main idea of combining value and demand queries is interesting. The authors provide a rigorous theoretical analysis and extensive experimental results.

## Weaknesses
It is not clear how the queries are generated. Is it possible to generate the queries in a more efficient way? The authors may want to provide more discussion on this.

## Questions
1. It is not clear how the queries are generated. Is it possible to generate the queries in a more efficient way? The authors may want to provide more discussion on this.

2. The authors may want to provide more discussion on the societal impact of this work.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4