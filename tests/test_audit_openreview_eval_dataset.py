import json
import sys
from argparse import Namespace

import scripts.audit_openreview_eval_dataset as audit_script


def make_args(**overrides):
    defaults = {
        "reviews_per_paper": 1,
        "expected_total": 2,
        "expected_year": 2025,
        "expected_conference": ["ICML"],
        "expected_per_conference": 2,
        "expected_per_collection_label": 1,
        "expected_per_final_label": 1,
        "max_one_sided_segments": None,
        "pdf_dir": None,
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def make_record(label, title, url_suffix):
    return {
        "title": title,
        "paper_dir": f"data/openreview_pdf/{url_suffix}.pdf",
        "paper_url": f"https://openreview.net/forum?id={url_suffix}",
        "pdf_url": f"https://openreview.net/pdf?id={url_suffix}",
        "conference": "ICML",
        "year": 2025,
        "accept_or_not": label,
        "collection_decision_category": label,
        "score": 4.0,
        "reviews": [
            {
                "reviewer_id": "Reviewer_1",
                "strengths": ["Clear motivation."],
                "weaknesses": ["Limited ablations."],
                "rating": 4.0,
                "confidence": 3.0,
                "decision": label,
                "rebuttal": "",
            }
        ],
    }


def test_audit_accepts_balanced_minimal_dataset():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }

    result = audit_script.audit_dataset(data, make_args())

    assert result.errors == []


def test_audit_flags_malformed_key():
    data = {
        "icml_good_2025_001_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }

    result = audit_script.audit_dataset(data, make_args())

    assert any("key does not match expected format" in error for error in result.errors)


def test_audit_flags_key_metadata_drift():
    data = {
        "iclr_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2024_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }

    result = audit_script.audit_dataset(data, make_args())

    assert any("key conference is iclr, but conference is 'ICML'" in error for error in result.errors)
    assert any("key year is 2024, but year is 2025" in error for error in result.errors)


def test_audit_flags_key_title_slug_drift():
    data = {
        "icml_accept_2025_001_different_title": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }

    result = audit_script.audit_dataset(data, make_args())

    assert any("key slug is 'different_title', but title slug is 'good_accept'" in error for error in result.errors)


def test_audit_flags_wrong_dataset_year_even_when_key_and_metadata_agree():
    data = {
        "icml_accept_2024_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2024_001_good_accept"]["year"] = 2024

    result = audit_script.audit_dataset(data, make_args())

    assert any("expected year 2025, found 2024" in error for error in result.errors)


def test_audit_flags_non_integer_year():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_good_accept"]["year"] = "2025"

    result = audit_script.audit_dataset(data, make_args())

    assert any("year is not an integer" in error for error in result.errors)


def test_audit_flags_final_label_imbalance():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_bad_reject": make_record("accept", "Bad Reject", "reject1"),
    }
    data["icml_reject_2025_001_bad_reject"]["collection_decision_category"] = "reject"

    result = audit_script.audit_dataset(data, make_args())

    assert "ICML: expected 1 final reject papers, found 0" in result.errors
    assert any("key bucket is reject, but accept_or_not is accept" in error for error in result.errors)


def test_audit_flags_record_schema_type_errors():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_bad_accept"]["title"] = 123
    data["icml_accept_2025_001_bad_accept"]["paper_url"] = 123
    data["icml_accept_2025_001_bad_accept"]["pdf_url"] = 123
    data["icml_accept_2025_001_bad_accept"]["paper_dir"] = 123
    data["icml_accept_2025_001_bad_accept"]["accept_or_not"] = True
    data["icml_accept_2025_001_bad_accept"]["collection_decision_category"] = "maybe"

    result = audit_script.audit_dataset(data, make_args())

    assert any("title is not a non-empty string" in error for error in result.errors)
    assert any("paper_url is not a non-empty string" in error for error in result.errors)
    assert any("pdf_url is not a non-empty string" in error for error in result.errors)
    assert any("paper_dir is not a non-empty string" in error for error in result.errors)
    assert any("accept_or_not must be a string accept/reject" in error for error in result.errors)
    assert any("collection_decision_category must normalize to accept/reject" in error for error in result.errors)


def test_audit_flags_review_schema_type_errors():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    review = data["icml_accept_2025_001_bad_accept"]["reviews"][0]
    review["reviewer_id"] = ""
    review["decision"] = "maybe"
    review["rebuttal"] = None

    result = audit_script.audit_dataset(data, make_args())

    assert any("reviewer_id is not a non-empty string" in error for error in result.errors)
    assert any("decision must be accept/reject" in error for error in result.errors)
    assert any("rebuttal is not a string" in error for error in result.errors)


def test_audit_flags_nonfinite_numbers():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_bad_reject": make_record("reject", "Bad Reject", "reject1"),
    }
    data["icml_accept_2025_001_bad_accept"]["score"] = float("nan")
    data["icml_accept_2025_001_bad_accept"]["reviews"][0]["confidence"] = float("inf")
    data["icml_reject_2025_001_bad_reject"]["reviews"][0]["rating"] = float("-inf")

    result = audit_script.audit_dataset(data, make_args())

    assert any("score is not finite" in error for error in result.errors)
    assert any("rating is not finite" in error for error in result.errors)
    assert any("confidence is not finite" in error for error in result.errors)


