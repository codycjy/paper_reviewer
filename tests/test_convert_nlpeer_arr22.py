from argparse import Namespace
from enum import Enum

import pytest

import scripts.convert_nlpeer_arr22 as converter
from scripts.convert_nlpeer_arr22 import (
    extract_structured_review,
    is_arr22_option,
    normalize_field_name,
    parse_numeric_score,
    resolve_dataset_option,
    validate_record,
)


class FakeDatasets(Enum):
    ARR22 = "ARR-22"
    F1000 = "F1000"


class FakePaperFormats:
    ITG = "itg"


def test_resolve_dataset_option_accepts_arr_22_aliases():
    option = resolve_dataset_option(FakeDatasets, "ARR-22")
    assert option.key == "ARR22"
    assert option.value == FakeDatasets.ARR22
    assert is_arr22_option(option)


def test_arr22_guard_rejects_other_dataset_options():
    option = resolve_dataset_option(FakeDatasets, "F1000")
    assert not is_arr22_option(option)


def test_normalize_field_name_removes_spacing_hyphen_and_underscore():
    assert normalize_field_name("Main Strengths") == "mainstrengths"
    assert normalize_field_name("Main-Weaknesses") == "mainweaknesses"
    assert normalize_field_name("overall_score") == "overallscore"


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (3, 3.0),
        (4.5, 4.5),
        ("3", 3.0),
        ("3: good", 3.0),
        ("3 - good", 3.0),
        ({"value": "2.5: fair"}, 2.5),
    ],
)
def test_parse_numeric_score_accepts_leading_numeric_values(raw, expected):
    assert parse_numeric_score(raw) == expected


@pytest.mark.parametrize("raw", ["good: 3", "", None, True, {"label": "3"}])
def test_parse_numeric_score_rejects_unreliable_values(raw):
    assert parse_numeric_score(raw) is None


def test_extract_structured_review_uses_only_structured_strength_weakness_fields():
    review = {
        "rid": "review_1",
        "report": {
            "main": "Strength: do not mine this unstructured text.",
            "Summary of Strengths": "Clear motivation\nand evaluation.",
            "Main-Weaknesses": ["Limited baselines.", ""],
        },
        "scores": {"Overall Score": "3 - good"},
    }

    extracted, missing = extract_structured_review(review, "paper42", 0)

    assert missing == ()
    assert extracted is not None
    assert extracted.score == 3.0
    assert extracted.score_field == "Overall Score"
    assert extracted.review == {
        "reviewer_id": "review_1",
        "strengths": ["Clear motivation and evaluation."],
        "weaknesses": ["Limited baselines."],
    }


def test_extract_structured_review_reports_all_missing_reasons():
    review = {"rid": "review_1", "report": {"main": "Free-form review."}, "scores": {"impact": "3"}}

    extracted, missing = extract_structured_review(review, "paper42", 0)

    assert extracted is None
    assert missing == ("missing_strengths", "missing_weaknesses", "missing_score")


def test_extract_structured_review_generates_stable_anonymous_id_without_reviewer_name():
    review = {
        "reviewer": "Named Reviewer",
        "report": {"Strengths": "Good idea.", "Weaknesses": "Needs more experiments."},
        "scores": {"overall": "4"},
    }

    first, first_missing = extract_structured_review(review, "paper42", 0)
    second, second_missing = extract_structured_review(review, "paper42", 0)

    assert first_missing == second_missing == ()
    assert first is not None
    assert second is not None
    assert first.review["reviewer_id"] == second.review["reviewer_id"]
    assert first.review["reviewer_id"].startswith("anonymous_")
    assert "Named" not in first.review["reviewer_id"]


def test_validate_record_requires_non_empty_strengths_and_weaknesses():
    record = {
        "paper_id": "arr22_paper42",
        "accept_or_not": "accept",
        "score": 3,
        "reviews": [
            {
                "reviewer_id": "review_1",
                "strengths": ["Clear motivation."],
                "weaknesses": ["Limited baselines."],
            }
        ],
    }
    validate_record(record)

    record["reviews"][0]["weaknesses"] = []
    with pytest.raises(AssertionError):
        validate_record(record)


def test_convert_dataset_exports_valid_reviews_and_counts_skips(monkeypatch):
    fake_data = [
        (
            "paper42",
            {},
            {},
            [
                {
                    "rid": "review_1",
                    "report": {"Strengths": "Clear.", "Weaknesses": "Limited baseline."},
                    "scores": {"overall": "3"},
                },
                {
                    "rid": "review_2",
                    "report": {"Strengths": "Useful."},
                    "scores": {"overall": "4"},
                },
                {
                    "rid": "review_3",
                    "report": {"Strengths": "Novel.", "Weaknesses": "Unclear."},
                    "scores": {"overall": "good"},
                },
            ],
        ),
        ("paper43", {}, {}, [{"report": {"main": "Free-form text."}, "scores": {}}]),
    ]

    monkeypatch.setattr(
        converter,
        "import_nlpeer",
        lambda: (FakeDatasets, FakePaperFormats, object),
    )
    monkeypatch.setattr(
        converter,
        "load_paper_review_dataset",
        lambda nlpeer_root, dataset_value, version, paper_formats, paper_review_dataset_cls: fake_data,
    )

    args = Namespace(
        nlpeer_root="/tmp/nlpeer",
        out="/tmp/out.jsonl",
        stats_out="/tmp/stats.json",
        dataset="ARR-22",
        version=1,
    )

    records, stats = converter.convert_dataset(args)

    assert len(records) == 1
    assert records[0]["paper_id"] == "arr22_paper42"
    assert records[0]["score"] == 3
    assert records[0]["reviews"] == [
        {
            "reviewer_id": "review_1",
            "strengths": ["Clear."],
            "weaknesses": ["Limited baseline."],
        }
    ]
    assert stats["total_papers_seen"] == 2
    assert stats["papers_exported"] == 1
    assert stats["total_reviews_seen"] == 4
    assert stats["reviews_exported"] == 1
    assert stats["reviews_skipped_missing_strengths"] == 1
    assert stats["reviews_skipped_missing_weaknesses"] == 2
    assert stats["reviews_skipped_missing_score"] == 2
    assert stats["score_distribution"] == {"3": 1}
    assert stats["accept_or_not_distribution"] == {"accept": 1}
