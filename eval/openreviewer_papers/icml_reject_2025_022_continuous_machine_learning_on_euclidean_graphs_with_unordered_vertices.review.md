# Review

## Summary
The paper proposes a method for comparing Euclidean graphs, i.e. point clouds or molecular graphs, which is invariant to rigid motions, Lipschitz continuous, and computable in polynomial time. This is achieved by a hierarchy of graph invariants, starting from the simple distances to the center of mass and other neighbors, to the more complex NCD (nested centered distribution) and NBM (nested bottleneck metric). The method is tested on QM9 and other datasets.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
The paper addresses an important problem in chemistry and materials science, which is to compare and classify molecular graphs. The proposed method is novel and has desirable properties for this task, i.e. invariance to rigid motion, Lipschitz continuity, and polynomial-time computability. The presentation is clear, and the paper is well-written.

## Weaknesses
The main weakness of the paper is the lack of comparison with other methods for comparing point clouds or molecular graphs. There are many such methods, including geometric deep learning models and traditional cheminformatics methods. Without such comparisons, it is hard to assess the practical utility of the proposed method.

## Questions
- How does the proposed method compare to other methods for comparing point clouds or molecular graphs, such as geometric deep learning models or traditional cheminformatics methods?
- The NCD and NBM invariants are quite complex and may be difficult to interpret or visualize. Do the authors have any suggestions for how to use these invariants in practice, or how to interpret them in the context of molecular properties?
- The paper mentions that the proposed method can distinguish all chemically different molecules in QM9. However, QM9 only contains molecules with up to 14 heavy atoms. How well does the method scale to larger molecules, such as proteins?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4