# Review

## Summary
The paper studies the problem of online decision making with predictions. Unlike most previous work, the paper focuses on the issue of calibration. In particular, it is argued that it is more reasonable to assume that the predictions are well-calibrated rather than assuming a global trust level in the predictions. Two problems are considered: ski rental and online job scheduling. For both problems, bounds are provided that relate the competitive ratio/expected regret to the calibration error of the predictor. Experiments are also provided.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
I think the paper studies an interesting problem and provides a nice framework for thinking about the reliability of predictions in online decision making problems. In particular, the notion of calibration is more nuanced than the notion of global trust that is often assumed in the literature. I also find the ski rental algorithm and analysis to be quite elegant.

## Weaknesses
I think the paper can be improved in several ways:

1. Theorem 3.4 is quite interesting. It shows that there are input distributions and predictors such that no deterministic algorithm can do better than the algorithm in Theorem 3.1. It would be interesting to also provide a lower bound on the expected competitive ratio of any algorithm (deterministic or otherwise) in terms of the calibration error. If such a bound cannot be provided, it would be useful to discuss why.

2. Theorem 3.1 provides an upper bound on the expected competitive ratio in terms of the calibration error. However, the dependence on the mean squared error of the predictor is not clear. In particular, the bound in Theorem 3.1 hides the dependence on $\eta$. It would be useful to provide a more explicit bound relating the expected competitive ratio to both the calibration error and the mean squared error. 

3. Theorem 4.3 provides nice bounds on the expected competitive ratio in terms of the calibration error. However, the dependence on the mean squared error is not clear. Providing a more explicit bound as in point 2 above would be useful. 

4. In the experiments, it would be useful to provide plots that show how the expected competitive ratio changes as the mean squared error and the calibration error changes. This would provide a nice verification of the theory.

## Questions
Please see the weaknesses section above.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4