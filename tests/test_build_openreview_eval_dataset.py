import http.client
from types import SimpleNamespace

import pytest
import scripts.build_openreview_eval_dataset as builder
import scripts.rebalance_openreview_eval_dataset as rebalance
import scripts.repair_openreview_eval_dataset as repair


class FakeNote:
    def __init__(
        self,
        note_id,
        content,
        invitations=None,
        signatures=None,
        forum="forum1",
        replyto=None,
        cdate=0,
    ):
        self.id = note_id
        self.content = content
        self.invitations = invitations or []
        self.signatures = signatures or []
        self.forum = forum
        self.replyto = replyto
        self.cdate = cdate


def test_split_bullets_preserves_numbered_review_points_with_continuations():
    text = """1. Clarity of writing and presentation: There are multiple instances where the paper lacks clarity in terms of writing and the meaning can only be understood
with someone who are in this domain.
2. Novelty: The paper does not propose any innovative approach. The use of Transformer type architectures is a well-known approach.
6. Figure 7b and 7c: it would be nice if a different color palette and markers were used to represent these plots. In its present for it is very difficult to interpret.
7)Font size for all the plots can be increased
8.. L205 - L206: Please correct this sentence."""

    assert builder.split_bullets(text) == [
        "Clarity of writing and presentation: There are multiple instances where the paper lacks clarity in terms of writing and the meaning can only be understood with someone who are in this domain.",
        "Novelty: The paper does not propose any innovative approach. The use of Transformer type architectures is a well-known approach.",
        "Figure 7b and 7c: it would be nice if a different color palette and markers were used to represent these plots. In its present for it is very difficult to interpret.",
        "Font size for all the plots can be increased",
        "L205 - L206: Please correct this sentence.",
    ]


def test_deterministic_segment_stops_weakness_before_questions_and_rubric_fields():
    raw_review = """
weaknesses
Needs stronger validation.

questions
Can the authors clarify the setup?

soundness
2

presentation
3

contribution
3

flag_for_ethics_review
No ethics review needed.

code_of_conduct
Yes
"""

    strengths, weaknesses = builder.deterministic_segment({}, raw_review)

    assert strengths == []
    assert weaknesses == ["Needs stronger validation."]


def test_build_raw_review_ignores_questions_and_rubric_metadata():
    raw_review = builder.build_raw_review(
        {
            "summary": "Paper summary.",
            "weaknesses": "Needs stronger validation.",
            "questions": "Can the authors clarify the setup?",
            "soundness": "2",
            "presentation": "3",
            "contribution": "3",
            "flag_for_ethics_review": "No ethics review needed.",
            "code_of_conduct": "Yes",
        }
    )

    assert "summary\nPaper summary." in raw_review
    assert "weaknesses\nNeeds stronger validation." in raw_review
    assert "questions" not in raw_review
    assert "soundness" not in raw_review
    assert "presentation" not in raw_review
    assert "contribution" not in raw_review
    assert "flag_for_ethics_review" not in raw_review
    assert "code_of_conduct" not in raw_review


def test_build_segmentation_review_text_strips_references_and_conduct_blocks():
    raw_review = builder.build_segmentation_review_text(
        {
            "summary": "This paper studies a new benchmark.",
            "review": """
Strengths:
The evaluation setup is careful.

References:
[1] Example Author. Example Paper. ICLR 2024.

Code Of Conduct: Affirmed

Weaknesses:
The ablation study is too small.
""",
            "rating": "5",
        }
    )

    assert "summary" not in raw_review
    assert "This paper studies" not in raw_review
    assert "The evaluation setup is careful." in raw_review
    assert "The ablation study is too small." in raw_review
    assert "References" not in raw_review
    assert "Example Author" not in raw_review
    assert "Code Of Conduct" not in raw_review
    assert "Affirmed" not in raw_review


def test_build_segmentation_review_text_handles_future_venue_field_names():
    raw_review = builder.build_segmentation_review_text(
        {
            "Paper Summary": "This paper proposes a method for graph learning.",
            "Reasons to Accept": "The proposed method is simple and the theoretical analysis is convincing.",
            "Reasons to Reject": "The experiments miss strong graph transformer baselines.",
            "Detailed Feedback to Authors": "The writing is hard to follow in Section 4.",
            "Reviewer Expertise": "I have reviewed many graph learning papers.",
            "Submission Checklist": "The authors confirmed all required policies.",
            "Bibliography": "[1] Example Author. Example Paper. ICML 2024.",
            "Numerical Score": "6: marginally above acceptance threshold",
        }
    )

    assert "This paper proposes" not in raw_review
    assert "The proposed method is simple" in raw_review
    assert "The experiments miss strong graph transformer baselines." in raw_review
    assert "The writing is hard to follow in Section 4." in raw_review
    assert "Reviewer Expertise" not in raw_review
    assert "Submission Checklist" not in raw_review
    assert "confirmed all required policies" not in raw_review
    assert "Bibliography" not in raw_review
    assert "Example Author" not in raw_review
    assert "Numerical Score" not in raw_review


def test_neurips_strengths_and_weaknesses_field_is_segmented_verbatim():
    content = {
        "summary": "The paper studies agnostic active learning.",
        "strengths_and_weaknesses": (
            "Strength:\n"
            "- Overall, I find the submission to be a very strong technical paper.\n"
            "- The result is also of sizeable significance.\n\n"
            "Weaknesses:\n"
            "- I have identified any particular weakness with regards to the science, "
            "although this might be due to my limited familiarity with the field."
        ),
        "limitations": "All the assumptions needed for the theoretical results to hold are clearly stated.",
    }

    raw_review = builder.build_raw_review(content)
    strengths, weaknesses = builder.deterministic_segment(content, raw_review)

    assert "strengths_and_weaknesses" in raw_review
    assert strengths == [
        "Overall, I find the submission to be a very strong technical paper.",
        "The result is also of sizeable significance.",
    ]
    assert weaknesses == [
        "I have identified any particular weakness with regards to the science, "
        "although this might be due to my limited familiarity with the field."
    ]
    assert "All the assumptions" not in raw_review


