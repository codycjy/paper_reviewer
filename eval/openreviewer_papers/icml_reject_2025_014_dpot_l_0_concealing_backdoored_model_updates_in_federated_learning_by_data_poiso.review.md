# Review

## Summary
This paper proposes a backdoor attack strategy in FL that dynamically constructs a per-round backdoor objective by optimizing an L0-norm-bounded backdoor trigger, making backdoor data have minimal effect on model updates and preserving the global model’s main-task performance. The authors theoretically justify the concealment property of DPOTL0’s model updates in linear models. The experiments show that DPOTL0, via only a data-poisoning attack, effectively undermines state-of-the-art defenses and outperforms existing backdoor attack techniques on various datasets.

## Soundness
2

## Presentation
2

## Contribution
2

## Strengths
1. The authors theoretically justify the concealment property of DPOTL0’s model updates in linear models.

2. The authors conduct a lot of experiments to verify the effectiveness of their method.

## Weaknesses
1. The paper is not organized clearly, which is not friendly for understanding. For example, there is a lack the detailed description of the threat model in Section 3.

2. The authors should give a formal definition of the backdoor attack in FL, which can make the paper more clear.

3. The authors should give a formal definition of the clean accuracy in the main task, which can make the paper more clear.

4. The authors should give a formal definition of the data poison rate, which can make the paper more clear.

5. The authors should give the reason why they choose the L0-norm-bounded trigger, which can make the paper more clear.

6. The authors should give a detailed description of the working principle of DPOTL0, which can make the paper more clear.

7. The authors should give a detailed description of the reason why DPOTL0 can achieve high clean accuracy, which is very important for backdoor attack.

8. The authors should give a detailed description of the reason why DPOTL0 can achieve high attack success rate, which is very important for backdoor attack.

9. The authors should give a detailed description of the reason why DPOTL0 can bypass the defense methods, which is very important for backdoor attack.

## Questions
Please see the Weaknesses.

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
3

## Confidence
4