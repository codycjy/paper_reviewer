# Review

## Summary
The authors propose a stochastic sparse sampling framework for the classification of variable length medical time series data. The proposed method consists of a local model that makes predictions on fixed length windows of the input time series, and an aggregation function that combines the local predictions to produce a global prediction. The authors demonstrate the efficacy of the proposed framework on a seizure onset zone (SOZ) detection task using a large multi-centre iEEG dataset. The authors also demonstrate that their proposed framework generalizes well to unseen medical centres.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The paper is well written and easy to follow.
- The authors demonstrate that their proposed method outperforms the baselines on the SOZ detection task.

## Weaknesses
- The technical novelty of the proposed method is limited. There are many existing methods that use a similar strategy of making local predictions on fixed length windows of the input time series and then aggregating the local predictions to produce a global prediction (for example [1]). 
- The authors have not compared their proposed method with any existing methods that make local predictions and then aggregate them. 
- The authors have not described how they have combined their proposed framework with the PatchTST backbone. 
- The authors have not discussed the limitations of their proposed method. 

[1] Early, Joseph, et al. "Inherently interpretable time series classification via multiple instance learning." The Twelfth International Conference on Learning Representations. 2024.

## Questions
- How is the proposed framework combined with the PatchTST backbone? 
- How does the proposed framework generalize to other medical time series classification tasks? 
- What is the computational complexity of the proposed framework?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4