def test_combined_strengths_and_weaknesses_splits_inline_weakness_cue():
    strengths, weaknesses = builder.split_combined_strengths_weaknesses(
        "The authors established the tight mistake bound. "
        "This solves a long-standing open problem. "
        "Regarding weaknesses, I do feel like a more concrete definition would help readers."
    )

    assert strengths == [
        "The authors established the tight mistake bound.",
        "This solves a long-standing open problem.",
    ]
    assert weaknesses == ["I do feel like a more concrete definition would help readers."]


def test_icml_rubric_fields_do_not_leak_into_weaknesses():
    content = {
        "strengths": "The training-time complexity analysis is helpful.",
        "weaknesses": "The adaptive inference strategy is only shown on Sudoku.",
        "claims_and_evidence": "The complexity claim is supported by theory and experiments.",
        "methods_and_evaluation_criteria": "The evaluation mostly makes sense.",
        "theoretical_claims": "The proofs seem correct.",
        "experimental_designs_or_analyses": "The experimental design is mostly correct.",
        "relation_to_broader_scientific_literature": "The findings may help future diffusion LLMs.",
        "essential_references_not_discussed": "No.",
    }

    raw_review = builder.build_raw_review(content)
    strengths, weaknesses = builder.deterministic_segment(content, raw_review)

    assert strengths == ["The training-time complexity analysis is helpful."]
    assert weaknesses == ["The adaptive inference strategy is only shown on Sudoku."]


def test_split_bullets_drops_standalone_rubric_headings():
    text = """
Originality:
- The problem framing is novel.
Quality:
- The empirical section is careful.
Weaknesses:
- The ablation set is small.
"""

    assert builder.split_bullets(text) == [
        "The problem framing is novel.",
        "The empirical section is careful.",
        "The ablation set is small.",
    ]


def test_inline_weakness_cue_does_not_split_inside_sentence():
    strengths, weaknesses = builder.split_combined_strengths_weaknesses(
        "Besides the theoretical part, the weakness of the paper lies in lacking scientific rigor."
    )

    assert strengths == [
        "Besides the theoretical part, the weakness of the paper lies in lacking scientific rigor."
    ]
    assert weaknesses == []


def test_structured_strength_field_routes_inline_weakness_label_to_weaknesses():
    content = {
        "strengths": (
            "Strengths: (1) Principled max-min formulation that directly targets reward hacking. "
            "(2) Improved interpretability through a linear variant. "
            "Weakness: (0) a straightforward approach by borrowing from distributionally robust RL literature. "
            "(1) no theoretical guarantee"
        ),
        "weaknesses": (
            "(0) a straightforward approach by borrowing from distributionally robust RL literature. "
            "(1) no theoretical guarantee"
        ),
    }

    raw_review = builder.build_raw_review(content)
    strengths, weaknesses = builder.deterministic_segment(content, raw_review)

    assert strengths == [
        "Principled max-min formulation that directly targets reward hacking. "
        "(2) Improved interpretability through a linear variant."
    ]
    assert weaknesses == [
        "a straightforward approach by borrowing from distributionally robust RL literature. "
        "(1) no theoretical guarantee"
    ]


def test_deterministic_segment_removes_exact_strength_weakness_overlap_from_strengths():
    content = {
        "strengths": "Clear motivation.\nLimited experiments.",
        "weaknesses": "Limited experiments.",
    }

    strengths, weaknesses = builder.deterministic_segment(content, builder.build_raw_review(content))

    assert strengths == ["Clear motivation."]
    assert weaknesses == ["Limited experiments."]


def test_source_supported_items_rejects_llm_paraphrases():
    raw_review = "Strength:\n- Exact strength sentence.\n\nWeaknesses:\n- Exact weakness sentence."

    assert builder.source_supported_items(
        ["Exact strength sentence.", "A paraphrased generated strength."],
        raw_review,
    ) == ["Exact strength sentence."]


def test_source_supported_items_rejects_mid_sentence_fragments_and_rubric_fields():
    raw_review = (
        "review\n"
        "Besides the theoretical part, the weakness of the paper lies in lacking rigor.\n\n"
        "claims_and_evidence\n"
        "The complexity claim is supported by theory and experiments."
    )

    assert builder.source_supported_items(
        [
            "of the paper lies in lacking rigor.",
            "The complexity claim is supported by theory and experiments.",
        ],
        raw_review,
    ) == []


def test_source_supported_items_rejects_references_conduct_and_generic_rubric_values():
    raw_review = """
Weaknesses:
Needs stronger baselines.

References:
[1] Example Author. Example Paper. ICLR 2024.

Code Of Conduct: Affirmed

Originality: high.
"""

    assert builder.source_supported_items(
        [
            "Needs stronger baselines.",
            "[1] Example Author. Example Paper. ICLR 2024.",
            "Code Of Conduct: Affirmed",
            "Originality: high.",
        ],
        raw_review,
    ) == ["Needs stronger baselines."]


def test_segmentation_filters_placeholder_items():
    assert builder.split_bullets("- N/A\n- None.\n- Real concern.") == ["Real concern."]
    assert builder.source_supported_items(
        ["N/A", "Exact weakness sentence."],
        "Weaknesses:\n- N/A\n- Exact weakness sentence.",
    ) == ["Exact weakness sentence."]


def test_collect_reviews_uses_llm_for_unstructured_mixed_segmentation(monkeypatch):
    review = FakeNote(
        note_id="review1",
        content={
            "review": (
                "The empirical result is convincing. "
                "Besides the theoretical part, the weakness of the paper lies in lacking rigor."
            ),
            "rating": "4: Accept",
        },
        invitations=["ICML.cc/2025/Conference/-/Official_Review"],
    )

    def fake_llm_segment_review(raw_review, model, base_url, api_key_env):
        return (
            ["The empirical result is convincing."],
            ["Besides the theoretical part, the weakness of the paper lies in lacking rigor."],
        )

    monkeypatch.setattr(builder, "llm_segment_review", fake_llm_segment_review)

    reviews = builder.collect_reviews(
        forum_notes=[review],
        use_llm_segmentation=True,
        llm_model="qwen",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
        max_reviews=1,
        dataset_decision="accept",
    )

    assert reviews[0]["strengths"] == ["The empirical result is convincing."]
    assert reviews[0]["weaknesses"] == [
        "Besides the theoretical part, the weakness of the paper lies in lacking rigor."
    ]


