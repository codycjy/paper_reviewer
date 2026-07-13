# Review

## Summary
This paper proposes a generative data augmentation method for time series classification. The method is based on a variational autoencoder and aims to encourage compactness of the latent representations for each class while maximizing the separability between classes. The authors evaluate the method on a large number of datasets from the UCR repository and compare to several existing data augmentation methods.

## Soundness
3

## Presentation
2

## Contribution
2

## Strengths
The paper is generally well written and easy to follow. The authors conduct a large number of experiments and compare their method to several existing methods. The method itself is simple, which is a good thing, and the authors provide code for their method.

## Weaknesses
The paper has a few weaknesses. First, the proposed method is not very novel. It consists of a standard VAE objective with a simple clustering loss added to the reconstruction loss. Second, the empirical results are not very convincing. The method does not improve over existing methods in many cases and the average improvement is small. Third, the authors do not discuss the computational complexity of their method, which must be high since it involves training a VAE from scratch many times.

## Questions
I have a few questions and suggestions for the authors:

- Can you provide an estimate of the computational complexity of your method compared to existing methods? How many epochs do you train for and how long does it take to train for an epoch?
- I think you should move the sensitivity analysis in 4.2.4. to an earlier section. I found it very useful to understand the impact of the alpha parameter.
- I think you should also move the analysis in 4.2.5. to an earlier section. It provides useful insight into the conditions under which your method works well.
- In section 4.2.3. you introduce a new metric, the embedded classifier accuracy. I don't understand this metric. Why do you take the maximum of the classifier accuracy and the VAE accuracy? What is the VAE accuracy?
- I think you should discuss the hyperparameter selection procedure. Do you train on a validation set or is it done purely on the training set?
- In section 4.2.6. you introduce a new metric, the class assignment confidence. I don't understand this metric. What is the likelihood that you assign to a sample? How do you assign a likelihood to a dataset? Is it the average likelihood over all samples?
- In section 3.3. you write "If sampled points lie in overlap regions, assign labels by maximizing the posterior probability to ensure risk-aware augmentation and avoid misclassification". How do you assign a label to a sample? Do you assign the label with the highest posterior probability?
- In section 3.3. you write "Use the augmented dataset to retrain the model from scratch". Do you always start from the same initialization or does the initialization change over iterations?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4