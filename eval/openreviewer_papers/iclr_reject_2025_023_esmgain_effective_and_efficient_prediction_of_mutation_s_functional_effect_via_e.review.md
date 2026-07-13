# Review

## Summary
This paper introduces ESM-Effect, a framework for predicting the functional effects of mutations in proteins. The authors address the limitations of existing methods by proposing a fine-tuning approach using ESM2 embeddings, which outperforms state-of-the-art competitors. They also establish a benchmarking framework with standardized datasets and metrics, emphasizing a new metric called relative Bin-Mean Error (rBME) for accurately assessing performance, particularly in rare gain-of-function regions. The study highlights the potential of ESM-Effect for clinical applications and identifies areas for further improvement, such as refining pretraining strategies.

## Soundness
3

## Presentation
2

## Contribution
2

## Strengths
- The paper introduces a novel framework, ESM-Effect, which enhances mutation functional effect prediction by fine-tuning ESM2 embeddings. 
- The study includes comprehensive ablation studies that explore different model configurations, such as model size scaling, fine-tuning strategies (LoRA vs. full fine-tuning), and regression head designs. 
- The authors propose a new metric, relative Bin-Mean Error (rBME), which is specifically designed to evaluate model performance, particularly for rare gain-of-function mutations. 
- The paper establishes a benchmarking framework that includes standardized datasets, evaluation metrics, and visualization techniques.

## Weaknesses
- The paper does not include a comparison with some of the latest methods in mutation pathogenicity prediction, such as those presented in [1,2,3,4].
- The paper does not provide a comprehensive comparison of computational efficiency between ESM-Effect and other methods, which would be valuable for assessing its scalability and practical applicability.
- The paper does not include a detailed error analysis or investigation of the model's failure modes, which would be valuable for understanding its limitations and potential areas for improvement.
- The paper could benefit from a more detailed discussion of the biological implications of the results, including how the findings might be interpreted in the context of known biological mechanisms or disease-associated variants.

[1] Saadat, Ali, and Jacques Fellay. "Fine-tuning the ESM2 protein language model to understand the functional impact of missense variants." arXiv preprint arXiv:2410.10919 (2024).

[2] Stein, David, et al. "Genome-wide prediction of pathogenic gain- and loss-of-function variants from ensemble learning of a diverse feature set." Genome Medicine 15.1 (2023): 103.

[3] Schmirler, Robert, Michael Heinzinger, and Burkhard Rost. "Fine-tuning protein language models boosts predictions across diverse tasks." Nature Communications 15.1 (2024): 7407.

[4] Lafita, Aleix, et al. "Fine-tuning Protein Language Models with Deep Mutational Scanning improves Variant Effect Prediction." arXiv preprint arXiv:2405.06729 (2024).

## Questions
- How does ESM-Effect compare to other recent methods in mutation pathogenicity prediction?
- What are the computational requirements for training and evaluating ESM-Effect, and how does this compare to other approaches?
- Can you provide more details on the biological interpretation of the model's predictions, particularly for rare gain-of-function mutations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
5

## Confidence
4