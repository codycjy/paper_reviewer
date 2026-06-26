import scripts.build_openreview_eval_dataset as builder


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
        ("accept1", "accept_oral", None),
        ("reject1", "reject", None),
    ]
