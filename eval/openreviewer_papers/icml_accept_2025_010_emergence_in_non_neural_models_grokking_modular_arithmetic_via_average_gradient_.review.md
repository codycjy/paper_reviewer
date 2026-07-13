# Review

## Summary
The paper studies feature learning in the context of modular arithmetic. The authors show that a non-neural algorithm called recursive feature machines (RFM) can learn to perform modular arithmetic. They further show that the learned representations by RFM are similar to those learned by neural networks.

## Soundness
2

## Presentation
3

## Contribution
2

## Strengths
The paper is well written. The experiments are clearly explained and easy to follow.

## Weaknesses
I have two main concerns about the paper:

1. The title and the abstract make it sound like the paper studies the phenomenon of grokking in modular arithmetic. However, the paper does not really study grokking. It is well known that neural networks can learn to perform modular arithmetic. The interesting question is why do neural networks learn to perform modular arithmetic so quickly, even though the training loss is zero very early on. The phenomenon of neural networks learning modular arithmetic quickly is called "grokking". The paper does not study this phenomenon. The paper simply shows that another algorithm (RFM) can learn to perform modular arithmetic. 

2. The paper is motivated by the fact that modular arithmetic is not well understood and it is an example of "emergence" in machine learning. I'm not fully convinced by this. Modular arithmetic is a very well-studied problem in mathematics. It is not clear to me what makes learning modular arithmetic by neural networks or any other algorithm "emergent". The paper does not really motivate the problem well. It simply states that modular arithmetic is not well understood and therefore it is interesting to study neural networks learning modular arithmetic. However, there are many problems that are not well understood from a mathematical point of view that neural networks can solve very efficiently. It is not clear why modular arithmetic is interesting and why we should study neural networks learning modular arithmetic. The paper does not really explain this.

## Questions
1. The authors state in the abstract that "we show that the phenomenon of grokking is not specific to neural networks". What do the authors mean by this? It is well known that grokking is a phenomenon that happens with neural networks. What does it mean for grokking to not be specific to neural networks?

2. The authors state that "to the best of our knowledge, no prior work shows a non-neural model that learns modular arithmetic". This is not correct. There are several works that study non-neural models (such as kernel methods) learning modular arithmetic. For example, see https://arxiv.org/abs/2402.16726. 

3. The authors state that "is not tied to gradient-based optimization methods". This is not correct. The paper studies gradient-based optimization methods.

4. The authors state that "is not predicted by training or test loss, let alone accuracy". What do the authors mean by this? It is not clear to me what "predicted by training or test loss" means. The training and test loss of what? How does it predict something?

5. The authors state that "we demonstrate empirically that grokking modular arithmetic". What do the authors mean by this? The paper does not really demonstrate grokking modular arithmetic. The paper shows that an algorithm called RFM can learn to perform modular arithmetic. There is a difference between demonstrating that an algorithm can learn to perform modular arithmetic and demonstrating that an algorithm groks modular arithmetic. Grokking is a phenomenon that happens with neural networks. It is not clear to me how one can demonstrate that an algorithm other than neural networks groks modular arithmetic.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4