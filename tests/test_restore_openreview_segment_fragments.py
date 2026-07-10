import scripts.restore_openreview_segment_fragments as restore


def test_restore_dataset_replaces_sentence_fragments_with_full_source_points():
    target = {
        "iclr_reject_2025_001_example": {
            "title": "Example Paper",
            "paper_url": "https://openreview.net/forum?id=abc123",
            "reviews": [
                {
                    "reviewer_id": "Reviewer_r7KQ",
                    "strengths": ["Clear writing."],
                    "weaknesses": [
                        "The use of Transformer type architectures is a well-known approach.",
                        "This paper showcases the implementation for the TSC problem.",
                        "Please have a formal definition for it.",
                        "In its present for it is very difficult to interpret.",
                        "7)Font size for all the plots can be increased",
                    ],
                }
            ],
        }
    }
    source = {
        "older_key": {
            "title": "Example Paper",
            "paper_url": "https://openreview.net/forum?id=abc123",
            "reviews": [
                {
                    "reviewer_id": "Reviewer_r7KQ",
                    "strengths": ["Clear writing."],
                    "weaknesses": [
                        "Novelty: The paper does not propose any innovative approach. The use of Transformer type architectures is a well-known approach. This paper showcases the implementation for the TSC problem.",
                        "What is the 'static' baseline comparison? Please have a formal definition for it.",
                        "Figure 7b and 7c: it would be nice if a different color palette and markers were used to represent these plots. In its present for it is very difficult to interpret.",
                        "7)Font size for all the plots can be increased",
                    ],
                }
            ],
        }
    }

    source_index = restore.build_source_index_from_dataset_for_test(source)
    restored, stats = restore.restore_dataset(target, source_index)
    review = restored["iclr_reject_2025_001_example"]["reviews"][0]

    assert review["weaknesses"] == [
        "Novelty: The paper does not propose any innovative approach. The use of Transformer type architectures is a well-known approach. This paper showcases the implementation for the TSC problem.",
        "What is the 'static' baseline comparison? Please have a formal definition for it.",
        "Figure 7b and 7c: it would be nice if a different color palette and markers were used to represent these plots. In its present for it is very difficult to interpret.",
        "Font size for all the plots can be increased",
    ]
    assert stats.changed_records == 1
    assert stats.changed_reviews == 1
    assert stats.restored_fields == 1
