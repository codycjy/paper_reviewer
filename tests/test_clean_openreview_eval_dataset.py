import scripts.clean_openreview_eval_dataset as cleaner


def test_clean_dataset_drops_legacy_policy_override_and_updates_review_decisions():
    data = {
        "neurips_reject_2025_001_policy_case": {
            "title": "Policy Case",
            "paper_url": "https://openreview.net/forum?id=policy",
            "pdf_url": "https://openreview.net/pdf?id=policy",
            "conference": "NeurIPS",
            "year": 2025,
            "accept_or_not": "accept",
            "collection_decision_category": "reject",
            "decision_override_reason": "Rejected paper relabeled because reviewers recommended accept.",
            "score": 8.0,
            "reviews": [
                {
                    "reviewer_id": "Reviewer_1",
                    "strengths": ["Strong result."],
                    "weaknesses": ["Limited discussion."],
                    "rating": 8.0,
                    "confidence": 4.0,
                    "decision": "accept",
                    "rebuttal": "",
                }
            ],
        }
    }

    cleaned, stats = cleaner.clean_dataset(data, keep_policy_overrides=False)
    record = cleaned["neurips_reject_2025_001_policy_case"]

    assert record["accept_or_not"] == "reject"
    assert record["reviews"][0]["decision"] == "reject"
    assert "decision_override_reason" not in record
    assert stats.policy_overrides_dropped == 1
    assert stats.review_decisions_updated == 1


def test_clean_dataset_sanitizes_section_markers_and_recomputes_score():
    data = {
        "icml_accept_2025_001_segment_case": {
            "title": "Segment Case",
            "paper_url": "https://openreview.net/forum?id=segment",
            "pdf_url": "https://openreview.net/pdf?id=segment",
            "conference": "ICML",
            "year": 2025,
            "accept_or_not": "accept",
            "collection_decision_category": "accept",
            "score": 99.0,
            "reviews": [
                {
                    "reviewer_id": "Reviewer_1",
                    "strengths": ["Strengths:", "Clear contribution."],
                    "weaknesses": ["Weaknesses:", "Needs stronger baselines."],
                    "rating": 4.0,
                    "confidence": 3.0,
                    "decision": "accept",
                    "rebuttal": "",
                }
            ],
        }
    }

    cleaned, stats = cleaner.clean_dataset(data, keep_policy_overrides=False)
    record = cleaned["icml_accept_2025_001_segment_case"]

    assert record["reviews"][0]["strengths"] == ["Clear contribution."]
    assert record["reviews"][0]["weaknesses"] == ["Needs stronger baselines."]
    assert record["score"] == 4.0
    assert stats.segment_items_removed == 2
    assert stats.scores_recomputed == 1


def test_clean_dataset_removes_placeholder_segments():
    data = {
        "icml_reject_2025_001_placeholder_case": {
            "title": "Placeholder Case",
            "paper_url": "https://openreview.net/forum?id=placeholder",
            "pdf_url": "https://openreview.net/pdf?id=placeholder",
            "conference": "ICML",
            "year": 2025,
            "accept_or_not": "reject",
            "collection_decision_category": "reject",
            "score": 4.0,
            "reviews": [
                {
                    "reviewer_id": "Reviewer_1",
                    "strengths": ["None.", "Useful framing."],
                    "weaknesses": ["N/A", "Limited evidence."],
                    "rating": 4.0,
                    "confidence": 3.0,
                    "decision": "reject",
                    "rebuttal": "",
                }
            ],
        }
    }

    cleaned, stats = cleaner.clean_dataset(data, keep_policy_overrides=False)
    record = cleaned["icml_reject_2025_001_placeholder_case"]

    assert record["reviews"][0]["strengths"] == ["Useful framing."]
    assert record["reviews"][0]["weaknesses"] == ["Limited evidence."]
    assert stats.segment_items_removed == 2


def test_clean_dataset_removes_non_substantive_segment_artifacts():
    data = {
        "icml_accept_2025_001_artifact_case": {
            "title": "Artifact Case",
            "paper_url": "https://openreview.net/forum?id=artifact",
            "pdf_url": "https://openreview.net/pdf?id=artifact",
            "conference": "ICML",
            "year": 2025,
            "accept_or_not": "accept",
            "collection_decision_category": "accept",
            "score": 4.0,
            "reviews": [
                {
                    "reviewer_id": "Reviewer_1",
                    "strengths": [
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
                        "---",
                        "Originality: high.",
                    ],
                    "rating": 4.0,
                    "confidence": 3.0,
                    "decision": "accept",
                    "rebuttal": "",
                }
            ],
        }
    }

    cleaned, stats = cleaner.clean_dataset(data, keep_policy_overrides=False)
    record = cleaned["icml_accept_2025_001_artifact_case"]

    assert record["reviews"][0]["strengths"] == [
        "Useful benchmark.",
        "Novel evaluation approach: The authors do things carefully.",
        "The paper's writing is excellent. Otherworldly.",
        "Clear contribution.",
    ]
    assert record["reviews"][0]["weaknesses"] == [
        "Limited breadth.",
        "Limited Experiment Results. Small variety.",
    ]
    assert stats.segment_items_removed == 17


def test_clean_dataset_removes_other_comments_or_suggestions_segments():
    data = {
        "icml_accept_2025_001_other_comments_case": {
            "title": "Other Comments Case",
            "paper_url": "https://openreview.net/forum?id=othercomments",
            "pdf_url": "https://openreview.net/pdf?id=othercomments",
            "conference": "ICML",
            "year": 2025,
            "accept_or_not": "accept",
            "collection_decision_category": "accept",
            "score": 4.0,
            "reviews": [
                {
                    "reviewer_id": "Reviewer_1",
                    "strengths": ["Clear contribution.", "other_comments_or_suggestions Please fix typos."],
                    "weaknesses": ["Limited ablations.", "other_comments_or_suggestions Suggestions:"],
                    "rating": 4.0,
                    "confidence": 3.0,
                    "decision": "accept",
                    "rebuttal": "",
                }
            ],
        }
    }

    cleaned, stats = cleaner.clean_dataset(data, keep_policy_overrides=False)
    record = cleaned["icml_accept_2025_001_other_comments_case"]

    assert record["reviews"][0]["strengths"] == ["Clear contribution."]
    assert record["reviews"][0]["weaknesses"] == ["Limited ablations."]
    assert stats.segment_items_removed == 2
