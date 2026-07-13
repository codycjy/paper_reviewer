# Review

## Summary
The paper presents a data-driven method to identify key amino acids that distinguish between paralogous proteins using the Shapley value-based feature subset selection algorithm, SVEA. By analyzing 15 pairs of paralogous proteins, the authors demonstrate that small amino acid subsets (5-10 amino acids) can effectively distinguish between protein pairs. The method is computationally efficient, requiring less data compared to traditional approaches, and is validated through multiple methods, including multiple sequence alignment, 3D structure analysis, and literature evidence.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
1. The method is computationally efficient and requires less data compared to traditional approaches.
2. The method is validated through multiple methods, including multiple sequence alignment, 3D structure analysis, and literature evidence.
3. The paper is well-written and easy to follow.

## Weaknesses
1. The authors used a Monte Carlo-based approximation algorithm for Shapley values, which is known to be exponentially time-consuming as the number of features increases. However, the number of features in this paper is relatively small (20), so the time cost of this step should be reported and compared.
2. The authors did not compare their method with other feature selection methods (e.g., MCI) or with other methods that identify key amino acids in proteins (e.g., machine learning methods based on mutational data).
3. The authors did not validate their method on large-scale datasets. For example, they could use the largest paralogous protein family in UniProt to train and test the model.
4. The authors did not provide a detailed analysis of the biological significance of the identified amino acids or their functional roles in the protein structure.
5. The authors did not discuss the limitations of their method or potential biases in the data or results.
6. The authors did not discuss how their method could be improved or extended in future work.

## Questions
1. What are the time and computational resource costs of the method?
2. How does the method perform compared to other feature selection or key amino acid identification methods?
3. How does the method perform on large-scale datasets?
4. What is the biological significance of the identified amino acids?
5. What are the limitations of the method, and are there potential biases in the data or results?
6. How could the method be improved or extended in future work?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4