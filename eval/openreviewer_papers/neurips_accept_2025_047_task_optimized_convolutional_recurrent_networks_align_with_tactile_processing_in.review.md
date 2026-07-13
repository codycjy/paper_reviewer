# Review

## Summary
The paper proposes a neural network architecture that is optimized for the task of predicting mouse responses to different objects that are probed with a whisker array. The network is trained on a large dataset of objects generated with a physical simulator. The authors find that convolutional RNNs are the best architecture, and that a contrastive loss is as good as a supervised loss in predicting mouse neural responses.

## Soundness
3

## Presentation
3

## Contribution
2

## Strengths
- The paper is well written and easy to follow
- The authors use a large dataset of objects generated with a physical simulator, which is an important step towards making progress in this field
- The authors perform a careful comparison of different architectures and training methods

## Weaknesses
- The paper is mostly a comparison of different architectures and training methods, but it is not clear what the take-home message is. The main result is that convolutional RNNs are best at predicting mouse responses, but it is not clear why this is the case. Is this relevant for understanding the biology? Is this architecture relevant for robotics? It is also not clear what the implications of the contrastive loss are. The authors mention that it is ethologically relevant, but this is not clear to me. Overall, the results are interesting, but it is not clear what we can learn from them.
- The authors use a dataset of 6 different objects to train the neural networks. This is a very small number of objects, and it is not clear whether the results will generalize to a larger number of objects. It would be useful to train the networks on a larger number of objects, and then test them on a held-out set of objects.

## Questions
- The authors mention that the convolutional RNN is the best architecture for predicting mouse responses. However, it is not clear why this is the case. Is it because the whisker data is temporally structured and the convolutional RNN is best able to capture these temporal dependencies? Is there another reason? It would be useful to have a more in-depth analysis of why the convolutional RNN is better.
- The authors mention that the contrastive loss is as good as the supervised loss in predicting mouse responses. However, it is not clear why this is the case. Is it because the contrastive loss captures broader, task-agnostic features that are relevant for the mouse responses? It would be useful to have a more in-depth analysis of why the contrastive loss is as good as the supervised loss.
- The authors use a dataset of 6 different objects to train the neural networks. This is a very small number of objects, and it is not clear whether the results will generalize to a larger number of objects. It would be useful to train the networks on a larger number of objects, and then test them on a held-out set of objects. This would help to assess the generalizability of the results.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4