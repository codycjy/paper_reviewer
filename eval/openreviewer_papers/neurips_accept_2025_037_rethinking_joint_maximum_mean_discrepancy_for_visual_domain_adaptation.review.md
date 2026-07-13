# Review

## Summary
This paper deduces a concise JMMD based on the Representer theorem that avoids the tensor-product operator and obtains two essential findings. First, they reveal the uniformity of JMMD by proving that previous marginal, class conditional, and weighted class conditional probability distribution distances are three special cases of JMMD with different label reproducing kernels. Second, they observe that the similarity weights, which strengthen the intra-class compactness in the graph of Hilbert Schmidt independence criterion (HSIC), take opposite signs in the graph of JMMD, revealing why JMMD degrades the feature discrimination. This motivates them to propose a novel loss JMMD-HSIC by jointly considering JMMD and HSIC to promote discrimination of JMMD. Extensive experiments on several cross-domain datasets could demonstrate the validity of their revealed theoretical results and the effectiveness of their proposed JMMD-HSIC.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper is well-written and easy to understand. The proposed JMMD-HSIC loss is interesting and effective. The experimental results are convincing. The theoretical analysis is sufficient.

## Weaknesses
The proposed JMMD-HSIC loss is based on the HSIC loss. What is the advantage of JMMD-HSIC over HSIC? Please provide a detailed analysis and explanation.

## Questions
Please see the Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
8

## Confidence
4