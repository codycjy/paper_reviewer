# Review

## Summary
This paper proposes a new algorithm for solving the optimal transport (OT) problem. The proposed algorithm is called Hierarchical Refinement (HiRef) and is designed to handle large-scale datasets by dynamically constructing a multiscale partition of each dataset using low-rank OT subproblems. The key innovation of HiRef is the introduction of a hierarchical refinement strategy that recursively co-clusters points with their image under the Monge map, which is a bijective optimal transport map between the datasets. The authors provide a theoretical result (Proposition 3.1) that proves the optimality of the low-rank factors and show that HiRef has linear space complexity and log-linear time complexity. The authors evaluate HiRef on several datasets, including synthetic datasets, large-scale matching problems, and the MERFISH Mouse Brain Receptor Map data, demonstrating its ability to scale to over a million points and compute high-quality alignments.

## Soundness
4

## Presentation
4

## Contribution
4

## Strengths
1. The paper introduces a novel algorithm, Hierarchical Refinement (HiRef), which addresses the scalability limitations of existing optimal transport (OT) solvers by leveraging low-rank OT subproblems and a recursive refinement strategy. This approach is innovative in combining hierarchical partitioning with low-rank approximation to handle large-scale datasets.

2. The theoretical results presented in the paper, particularly Proposition 3.1, provide a solid foundation for the proposed algorithm. The authors prove that the low-rank factors optimally co-cluster points with their image under the Monge map, which is a bijective optimal transport map between the datasets. This theoretical contribution enhances the understanding of optimal transport and its application to large-scale datasets.

3. The experimental evaluation of HiRef is comprehensive, covering synthetic datasets, large-scale matching problems, and real-world datasets like the MERFISH Mouse Brain Receptor Map data. The results demonstrate HiRef's ability to scale to over a million points and compute high-quality alignments, outperforming existing solvers in terms of primal cost and computational efficiency. The experiments are well-designed and provide strong evidence for the effectiveness of the proposed method.

4. The paper is well-structured and clearly written. The authors provide a detailed explanation of the proposed algorithm, including its theoretical foundations and implementation details. The use of figures and tables to illustrate the results further enhances the clarity of the presentation.

## Weaknesses
1. The paper does not provide a detailed analysis of the computational complexity of HiRef beyond the log-linear time complexity. It would be beneficial to include a more thorough complexity analysis, especially regarding the constant factors and the impact of the rank schedule.

2. While the experimental evaluation is comprehensive, it would be valuable to include a comparison with more baselines, particularly other state-of-the-art solvers for large-scale optimal transport problems. This would provide a more complete picture of HiRef's performance relative to existing methods.

3. The paper could benefit from a more detailed discussion of the limitations of HiRef, including the assumptions made and the potential scenarios where HiRef may not perform optimally. This would enhance the transparency and usefulness of the proposed method.

## Questions
1. Can you provide a more detailed analysis of the computational complexity of HiRef, including the constant factors and how they scale with the dataset size?

2. How does HiRef perform compared to other state-of-the-art solvers for large-scale optimal transport problems? Are there any specific scenarios where HiRef excels or falls short?

3. Can you provide more insights into the limitations of HiRef, including the assumptions made and the potential scenarios where HiRef may not perform optimally?

4. How sensitive is HiRef to the choice of rank schedule? Can you provide guidelines or heuristics for selecting an appropriate rank schedule for different datasets?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4