def test_audit_warns_for_null_confidence_without_failing():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_good_accept"]["reviews"][0]["confidence"] = None

    result = audit_script.audit_dataset(data, make_args())
    metadata = audit_script.review_metadata_summary(data)

    assert result.errors == []
    assert any("confidence is null" in warning for warning in result.warnings)
    assert metadata["counts"]["null_confidence"] == 1
    assert metadata["counts"]["finite_confidence"] == 1


def test_audit_flags_duplicate_reviews_within_paper():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    duplicate_reviewer = {
        "reviewer_id": "Reviewer_1",
        "strengths": ["Different strength."],
        "weaknesses": ["Different weakness."],
        "rating": 5.0,
        "confidence": 4.0,
        "decision": "accept",
        "rebuttal": "",
    }
    duplicate_payload = {
        "reviewer_id": "Reviewer_2",
        "strengths": ["Clear motivation."],
        "weaknesses": ["Limited ablations."],
        "rating": 4.0,
        "confidence": 2.0,
        "decision": "reject",
        "rebuttal": "",
    }
    data["icml_accept_2025_001_bad_accept"]["reviews"].append(duplicate_reviewer)
    data["icml_reject_2025_001_good_reject"]["reviews"].append(duplicate_payload)

    result = audit_script.audit_dataset(data, make_args(reviews_per_paper=2))

    assert any("duplicate reviewer_id 'Reviewer_1'" in error for error in result.errors)
    assert any("duplicate review payload" in error for error in result.errors)


def test_audit_flags_duplicate_review_segments_within_side():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_good_accept"]["reviews"][0]["strengths"] = [
        "Clear motivation.",
        " clear   motivation. ",
    ]

    result = audit_script.audit_dataset(data, make_args())

    assert any("duplicate strengths segment at indexes 0 and 1" in error for error in result.errors)


def test_audit_flags_strength_weakness_overlap():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_good_accept"]["reviews"][0]["strengths"] = [
        "Clear motivation.",
        "Limited experiments.",
    ]
    data["icml_accept_2025_001_good_accept"]["reviews"][0]["weaknesses"] = [
        " limited experiments. ",
    ]

    result = audit_script.audit_dataset(data, make_args())

    assert any("segment appears in both strengths[1] and weaknesses[0]" in error for error in result.errors)


def test_audit_validates_openreview_url_formats():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_bad_accept"]["paper_url"] = "https://example.com/forum?id=accept1"
    data["icml_accept_2025_001_bad_accept"]["pdf_url"] = "https://openreview.net/not-pdf?id=accept1"
    data["icml_reject_2025_001_good_reject"]["pdf_url"] = "https://openreview.net/pdf/abc123.pdf"

    result = audit_script.audit_dataset(data, make_args())

    assert any("paper_url is not an OpenReview forum URL" in error for error in result.errors)
    assert any("pdf_url is not an OpenReview PDF URL" in error for error in result.errors)
    assert not any("icml_reject_2025_001_good_reject: pdf_url" in error for error in result.errors)


def test_audit_flags_openreview_url_id_mismatch():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_bad_accept"]["pdf_url"] = "https://openreview.net/pdf?id=other-paper"

    result = audit_script.audit_dataset(data, make_args())

    assert any("paper_url id 'accept1' does not match pdf_url id 'other-paper'" in error for error in result.errors)