def test_collect_reviews_sends_cleaned_review_text_to_llm(monkeypatch):
    review = FakeNote(
        note_id="review1",
        content={
            "summary": "A neutral paper summary.",
            "review": """
Strengths:
The empirical result is convincing.

References:
[1] Example Author. Example Paper. ICLR 2024.

Code Of Conduct: Affirmed

Weaknesses:
Needs stronger baselines.
""",
            "rating": "4: Accept",
        },
        invitations=["ICML.cc/2025/Conference/-/Official_Review"],
    )

    def fake_llm_segment_review(raw_review, model, base_url, api_key_env):
        assert "A neutral paper summary" not in raw_review
        assert "References" not in raw_review
        assert "Code Of Conduct" not in raw_review
        assert "The empirical result is convincing." in raw_review
        assert "Needs stronger baselines." in raw_review
        return (
            ["The empirical result is convincing.", "Code Of Conduct: Affirmed"],
            ["Needs stronger baselines.", "[1] Example Author. Example Paper. ICLR 2024."],
        )

    monkeypatch.setattr(builder, "llm_segment_review", fake_llm_segment_review)

    reviews = builder.collect_reviews(
        forum_notes=[review],
        use_llm_segmentation=True,
        llm_model="qwen",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
        max_reviews=1,
        dataset_decision="accept",
    )

    assert reviews[0]["strengths"] == ["The empirical result is convincing."]
    assert reviews[0]["weaknesses"] == ["Needs stronger baselines."]


def test_icml_overall_recommendation_is_parsed_as_rating_and_recommendation():
    content = {"overall_recommendation": "4: Accept"}

    rating = builder.review_rating(content)

    assert rating == 4.0
    assert builder.reviewer_recommendation(content, rating, "ICML") == "accept"


def test_accept_reject_classifier_recognizes_non_oral_acceptance():
    assert builder.classify_accept_reject_decision("ICML 2025 Poster") == "accept"
    assert builder.collection_category_from_decision("ICML 2025 Poster") == "accept"
    assert builder.classify_accept_reject_decision("Decision: Reject") == "reject"


def test_recommendation_note_is_not_treated_as_final_decision():
    submission = FakeNote(
        note_id="paper1",
        content={"title": "Paper", "venue": "ICML 2025 Submitted"},
    )
    recommendation = FakeNote(
        note_id="rec1",
        content={"recommendation": "Accept"},
        invitations=["ICML.cc/2025/Conference/Submission1/-/Recommendation"],
    )

    assert not builder.is_decision(recommendation)
    assert builder.classify_accept_reject_decision(builder.paper_decision(submission, [recommendation])) is None


def test_decision_note_may_store_label_in_recommendation_field():
    decision = FakeNote(
        note_id="decision1",
        content={"recommendation": "Accept"},
        invitations=["ICML.cc/2025/Conference/Submission1/-/Decision"],
    )

    assert builder.is_decision(decision)
    assert builder.classify_accept_reject_decision(builder.decision_text(decision)) == "accept"


def test_policy_rejection_regex_does_not_match_bandit():
    assert not builder.POLICY_REJECTION_RE.search("contextual bandits")
    assert builder.POLICY_REJECTION_RE.search("country ban")


def test_policy_override_is_opt_in_for_reject_labels():
    submission = FakeNote("paper1", {"decision": "Reject due to country restriction"})
    reviews = [
        FakeNote(
            f"review{i}",
            {"rating": "8: accept", "confidence": "4"},
            invitations=["NeurIPS.cc/2025/Conference/-/Official_Review"],
        )
        for i in range(3)
    ]

    assert builder.dataset_decision_label(submission, reviews, "NeurIPS", "reject") == ("reject", None)

    final_decision, override_reason = builder.dataset_decision_label(
        submission,
        reviews,
        "NeurIPS",
        "reject",
        respect_policy_overrides=True,
    )

    assert final_decision == "accept"
    assert "policy" in override_reason


def test_collect_reviews_excludes_raw_review_and_strips_rebuttal_comment_label():
    review = FakeNote(
        note_id="review1",
        content={
            "strengths": "Clear motivation.",
            "weaknesses": "Needs stronger validation.",
            "rating": "8",
            "confidence": "4",
        },
        invitations=["ICLR.cc/2025/Conference/-/Official_Review"],
        signatures=["ICLR.cc/2025/Conference/Paper1/AnonReviewer1"],
    )
    rebuttal = FakeNote(
        note_id="reply1",
        content={"comment": "comment\nThanks for the careful review."},
        invitations=["ICLR.cc/2025/Conference/-/Comment"],
        signatures=["ICLR.cc/2025/Conference/Paper1/Authors"],
        replyto="review1",
    )

    reviews = builder.collect_reviews(
        forum_notes=[review, rebuttal],
        use_llm_segmentation=False,
        llm_model="unused",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
        max_reviews=1,
        dataset_decision="accept",
    )

    assert len(reviews) == 1
    assert "raw_review" not in reviews[0]
    assert reviews[0]["rebuttal"] == "Thanks for the careful review."


def test_rebuttal_comment_under_official_review_thread_is_not_review():
    rebuttal_comment = FakeNote(
        note_id="comment1",
        content={"comment": "A post-rebuttal comment."},
        invitations=["ICML.cc/2025/Conference/Submission1/Official_Review2/Rebuttal1/-/Rebuttal_Comment"],
        signatures=["ICML.cc/2025/Conference/Submission1/Reviewer_opdC"],
    )

    assert not builder.is_official_review(rebuttal_comment)


def test_icml_review_form_content_is_official_review_without_direct_invitation():
    review = FakeNote(
        note_id="review1",
        content={
            "strengths": "The problem is important.",
            "weaknesses": "The experiments are incomplete.",
            "overall_recommendation": "2: Reject",
        },
        invitations=["ICML.cc/2025/Conference/Submission1/-/Review_Rating"],
        signatures=["ICML.cc/2025/Conference/Submission1/Reviewer_M9zw"],
    )

    assert builder.is_official_review(review)


