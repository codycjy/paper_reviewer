# Review

## Summary
This paper introduces the Core Sentiment Inventory (CSI), a new evaluation tool designed to assess the implicit sentiment tendencies of large language models (LLMs). Inspired by the Implicit Association Test (IAT), CSI aims to provide a reliable and valid measure of LLMs' optimism, pessimism, and neutrality in both English and Chinese. The authors argue that existing psychometric methods, such as the Big Five Inventory (BFI), are limited in their reliability and validity when applied to LLMs. Through experiments with several state-of-the-art LLMs, the authors demonstrate that CSI yields more consistent results, reduces reluctance rates, and exhibits predictive power in sentiment-related tasks.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
- The CSI is designed to be bilingual (English and Chinese), allowing for a more comprehensive assessment of LLMs' sentiment tendencies across different languages and cultural contexts.
- The experiments reveal that CSI significantly reduces reluctance rates, indicating that LLMs are more willing to engage with the test items, which is a crucial improvement over traditional methods.
- The paper provides a detailed analysis of the results, including sentiment profiles of mainstream models, reliability assessments, and validity assessments. This analysis offers valuable insights into the emotional tendencies of LLMs and how these tendencies vary across languages and contexts.

## Weaknesses
- The paper does not clearly explain how the CSI score is calculated. While the authors describe the Optimism Score, Pessimism Score, and Neutral Score, they do not provide a comprehensive formula or explanation of how these scores are combined to generate the overall CSI score.
- The study only assesses the models' sentiment associations with the words in the CSI, but it does not evaluate how these sentiments manifest in the models' responses to open-ended questions or scenarios. This limitation reduces the generalizability of the findings to real-world applications where LLMs may need to express more nuanced sentiments.
- The study focuses primarily on GPT-4, GPT-3.5 Turbo, Qwen2-72B, and Llama3.1-70B, which are all relatively large models. It would be valuable to see how CSI performs with smaller LLMs or models trained on smaller datasets. This could provide insights into how the reliability and validity of CSI are affected by model size and training data.
- The paper does not provide a comparison of CSI with other psychometric methods beyond BFI. It would be beneficial to see how CSI performs in comparison to other methods, such as the Implicit Emotional Inventory (IEI) or the Affective Lexicon Inventory (ALI), which are designed to assess the implicit emotions of LLMs.

## Questions
- How is the CSI score calculated? Can you provide a detailed formula or explanation of how the Optimism Score, Pessimism Score, and Neutral Score are combined to generate the overall CSI score?
- How do the sentiment tendencies measured by CSI manifest in the models' responses to open-ended questions or scenarios? Have you conducted any experiments to assess this?
- How does CSI perform with smaller LLMs or models trained on smaller datasets? Have you considered testing CSI on any smaller models or evaluating its performance on a dataset with a smaller vocabulary?
- Have you compared CSI with other psychometric methods, such as the Implicit Emotional Inventory (IEI) or the Affective Lexicon Inventory (ALI)? If so, how does CSI perform in comparison to these methods?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4