def test_audit_flags_duplicate_pdf_url_and_paper_dir():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_good_accept"]["pdf_url"] = "https://openreview.net/pdf/dup123.pdf"
    data["icml_reject_2025_001_good_reject"]["pdf_url"] = "https://openreview.net/pdf/dup123.pdf"
    data["icml_accept_2025_001_good_accept"]["paper_dir"] = "data/openreview_pdf/shared.pdf"
    data["icml_reject_2025_001_good_reject"]["paper_dir"] = "data/openreview_pdf/shared.pdf"

    result = audit_script.audit_dataset(data, make_args())
    summary = audit_script.duplicate_summary(data)

    assert any("duplicate pdf_url https://openreview.net/pdf/dup123.pdf" in error for error in result.errors)
    assert any("duplicate paper_dir data/openreview_pdf/shared.pdf" in error for error in result.errors)
    assert summary["pdf_urls"] == [
        {
            "value": "https://openreview.net/pdf/dup123.pdf",
            "keys": ["icml_accept_2025_001_good_accept", "icml_reject_2025_001_good_reject"],
        }
    ]
    assert summary["paper_dirs"] == [
        {
            "value": "data/openreview_pdf/shared.pdf",
            "keys": ["icml_accept_2025_001_good_accept", "icml_reject_2025_001_good_reject"],
        }
    ]


def test_audit_validates_paper_dir_against_local_pdf_dir(tmp_path):
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    for key in data:
        (pdf_dir / f"{key}.pdf").write_bytes(b"%PDF local")
    data["icml_accept_2025_001_bad_accept"]["paper_dir"] = str(pdf_dir / "wrong.pdf")
    data["icml_reject_2025_001_good_reject"]["paper_dir"] = str(pdf_dir / "icml_reject_2025_001_good_reject.pdf")

    result = audit_script.audit_dataset(data, make_args(pdf_dir=pdf_dir))

    assert any("does not match expected local PDF" in error for error in result.errors)
    assert not any("icml_reject_2025_001_good_reject: paper_dir" in error for error in result.errors)


def test_audit_flags_corrupt_local_pdf(tmp_path):
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    (pdf_dir / "icml_accept_2025_001_bad_accept.pdf").write_bytes(b"<html>challenge</html>")
    (pdf_dir / "icml_reject_2025_001_good_reject.pdf").write_bytes(b"%PDF local")
    for key in data:
        data[key]["paper_dir"] = str(pdf_dir / f"{key}.pdf")

    result = audit_script.audit_dataset(data, make_args(pdf_dir=pdf_dir))

    assert any("does not start with %PDF header" in error for error in result.errors)
    assert not any("icml_reject_2025_001_good_reject: local PDF" in error for error in result.errors)


def test_audit_summarizes_orphan_local_pdfs(tmp_path):
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    for key in data:
        (pdf_dir / f"{key}.pdf").write_bytes(b"%PDF local")
        data[key]["paper_dir"] = str(pdf_dir / f"{key}.pdf")
    (pdf_dir / "stale_extra.pdf").write_bytes(b"%PDF local")

    result = audit_script.audit_dataset(data, make_args(pdf_dir=pdf_dir))
    summary = audit_script.local_pdf_inventory_summary(data, make_args(pdf_dir=pdf_dir))

    assert any("1 unreferenced PDF files" in warning for warning in result.warnings)
    assert summary["total_pdf_files"] == 3
    assert summary["referenced_pdf_files"] == 2
    assert summary["missing_for_records"] == []
    assert summary["orphan_pdf_files"] == ["stale_extra"]
    assert summary["invalid_pdf_files"] == []


def test_audit_flags_section_marker_segments():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_bad_accept"]["reviews"][0]["strengths"] = ["Originality:"]

    result = audit_script.audit_dataset(data, make_args())

    assert any("section/rubric marker" in error for error in result.errors)


def test_audit_flags_placeholder_segments():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_bad_accept"]["reviews"][0]["strengths"] = ["N/A"]

    result = audit_script.audit_dataset(data, make_args())

    assert any("placeholder segment" in error for error in result.errors)


def test_audit_flags_non_substantive_segment_artifacts():
    data = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    data["icml_accept_2025_001_bad_accept"]["reviews"][0]["strengths"] = ["**References**"]

    result = audit_script.audit_dataset(data, make_args())

    assert any("section/rubric marker" in error for error in result.errors)