def test_fetch_forum_notes_merges_direct_replies_and_deduplicates():
    forum = "forum123"
    forum_review = FakeNote(
        note_id="review1",
        forum=forum,
        replyto=forum,
        content={"review": "Forum review.", "rating": "3"},
        invitations=["ICML.cc/2025/Conference/-/Official_Review"],
    )
    direct_reply_review = FakeNote(
        note_id="review2",
        forum="thread_for_review2",
        replyto=forum,
        content={
            "strengths": "Clear motivation.",
            "weaknesses": "Missing validation.",
            "overall_recommendation": "2: Reject",
        },
        signatures=["ICML.cc/2025/Conference/Submission1/Reviewer_4ZuV"],
    )

    class FakeClient:
        def get_all_notes(self, **kwargs):
            if kwargs == {"forum": forum}:
                return [forum_review]
            if kwargs == {"replyto": forum}:
                return [forum_review, direct_reply_review]
            raise AssertionError(f"unexpected query: {kwargs}")

    notes = builder.fetch_forum_notes(FakeClient(), forum)

    assert [note.id for note in notes] == ["review1", "review2"]


def test_select_papers_uses_metadata_reject_candidates_without_forum_scan():
    venue = builder.VenueSpec("ICLR", 2025, "ICLR.cc/2025/Conference")
    accept = FakeNote(
        note_id="accept1",
        content={
            "title": "Accepted Paper",
            "venue": "ICLR 2025 Oral",
            "venueid": "ICLR.cc/2025/Conference",
        },
    )
    reject = FakeNote(
        note_id="reject1",
        content={
            "title": "Rejected Paper",
            "venue": "Submitted to ICLR 2025 Conference",
            "venueid": "ICLR.cc/2025/Conference",
        },
    )

    original_fetch_decision_notes = builder.fetch_decision_notes
    original_fetch_forum_notes = builder.fetch_forum_notes
    builder.fetch_decision_notes = lambda client, venue: {}

    def fail_forum_fetch(client, forum):
        raise AssertionError("metadata selection should not fetch fallback forums")

    builder.fetch_forum_notes = fail_forum_fetch
    try:
        selected = builder.select_papers(
            submissions=[accept, reject],
            client=object(),
            venue=venue,
            per_category=1,
            max_fallback_forum_checks=0,
        )
    finally:
        builder.fetch_decision_notes = original_fetch_decision_notes
        builder.fetch_forum_notes = original_fetch_forum_notes

    assert [(paper.id, label, forum_notes) for paper, label, forum_notes in selected] == [
        ("accept1", "accept", None),
        ("reject1", "reject", None),
    ]


def test_selection_treats_poster_accepts_as_accept_not_rejects():
    venue = builder.VenueSpec("ICLR", 2025, "ICLR.cc/2025/Conference")
    poster = FakeNote(
        note_id="poster1",
        content={
            "title": "Poster Paper",
            "venue": "ICLR 2025 Poster",
            "venueid": "ICLR.cc/2025/Conference",
        },
    )

    assert builder.classify_decision(builder.submission_decision(poster)) is None
    assert builder.decision_bucket_from_text(builder.submission_decision(poster)) == "accept"
    assert not builder.likely_reject_from_submission_metadata(poster, venue)


def test_repair_record_refreshes_existing_paper_without_adding_new_key():
    forum = "forum123"
    submission = FakeNote(
        note_id=forum,
        forum=forum,
        content={
            "title": "Poster Paper",
            "venue": "ICML 2025 Poster",
            "pdf": "/pdf?id=forum123",
        },
    )
    review = FakeNote(
        note_id="review1",
        forum=forum,
        content={
            "strengths": "Clear contribution.",
            "weaknesses": "Needs stronger baselines.",
            "overall_recommendation": "4: Accept",
            "confidence": "3",
        },
        invitations=["ICML.cc/2025/Conference/-/Official_Review"],
        signatures=["ICML.cc/2025/Conference/Submission1/Reviewer_abcd"],
    )

    class FakeClient:
        def get_all_notes(self, **kwargs):
            if kwargs == {"forum": forum}:
                return [submission, review]
            if kwargs == {"replyto": forum}:
                return []
            raise AssertionError(f"unexpected query: {kwargs}")

    class Args:
        use_llm_segmentation = False
        llm_model = "unused"
        llm_base_url = None
        llm_api_key_env = "UNUSED"
        reviews_per_paper = 3
        respect_policy_overrides = False

    original = {
        "title": "Old Title",
        "paper_url": "https://openreview.net/forum?id=forum123",
        "pdf_url": None,
        "conference": "ICML",
        "year": 2025,
        "accept_or_not": "reject",
        "collection_decision_category": "reject",
        "score": None,
        "reviews": [],
    }

    repaired, warnings = repair.repair_record("icml_reject_2025_001_paper_key", original, FakeClient(), Args())

    assert repaired["title"] == "Poster Paper"
    assert repaired["accept_or_not"] == "accept"
    assert repaired["collection_decision_category"] == "accept"
    assert repaired["score"] == 4.0
    assert repaired["reviews"][0]["rating"] == 4.0
    assert repaired["reviews"][0]["weaknesses"] == ["Needs stronger baselines."]
    assert warnings == [
        "final decision 'accept' differs from key bucket 'reject'; "
        "run rebalance_openreview_eval_dataset.py to rename/reindex this record",
        "found 1 official reviews; expected 3",
    ]


def test_repair_recovers_collection_bucket_from_verified_label_before_key():
    record = {
        "collection_decision_category": "accept",
        "accept_or_not": "accept",
    }

    category, warning = repair.resolve_collection_category("icml_reject_2025_001_bad_bucket", record)

    assert category == "accept"
    assert warning is None


def test_repair_selected_items_can_filter_exact_keys():
    class Args:
        only_key = ["paper_b"]
        only_conference = None
        start_after = None
        limit = None

    dataset = {
        "paper_a": {"conference": "ICML"},
        "paper_b": {"conference": "ICLR"},
        "paper_c": {"conference": "NeurIPS"},
    }

    assert repair.selected_items(dataset, Args()) == [("paper_b", {"conference": "ICLR"})]


