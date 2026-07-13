# Review

## Summary
This paper proposes a hybrid batch training strategy to simultaneously improve zero-shot retrieval performance across monolingual, cross-lingual, and multilingual settings while mitigating language bias. The approach fine-tunes multilingual language models using a mix of monolingual and cross-lingual question-answer pair batches sampled based on dataset size. Experiments on XQuAD-R, MLQA-R, and MIRACL benchmark datasets show that the proposed method consistently achieves comparable or superior results in zero-shot retrieval across various languages and retrieval tasks compared to monolingual-only or cross-lingual-only training.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The paper proposes a hybrid batch training strategy that can simultaneously optimize retrieval performance across monolingual, cross-lingual, and multilingual settings while also mitigating language bias.
2. The paper conducts experiments on XQuAD-R, MLQA-R, and MIRACL benchmark datasets, demonstrating the effectiveness of the proposed approach, with models trained using the hybrid batch strategy consistently achieving competitive results in zero-shot retrieval across various languages and retrieval tasks, outperforming models trained with only monolingual or cross-lingual data.

## Weaknesses
1. The proposed method lacks innovation and is merely a combination of X-X and X-Y.
2. The paper does not analyze why a combination of X-X and X-Y would be better than either X-X or X-Y alone, and there is no theoretical or experimental evidence to support this claim.
3. The paper does not discuss the impact of different values of α and β on the results.
4. The experimental section only compares the results of the proposed method with X-X and X-Y, without comparing them to other state-of-the-art methods in the field.

## Questions
1. Why is a combination of X-X and X-Y better than either X-X or X-Y alone? Is there any theoretical or experimental evidence to support this claim?
2. How do different values of α and β affect the results?
3. Can you compare the results of the proposed method with other state-of-the-art methods in the field?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
5