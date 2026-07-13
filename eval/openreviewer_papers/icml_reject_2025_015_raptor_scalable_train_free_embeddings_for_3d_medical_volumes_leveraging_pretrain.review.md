# Review

## Summary
The paper presents RAPTOR, a novel method for generating embeddings from 3D medical imaging data without requiring extensive computational resources or large datasets. RAPTOR leverages a pre-trained 2D foundation model (DINOv2-L) to extract features from individual cross-sectional views of a 3D volume, followed by random projections to reduce the spatial dimensions. This approach allows RAPTOR to achieve high-performance results across various tasks, including classification and regression, on multiple datasets, outperforming several state-of-the-art (SOTA) models. The method is particularly notable for its ability to perform well without the need for costly 3D model training.

## Soundness
4

## Presentation
4

## Contribution
3

## Strengths
1. The paper introduces a novel approach that leverages a pre-trained 2D foundation model and random projections to create embeddings for 3D data, which is both innovative and practical for data-scarce environments.
2. RAPTOR demonstrates strong performance across multiple datasets and tasks, including classification and regression, outperforming several state-of-the-art models.
3. The method avoids the need for costly 3D model training, which is a significant advantage in terms of computational efficiency.
4. RAPTOR is model-agnostic, meaning it can easily incorporate future advancements in 2D foundation models, making it a flexible choice for 3D data analysis.

## Weaknesses
1. While the method performs well across various tasks, it shows only modest performance on select datasets, such as the Fracture3D dataset, indicating that domain-specific priors or refining the axial sampling strategy could further improve results.
2. The paper primarily focuses on medical imaging data. It is unclear how well the method would generalize to other domains, such as Earth observation data or other volumetric data types.
3. The method relies on random projections, which may not capture all the nuances of complex 3D structures in some cases. This could potentially lead to a loss of information.

## Questions
1. How does RAPTOR handle variations in image quality or noise levels within the same dataset? Are there specific recommendations for preprocessing the data to ensure robustness across different modalities?
2. Could the authors provide more insight into how the choice of the number of projections (K) affects performance across different datasets and tasks? Is there a general guideline for selecting K?
3. How does RAPTOR perform on datasets with significant variations in size or resolution? Is there a recommended approach for handling such datasets to maintain performance?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4