def test_repair_selected_items_splits_space_joined_only_keys():
    class Args:
        only_key = ["paper_b paper_c"]
        only_conference = None
        start_after = None
        limit = None

    dataset = {
        "paper_a": {"conference": "ICML"},
        "paper_b": {"conference": "ICLR"},
        "paper_c": {"conference": "NeurIPS"},
    }

    assert repair.selected_items(dataset, Args()) == [
        ("paper_b", {"conference": "ICLR"}),
        ("paper_c", {"conference": "NeurIPS"}),
    ]


def test_repair_sanitizes_existing_rubric_leaks():
    reviews = [
        {
            "strengths": ["Useful framing.", "Strengths:"],
            "weaknesses": [
                "Needs stronger text experiments.",
                "claims_and_evidence",
                "The complexity claim is supported.",
                "methods_and_evaluation_criteria",
                "The evaluation mostly makes sense.",
            ],
        }
    ]

    assert repair.sanitize_reviews(reviews) == [
        {
            "strengths": ["Useful framing."],
            "weaknesses": ["Needs stronger text experiments."],
        }
    ]


def test_repair_sanitizes_non_substantive_segment_artifacts():
    reviews = [
        {
            "strengths": [
                "**",
                "**Strengths:**",
                "S1.",
                "**S2.** Useful benchmark.",
                "A.",
                "https://openreview.net/forum?id=artifact",
                "&nbsp;",
                "No further comments.",
                "See Q1.",
                "Novel evaluation approach:** The authors do things carefully.",
                "The paper's writing is excellent.** Otherworldly.",
                "Clear contribution.",
            ],
            "weaknesses": [
                "---",
                "References:",
                "W2.",
                "**Minor:** Limited breadth.",
                "**Minor Comments:**",
                "**Limited Experiment Results.** Small variety.",
                "Major:",
                "Q2.",
                "Minor Remarks",
                "PMLR, 2020.",
                "Lee, M.",
                "Needs stronger baselines.",
                "Originality: high.",
            ],
        }
    ]

    assert repair.sanitize_reviews(reviews) == [
        {
            "strengths": [
                "Useful benchmark.",
                "Novel evaluation approach: The authors do things carefully.",
                "The paper's writing is excellent. Otherworldly.",
                "Clear contribution.",
            ],
            "weaknesses": [
                "Limited breadth.",
                "Limited Experiment Results. Small variety.",
                "Needs stronger baselines.",
            ],
        }
    ]


def test_repair_sanitizes_other_comments_or_suggestions_segments():
    reviews = [
        {
            "strengths": [
                "Clear contribution.",
                "other_comments_or_suggestions I would add a typo fix.",
                "This should be ignored after other comments.",
            ],
            "weaknesses": [
                "Needs stronger baselines.",
                "other_comments_or_suggestions Suggestions:",
            ],
        }
    ]

    assert repair.sanitize_reviews(reviews) == [
        {
            "strengths": ["Clear contribution."],
            "weaknesses": ["Needs stronger baselines."],
        }
    ]


def test_repair_sanitizes_strength_items_with_weakness_labels():
    reviews = [
        {
            "strengths": [
                "Strengths: Clear motivation.",
                "Weakness: Needs stronger baselines.",
            ],
            "weaknesses": ["Needs stronger baselines."],
        }
    ]

    assert repair.sanitize_reviews(reviews) == [
        {
            "strengths": ["Clear motivation."],
            "weaknesses": ["Needs stronger baselines."],
        }
    ]


def test_repair_sanitizes_exact_strength_weakness_overlaps():
    reviews = [
        {
            "strengths": ["Clear motivation.", "Limited experiments."],
            "weaknesses": ["Limited experiments."],
        }
    ]

    assert repair.sanitize_reviews(reviews) == [
        {
            "strengths": ["Clear motivation."],
            "weaknesses": ["Limited experiments."],
        }
    ]


def test_repair_record_uses_qwen_segmentation_when_requested(monkeypatch):
    forum = "forum456"
    submission = FakeNote(
        note_id=forum,
        forum=forum,
        content={"title": "Mixed Review Paper", "venue": "ICML 2025 Poster"},
    )
    review = FakeNote(
        note_id="review1",
        forum=forum,
        content={
            "review": (
                "The empirical evidence is convincing. "
                "Besides the theoretical part, the weakness of the paper lies in lacking rigor."
            ),
            "overall_recommendation": "4: Accept",
        },
        invitations=["ICML.cc/2025/Conference/-/Official_Review"],
    )

    class FakeClient:
        def get_all_notes(self, **kwargs):
            if kwargs == {"forum": forum}:
                return [submission, review]
            if kwargs == {"replyto": forum}:
                return []
            raise AssertionError(f"unexpected query: {kwargs}")

    class Args:
        use_llm_segmentation = True
        llm_model = "qwen"
        llm_base_url = None
        llm_api_key_env = "UNUSED"
        reviews_per_paper = 1
        respect_policy_overrides = False

    def fake_llm_segment_review(raw_review, model, base_url, api_key_env):
        return (
            ["The empirical evidence is convincing."],
            ["Besides the theoretical part, the weakness of the paper lies in lacking rigor."],
        )

    monkeypatch.setattr(builder, "llm_segment_review", fake_llm_segment_review)

    original = {
        "paper_url": "https://openreview.net/forum?id=forum456",
        "conference": "ICML",
        "accept_or_not": "accept",
        "collection_decision_category": "accept",
        "reviews": [],
    }

    repaired, warnings = repair.repair_record("paper_key", original, FakeClient(), Args())

    assert repaired["reviews"][0]["strengths"] == ["The empirical evidence is convincing."]
    assert repaired["reviews"][0]["weaknesses"] == [
        "Besides the theoretical part, the weakness of the paper lies in lacking rigor."
    ]
    assert warnings == []