def test_audit_reports_missing_numbered_slots():
    data = {
        "icml_accept_2025_001_good_accept_1": make_record("accept", "Good Accept 1", "accept1"),
        "icml_reject_2025_001_good_reject_1": make_record("reject", "Good Reject 1", "reject1"),
        "icml_reject_2025_002_good_reject_2": make_record("reject", "Good Reject 2", "reject2"),
    }

    result = audit_script.audit_dataset(
        data,
        make_args(expected_total=4, expected_per_conference=4, expected_per_collection_label=2, expected_per_final_label=-1),
    )

    assert "ICML: missing collected accept key slots: 002" in result.errors


def test_audit_negative_expected_counts_skip_exact_distribution_checks():
    data = {
        "icml_accept_2025_001_good_accept_1": make_record("accept", "Good Accept 1", "accept1"),
        "icml_accept_2025_002_good_accept_2": make_record("accept", "Good Accept 2", "accept2"),
        "icml_reject_2025_001_good_reject_1": make_record("reject", "Good Reject 1", "reject1"),
    }

    result = audit_script.audit_dataset(
        data,
        make_args(
            expected_total=-1,
            expected_per_conference=-1,
            expected_per_collection_label=-1,
            expected_per_final_label=-1,
        ),
    )

    assert result.errors == []


def test_audit_can_fail_on_one_sided_segments():
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_one_sided_reject": make_record("reject", "One Sided Reject", "reject1"),
    }
    data["icml_reject_2025_001_one_sided_reject"]["reviews"][0]["weaknesses"] = []

    result = audit_script.audit_dataset(data, make_args(max_one_sided_segments=0))

    assert "expected at most 0 one-sided segment reviews, found 1" in result.errors


def test_audit_writes_machine_readable_json_report(tmp_path, monkeypatch):
    data = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    input_path = tmp_path / "dataset.json"
    report_path = tmp_path / "reports" / "audit.json"
    input_path.write_text(json.dumps(data), encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "audit_openreview_eval_dataset.py",
            "--input",
            str(input_path),
            "--reviews-per-paper",
            "1",
            "--expected-total",
            "2",
            "--expected-conference",
            "ICML",
            "--expected-per-conference",
            "2",
            "--expected-per-collection-label",
            "1",
            "--expected-per-final-label",
            "1",
            "--pdf-dir",
            str(tmp_path / "pdfs"),
            "--json-output",
            str(report_path),
        ],
    )

    audit_script.main()

    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report["input"] == str(input_path)
    assert report["records"] == 2
    assert report["passed"] is True
    assert report["error_count"] == 0
    assert report["errors"] == []
    assert report["warning_count"] == len(report["warnings"])
    assert report["warning_breakdown"] == {
        "distribution": 3,
    }
    assert report["criteria"] == {
        "reviews_per_paper": 1,
        "expected_total": 2,
        "expected_year": 2025,
        "expected_conference": ["ICML"],
        "expected_per_conference": 2,
        "expected_per_collection_label": 1,
        "expected_per_final_label": 1,
        "max_one_sided_segments": None,
        "pdf_dir": str(tmp_path / "pdfs"),
    }
    assert report["summary"]["distributions"]["conference_counts"] == {"ICML": 2}
    assert report["summary"]["distributions"]["collection_bucket_counts"] == {
        "ICML": {"accept": 1, "reject": 1}
    }
    assert report["summary"]["key_slots"] == [
        {
            "conference": "ICML",
            "bucket": "accept",
            "present_slots": ["001"],
            "missing_slots": [],
            "duplicate_slots": [],
        },
        {
            "conference": "ICML",
            "bucket": "reject",
            "present_slots": ["001"],
            "missing_slots": [],
            "duplicate_slots": [],
        },
    ]
    assert report["summary"]["duplicates"] == {
        "paper_urls": [],
        "pdf_urls": [],
        "paper_dirs": [],
        "titles": [],
    }
    assert report["summary"]["local_pdfs"] == {
        "pdf_dir": str(tmp_path / "pdfs"),
        "exists": False,
        "total_pdf_files": 0,
        "referenced_pdf_files": 0,
        "missing_for_records": [],
        "orphan_pdf_files": [],
        "invalid_pdf_files": [],
    }
    assert report["summary"]["review_metadata"] == {
        "counts": {
            "finite_confidence": 2,
            "finite_ratings": 2,
            "total_reviews": 2,
        },
        "by_conference": {
            "ICML": {
                "finite_confidence": 2,
                "finite_ratings": 2,
                "total_reviews": 2,
            }
        },
    }
    assert report["summary"]["review_segments"]["counts"] == {"total_reviews": 2}
    assert report["summary"]["review_segments"]["problem_reviews"] == []
