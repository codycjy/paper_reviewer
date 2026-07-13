# Review

## Summary
This paper proposes a novel memory-efficient optimizer for fine-tuning large language models (LLMs) by integrating block coordinate descent (BCD) with a Hessian-informed zeroth-order method. The key innovation is treating model layers as blocks and selectively updating only a subset per iteration, reducing memory requirements. The method achieves up to 39% memory reduction compared to existing Hessian-informed zeroth-order methods while maintaining baseline accuracy across various tasks. The approach is validated through experiments on medium-sized models (OPT-1.3B and LLaMA-2-7B), demonstrating improved memory efficiency and convergence rates.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
1. The paper presents a novel combination of block coordinate descent (BCD) with Hessian-informed zeroth-order optimization, addressing both memory efficiency and convergence speed. This integration is creative and well-motivated.
2. The paper is well-structured, clearly explaining the problem, related work, and methodology. The proposed algorithm is presented in detail with clear pseudocode.
3. The proposed method demonstrates practical benefits, achieving up to 39% memory reduction for medium-sized LLMs compared to existing methods.

## Weaknesses
1. The paper lacks a thorough theoretical analysis of the convergence properties of the proposed method. While some convergence results are provided, a deeper exploration of the method's convergence behavior would strengthen the contribution.
2. The experimental evaluation is limited to relatively small models (OPT-1.3B and LLaMA-2-7B). It would be valuable to see how the method scales to larger models, such as LLaMA-2-13B or other state-of-the-art LLMs.
3. The paper does not extensively compare the proposed method with other recent memory-efficient training techniques, such as gradient checkpointing, gradient compression, or mixed precision training. Including these comparisons would provide a more comprehensive assessment of the method's effectiveness.

## Questions
1. How does the proposed method perform on larger LLMs, such as LLaMA-2-13B or other models with more than 7 billion parameters?
2. Can the authors provide more insights into the convergence behavior of the proposed method, particularly in terms of the impact of block size and update frequency on convergence rates?
3. How does the method compare with other memory-efficient training techniques like gradient checkpointing, gradient compression, or mixed precision training in terms of both memory efficiency and training quality?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4