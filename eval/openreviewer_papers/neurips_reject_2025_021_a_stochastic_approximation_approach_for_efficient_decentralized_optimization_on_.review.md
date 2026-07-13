# Review

## Summary
This paper studies decentralized optimization over random networks. Using a primal-dual algorithm, the authors show how to achieve $\mathcal{O}(\sigma/\sqrt{nT})$ convergence rate for the expected squared gradient norm.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
The paper is well-written and easy to follow. The authors propose a primal-dual algorithm and achieve a convergence rate of $\mathcal{O}(\sigma/\sqrt{nT})$ for the expected squared gradient norm. This is a good result and matches the convergence rate of decentralized SGD with gradient compression.

## Weaknesses
1. The random networks considered in this paper are not well-motivated. The authors consider a random graph where each edge is independently activated with a constant probability. This model is quite different from the dynamic networks considered in the existing literature, e.g., Kovalev et al. 2021, 2024. In their model, the graph is activated at each time step, and the mixing matrix is different at each time step. This makes the analysis of gradient tracking algorithms challenging. However, in this paper, the mixing matrix is the same at each time step, which makes the analysis much easier. I suggest the authors consider the dynamic network model in Kovalev et al. 2021, 2024 and provide convergence analysis for the proposed algorithm in this setting. 

2. The convergence rate of the proposed algorithm is not surprising. In the deterministic setting, the algorithm becomes the gradient tracking algorithm, and the convergence rate is the same as the existing gradient tracking algorithms. In the stochastic setting, the algorithm is the primal-dual algorithm, and the convergence rate is the same as the existing primal-dual algorithms. The analysis seems to be a combination of the existing gradient tracking algorithms and primal-dual algorithms. The authors need to highlight the technical challenges and provide more intuition behind the analysis. 

3. The authors should provide more discussion on the comparison between the proposed algorithm and the existing algorithms. For example, what are the advantages of the proposed algorithm? Does the proposed algorithm have a lower communication cost than the existing algorithms? Does the proposed algorithm have a faster convergence rate than the existing algorithms? The current comparison is not sufficient. 

4. The authors should provide more discussion on the connection between the proposed algorithm and the existing algorithms. For example, the authors should explain how the proposed algorithm reduces the communication cost. 

5. The authors should provide numerical results to show the advantages of the proposed algorithm. For example, the authors should provide numerical results to show that the proposed algorithm has a lower communication cost than the existing algorithms.

## Questions
Please see the weaknesses above.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4