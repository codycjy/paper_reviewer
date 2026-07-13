# Review

## Summary
This paper proposes a novel deep learning framework called Seq2Exp for gene expression prediction that integrates DNA sequences and epigenomic signals to discover and extract regulatory elements driving target gene expression. The key contributions are:
- A framework articulating the causal relationships between epigenomic signals, DNA sequences, target gene expression, and related regulatory elements.
- A method that combines the mask probability distribution from DNA sequences and epigenomic signals, filtering out non-causal regions using an information bottleneck.
- State-of-the-art performance compared to previous gene expression prediction baselines, with the extracted regulatory elements serving as better subsequences than statistical peak-calling methods for epigenomic signals like MACS3.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- Novel framework integrating DNA sequences and epigenomic signals for gene expression prediction.
- Theoretical foundation using information bottleneck and Beta distribution for mask modeling.
- State-of-the-art performance on gene expression prediction task.
- The extracted regulatory elements are biologically meaningful and improve interpretability.

## Weaknesses
- The paper only evaluates on two cell types, limiting generalizability. Expanding to more cell types would strengthen the claims.
- The framework assumes independent effects of DNA sequences and epigenomic signals, which may not fully capture complex interactions.
- The causal relationships and information bottleneck assumptions could be more rigorously validated experimentally.

## Questions
- How does the model handle potential false positive regulatory elements identified by the mask?
- What is the computational complexity of the method compared to baseline approaches?
- How does the performance scale with increasing epigenomic signal dimensions?
- Could the framework be extended to predict other genomic features beyond gene expression?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4