def test_rebalance_rekeys_verified_decision_and_copies_pdf(monkeypatch, tmp_path):
    accept_forum = "accept_forum"
    reject_forum = "reject_forum"

    def review(note_id, forum, rating="4"):
        return FakeNote(
            note_id=note_id,
            forum=forum,
            content={
                "strengths": f"Clear contribution from {note_id}.",
                "weaknesses": f"Needs stronger validation for {note_id}.",
                "overall_recommendation": f"{rating}: score",
            },
            invitations=["ICML.cc/2025/Conference/-/Official_Review"],
            signatures=[f"ICML.cc/2025/Conference/Submission1/Reviewer_{note_id}"],
        )

    accept_submission = FakeNote(
        note_id=accept_forum,
        forum=accept_forum,
        content={"title": "Accepted Paper", "venue": "ICML 2025 Poster", "pdf": f"/pdf?id={accept_forum}"},
    )
    reject_submission = FakeNote(
        note_id=reject_forum,
        forum=reject_forum,
        content={"title": "Rejected Paper", "venue": "Submitted to ICML 2025", "pdf": f"/pdf?id={reject_forum}"},
    )
    reject_decision = FakeNote(
        note_id="reject_decision",
        forum=reject_forum,
        content={"decision": "Reject"},
        invitations=["ICML.cc/2025/Conference/Submission2/-/Decision"],
    )

    class FakeClient:
        def get_all_notes(self, **kwargs):
            if kwargs == {"forum": accept_forum}:
                return [accept_submission, *[review(f"A{i}", accept_forum) for i in range(3)]]
            if kwargs == {"forum": reject_forum}:
                return [reject_submission, reject_decision, *[review(f"R{i}", reject_forum, "2") for i in range(3)]]
            if kwargs in ({"replyto": accept_forum}, {"replyto": reject_forum}):
                return []
            raise AssertionError(f"unexpected query: {kwargs}")

    monkeypatch.setattr(builder, "import_openreview", lambda: object())
    monkeypatch.setattr(builder, "get_client", lambda openreview: FakeClient())

    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    old_accept_key = "icml_reject_2025_001_accepted_paper"
    old_reject_key = "icml_reject_2025_002_rejected_paper"
    (pdf_dir / f"{old_accept_key}.pdf").write_bytes(b"%PDF accepted")
    (pdf_dir / f"{old_reject_key}.pdf").write_bytes(b"%PDF rejected")
    dataset_path = tmp_path / "dataset.json"
    dataset_path.write_text(
        builder.json.dumps(
            {
                old_accept_key: {
                    "title": "Accepted Paper",
                    "paper_dir": str(pdf_dir / f"{old_accept_key}.pdf"),
                    "paper_url": f"https://openreview.net/forum?id={accept_forum}",
                    "pdf_url": f"https://openreview.net/pdf?id={accept_forum}",
                    "conference": "ICML",
                    "year": 2025,
                    "topic": "Others",
                    "accept_or_not": "reject",
                    "collection_decision_category": "reject",
                    "reviews": [],
                },
                old_reject_key: {
                    "title": "Rejected Paper",
                    "paper_dir": str(pdf_dir / f"{old_reject_key}.pdf"),
                    "paper_url": f"https://openreview.net/forum?id={reject_forum}",
                    "pdf_url": f"https://openreview.net/pdf?id={reject_forum}",
                    "conference": "ICML",
                    "year": 2025,
                    "topic": "Others",
                    "accept_or_not": "reject",
                    "collection_decision_category": "reject",
                    "reviews": [],
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    args = SimpleNamespace(
        input=str(dataset_path),
        output=str(tmp_path / "out.json"),
        venues=None,
        target_per_category=1,
        reviews_per_paper=3,
        pdf_dir=str(pdf_dir),
        topic="Others",
        request_delay=0,
        max_topup_forum_checks=0,
        sleep=0,
        dry_run=False,
        no_backup=True,
        move_pdfs=False,
        download_pdfs=False,
        drop_short_review_papers=False,
        respect_policy_overrides=False,
        use_llm_segmentation=False,
        llm_model="unused",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
    )

    output, stats = rebalance.rebalance_dataset(args)

    assert "icml_accept_2025_001_accepted_paper" in output
    assert "icml_reject_2025_001_rejected_paper" in output
    assert output["icml_accept_2025_001_accepted_paper"]["accept_or_not"] == "accept"
    assert output["icml_accept_2025_001_accepted_paper"]["collection_decision_category"] == "accept"
    assert len(output["icml_accept_2025_001_accepted_paper"]["reviews"]) == 3
    assert (pdf_dir / "icml_accept_2025_001_accepted_paper.pdf").exists()
    assert output["icml_accept_2025_001_accepted_paper"]["paper_dir"] == str(
        pdf_dir / "icml_accept_2025_001_accepted_paper.pdf"
    )
    assert stats.existing_rekeyed == 2
    assert stats.pdf_copied == 2


def test_rebalance_topup_uses_likely_reject_metadata(monkeypatch):
    forum = "likely_reject_forum"
    venue = builder.VenueSpec("ICML", 2025, "ICML.cc/2025/Conference")
    submission = FakeNote(
        note_id=forum,
        forum=forum,
        content={
            "title": "Likely Rejected Paper",
            "venue": "Submitted to ICML 2025",
            "pdf": f"/pdf?id={forum}",
        },
    )
    reviews = [
        FakeNote(
            note_id=f"review{i}",
            forum=forum,
            content={
                "strengths": f"Clear idea {i}.",
                "weaknesses": f"Needs more evidence {i}.",
                "overall_recommendation": "3: reject",
            },
            invitations=["ICML.cc/2025/Conference/-/Official_Review"],
            signatures=[f"ICML.cc/2025/Conference/Submission1/Reviewer_{i}"],
        )
        for i in range(3)
    ]

    class FakeClient:
        def get_all_notes(self, **kwargs):
            if kwargs == {"forum": forum}:
                return [submission, *reviews]
            if kwargs == {"replyto": forum}:
                return []
            if "invitation" in kwargs:
                return []
            raise AssertionError(f"unexpected query: {kwargs}")

    args = SimpleNamespace(
        target_per_category=1,
        reviews_per_paper=3,
        max_topup_forum_checks=10,
        respect_policy_overrides=False,
        use_llm_segmentation=False,
        llm_model="unused",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
        topic="Others",
    )
    groups = rebalance.defaultdict(list)
    stats = rebalance.RebalanceStats()

    monkeypatch.setattr(builder, "fetch_submissions", lambda client, venue: [submission])

    rebalance.top_up_bucket(groups, set(), set(), FakeClient(), venue, "reject", args, stats)

    assert stats.topup_checked == 1
    assert stats.topup_added == 1
    assert groups[("ICML", "reject")][0][1]["title"] == "Likely Rejected Paper"
    assert groups[("ICML", "reject")][0][1]["accept_or_not"] == "reject"
    assert len(groups[("ICML", "reject")][0][1]["reviews"]) == 3


def test_rebalance_pdf_download_prefers_forum_url(monkeypatch, tmp_path):
    attempted = []
    stats = rebalance.RebalanceStats()
    args = SimpleNamespace(
        pdf_dir=str(tmp_path),
        dry_run=False,
        move_pdfs=False,
        download_pdfs=True,
        sleep=0,
    )
    record = {
        "paper_url": "https://openreview.net/forum?id=forum123",
        "pdf_url": "https://openreview.net/pdf/hash-style-url.pdf",
        "paper_dir": "",
    }

    def fake_download_pdf(url, destination, sleep_seconds=0):
        attempted.append(url)
        if url == "https://openreview.net/pdf?id=forum123":
            destination.write_bytes(b"%PDF fallback")
            return True
        return False

    monkeypatch.setattr(builder, "download_pdf", fake_download_pdf)

    paper_dir = rebalance.ensure_pdf_for_key("old_key", "new_key", record, args, stats)

    assert attempted == ["https://openreview.net/pdf?id=forum123"]
    assert paper_dir == str(tmp_path / "new_key.pdf")
    assert (tmp_path / "new_key.pdf").exists()
    assert stats.pdf_downloaded == 1
    assert stats.pdf_missing == 0


def test_rebalance_topup_only_appends_without_refreshing_existing(monkeypatch, tmp_path):
    existing_forum = "existing_forum"
    topup_forum = "topup_forum"
    venue = builder.VenueSpec("ICML", 2025, "ICML.cc/2025/Conference")
    topup_submission = FakeNote(
        note_id=topup_forum,
        forum=topup_forum,
        content={
            "title": "Likely Rejected Paper",
            "venue": "Submitted to ICML 2025",
            "pdf": f"/pdf?id={topup_forum}",
        },
    )
    reviews = [
        FakeNote(
            note_id=f"review{i}",
            forum=topup_forum,
            content={
                "strengths": f"Clear idea {i}.",
                "weaknesses": f"Needs more evidence {i}.",
                "overall_recommendation": "3: reject",
            },
            invitations=["ICML.cc/2025/Conference/-/Official_Review"],
            signatures=[f"ICML.cc/2025/Conference/Submission1/Reviewer_{i}"],
        )
        for i in range(3)
    ]

    class FakeClient:
        def get_all_notes(self, **kwargs):
            if kwargs == {"forum": existing_forum}:
                raise AssertionError("top-up-only should not refetch existing records")
            if kwargs == {"forum": topup_forum}:
                return [topup_submission, *reviews]
            if kwargs == {"replyto": topup_forum}:
                return []
            if "invitation" in kwargs:
                return []
            raise AssertionError(f"unexpected query: {kwargs}")

    dataset_path = tmp_path / "dataset.json"
    existing_key = "icml_reject_2025_001_existing_paper"
    dataset_path.write_text(
        builder.json.dumps(
            {
                existing_key: {
                    "title": "Existing Paper",
                    "paper_dir": "",
                    "paper_url": f"https://openreview.net/forum?id={existing_forum}",
                    "pdf_url": f"https://openreview.net/pdf?id={existing_forum}",
                    "conference": "ICML",
                    "year": 2025,
                    "topic": "Others",
                    "accept_or_not": "reject",
                    "collection_decision_category": "reject",
                    "reviews": [{"reviewer_id": "r1"}, {"reviewer_id": "r2"}, {"reviewer_id": "r3"}],
                }
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    args = SimpleNamespace(
        input=str(dataset_path),
        output=str(tmp_path / "out.json"),
        venues=["ICML:2025"],
        target_per_category=2,
        reviews_per_paper=3,
        pdf_dir=str(tmp_path / "pdfs"),
        topic="Others",
        request_delay=0,
        max_topup_forum_checks=10,
        sleep=0,
        dry_run=False,
        no_backup=True,
        top_up_only=True,
        move_pdfs=False,
        download_pdfs=False,
        drop_short_review_papers=True,
        respect_policy_overrides=False,
        use_llm_segmentation=False,
        llm_model="unused",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
    )

    monkeypatch.setattr(builder, "import_openreview", lambda: object())
    monkeypatch.setattr(builder, "get_client", lambda openreview: FakeClient())
    monkeypatch.setattr(builder, "fetch_submissions", lambda client, venue: [topup_submission])

    output, stats = rebalance.rebalance_dataset(args)

    assert output[existing_key]["title"] == "Existing Paper"
    assert "icml_reject_2025_002_likely_rejected_paper" in output
    assert output["icml_reject_2025_002_likely_rejected_paper"]["accept_or_not"] == "reject"
    assert len(output["icml_reject_2025_002_likely_rejected_paper"]["reviews"]) == 3
    assert stats.existing_rekeyed == 0
    assert stats.topup_added == 1


def test_rebalance_topup_only_can_drop_empty_segment_papers(monkeypatch, tmp_path):
    bad_forum = "bad_forum"
    topup_forum = "replacement_forum"
    topup_submission = FakeNote(
        note_id=topup_forum,
        forum=topup_forum,
        content={
            "title": "Replacement Reject",
            "venue": "Submitted to ICML 2025",
            "pdf": f"/pdf?id={topup_forum}",
        },
    )
    reviews = [
        FakeNote(
            note_id=f"review{i}",
            forum=topup_forum,
            content={
                "strengths": f"Clear idea {i}.",
                "weaknesses": f"Needs more evidence {i}.",
                "overall_recommendation": "3: reject",
            },
            invitations=["ICML.cc/2025/Conference/-/Official_Review"],
            signatures=[f"ICML.cc/2025/Conference/Submission1/Reviewer_{i}"],
        )
        for i in range(3)
    ]

    class FakeClient:
        def get_all_notes(self, **kwargs):
            if kwargs == {"forum": topup_forum}:
                return [topup_submission, *reviews]
            if kwargs == {"replyto": topup_forum}:
                return []
            if "invitation" in kwargs:
                return []
            raise AssertionError(f"unexpected query: {kwargs}")

    dataset_path = tmp_path / "dataset.json"
    bad_key = "icml_reject_2025_001_bad_reject"
    dataset_path.write_text(
        builder.json.dumps(
            {
                bad_key: {
                    "title": "Bad Reject",
                    "paper_dir": "",
                    "paper_url": f"https://openreview.net/forum?id={bad_forum}",
                    "pdf_url": f"https://openreview.net/pdf?id={bad_forum}",
                    "conference": "ICML",
                    "year": 2025,
                    "topic": "Others",
                    "accept_or_not": "reject",
                    "collection_decision_category": "reject",
                    "reviews": [
                        {
                            "reviewer_id": "Reviewer_1",
                            "strengths": [],
                            "weaknesses": [],
                            "rating": 3.0,
                            "confidence": None,
                            "decision": "reject",
                            "rebuttal": "",
                        },
                        {
                            "reviewer_id": "Reviewer_2",
                            "strengths": ["Clear."],
                            "weaknesses": ["Limited."],
                            "rating": 3.0,
                            "confidence": None,
                            "decision": "reject",
                            "rebuttal": "",
                        },
                        {
                            "reviewer_id": "Reviewer_3",
                            "strengths": ["Useful."],
                            "weaknesses": ["Narrow."],
                            "rating": 3.0,
                            "confidence": None,
                            "decision": "reject",
                            "rebuttal": "",
                        },
                    ],
                }
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    args = SimpleNamespace(
        input=str(dataset_path),
        output=str(tmp_path / "out.json"),
        venues=["ICML:2025"],
        target_per_category=1,
        reviews_per_paper=3,
        pdf_dir=str(tmp_path / "pdfs"),
        topic="Others",
        request_delay=0,
        max_topup_forum_checks=10,
        sleep=0,
        dry_run=False,
        no_backup=True,
        top_up_only=True,
        drop_empty_segment_papers=True,
        move_pdfs=False,
        download_pdfs=False,
        drop_short_review_papers=True,
        respect_policy_overrides=False,
        use_llm_segmentation=False,
        llm_model="unused",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
    )

    monkeypatch.setattr(builder, "import_openreview", lambda: object())
    monkeypatch.setattr(builder, "get_client", lambda openreview: FakeClient())
    monkeypatch.setattr(builder, "fetch_submissions", lambda client, venue: [topup_submission])

    output, stats = rebalance.rebalance_dataset(args)

    assert bad_key not in output
    assert "icml_reject_2025_001_replacement_reject" in output
    assert output["icml_reject_2025_001_replacement_reject"]["accept_or_not"] == "reject"
    assert stats.existing_dropped == 1
    assert stats.topup_added == 1


def test_download_pdf_handles_incomplete_read_without_crashing(monkeypatch, tmp_path):
    def raise_incomplete_read(url, timeout):
        raise http.client.IncompleteRead(b"partial", 10)

    monkeypatch.setattr(builder.urllib.request, "urlopen", raise_incomplete_read)
    monkeypatch.setattr(builder.time, "sleep", lambda seconds: None)

    destination = tmp_path / "paper.pdf"

    assert not builder.download_pdf("https://openreview.net/pdf?id=test", destination)
    assert not destination.exists()


def test_download_pdf_reuses_existing_file(monkeypatch, tmp_path):
    def fail_urlopen(url, timeout):
        raise AssertionError("existing PDF should not be downloaded again")

    monkeypatch.setattr(builder.urllib.request, "urlopen", fail_urlopen)
    destination = tmp_path / "paper.pdf"
    destination.write_bytes(b"%PDF existing")

    assert builder.download_pdf("https://openreview.net/pdf?id=test", destination)


def test_build_dataset_does_not_download_pdf_for_skipped_incomplete_paper(monkeypatch, tmp_path):
    submission = FakeNote(
        note_id="forum123",
        forum="forum123",
        content={"title": "Incomplete Paper", "pdf": "/pdf?id=forum123"},
    )

    monkeypatch.setattr(builder, "import_openreview", lambda: object())
    monkeypatch.setattr(builder, "get_client", lambda openreview: object())
    monkeypatch.setattr(builder, "fetch_submissions", lambda client, venue: [submission])
    monkeypatch.setattr(
        builder,
        "select_papers",
        lambda submissions, client, venue, per_category, max_fallback_forum_checks: [(submission, "reject", [])],
    )
    monkeypatch.setattr(builder, "collect_reviews", lambda **kwargs: [])
    monkeypatch.setattr(
        builder,
        "download_pdf",
        lambda url, destination, sleep_seconds=0.0: (_ for _ in ()).throw(
            AssertionError("skipped papers should not download PDFs")
        ),
    )
    monkeypatch.setattr(builder, "validate_dataset", lambda dataset, venues, expected, reviews: None)

    args = SimpleNamespace(
        venues=["ICLR:2025"],
        per_category=50,
        max_papers_per_conference=100,
        max_fallback_forum_checks=0,
        paper_gap_seconds=0,
        output=str(tmp_path / "dataset.json"),
        pdf_dir=str(tmp_path / "pdfs"),
        download_pdfs=True,
        sleep=0,
        use_llm_segmentation=False,
        llm_model="unused",
        llm_base_url=None,
        llm_api_key_env="UNUSED",
        reviews_per_paper=3,
        allow_incomplete=False,
        topic="Others",
        respect_policy_overrides=False,
    )

    assert builder.build_dataset(args) == {}
    assert not (tmp_path / "pdfs").exists()


def test_build_main_prints_openreview_challenge_guidance(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(
        builder,
        "parse_args",
        lambda: SimpleNamespace(
            llm_base_url="",
            llm_api_key_env="DASHSCOPE_API_KEY",
            use_llm_segmentation=False,
            output=str(tmp_path / "dataset.json"),
        ),
    )

    def raise_challenge(args):
        raise RuntimeError("{'name': 'ChallengeRequiredError', 'details': {'challengeUrl': 'https://openreview.net'}}")

    monkeypatch.setattr(builder, "build_dataset", raise_challenge)

    with pytest.raises(SystemExit) as exc:
        builder.main()

    assert exc.value.code == 1
    assert "OpenReview API challenge required" in capsys.readouterr().err
