import json
import sys
from argparse import Namespace
from pathlib import Path

import pytest

import scripts.apply_openreview_eval_dataset_repairs as applier


def make_record(label, title, url_suffix, strengths=None, weaknesses=None):
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
                "strengths": strengths if strengths is not None else ["Clear."],
                "weaknesses": weaknesses if weaknesses is not None else ["Short."],
                "rating": 4.0,
                "confidence": 3.0,
                "decision": label,
                "rebuttal": "",
            }
        ],
    }


def test_apply_repairs_overlays_targeted_review_and_fills_missing_slot(tmp_path):
    base = {
        "icml_accept_2025_001_base_accept": make_record("accept", "Base Accept", "base_accept"),
        "icml_reject_2025_001_empty_reject": make_record("reject", "Empty Reject", "empty", [], []),
    }
    targeted = {
        "icml_reject_2025_001_empty_reject": make_record(
            "reject",
            "Empty Reject",
            "empty",
            ["Recovered strength."],
            ["Recovered weakness."],
        )
    }
    refill = {
        "icml_reject_2025_099_new_refill": make_record("reject", "New Refill", "new_refill")
    }
    plan = {
        "missing_slots": [
            {
                "conference": "ICML",
                "bucket": "reject",
                "missing_slots": ["002"],
                "duplicate_slots": [],
            }
        ],
        "empty_segment_reviews": [
            {
                "key": "icml_reject_2025_001_empty_reject",
                "review_index": 0,
            }
        ],
    }

    for name, payload in {
        "base.json": base,
        "targeted.json": targeted,
        "refill.json": refill,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    pdf_dir = tmp_path / "pdfs"
    pdf_dir.mkdir()
    (pdf_dir / "icml_reject_2025_099_new_refill.pdf").write_bytes(b"%PDF refill")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[str(tmp_path / "targeted.json")],
            segment_qa_repair=[],
            refill=[str(tmp_path / "refill.json")],
            pdf_dir=str(pdf_dir),
        )
    )

    assert dataset["icml_reject_2025_001_empty_reject"]["reviews"][0]["strengths"] == ["Recovered strength."]
    assert "icml_reject_2025_002_new_refill" in dataset
    assert (pdf_dir / "icml_reject_2025_002_new_refill.pdf").exists()
    assert dataset["icml_reject_2025_002_new_refill"]["paper_dir"] == str(
        pdf_dir / "icml_reject_2025_002_new_refill.pdf"
    )
    assert stats.targeted_records_replaced == 1
    assert stats.missing_slots_filled == 1
    assert stats.local_pdfs_copied == 1
    assert stats.unresolved == []


def test_apply_repairs_uses_later_usable_targeted_repair(tmp_path):
    base = {
        "icml_reject_2025_001_empty_reject": make_record("reject", "Empty Reject", "empty", [], []),
    }
    bad_targeted = {
        "icml_reject_2025_001_empty_reject": make_record("reject", "Empty Reject", "empty", [], [])
    }
    good_targeted = {
        "icml_reject_2025_001_empty_reject": make_record(
            "reject",
            "Empty Reject",
            "empty",
            ["Recovered strength."],
            ["Recovered weakness."],
        )
    }
    plan = {
        "missing_slots": [],
        "empty_segment_reviews": [
            {
                "key": "icml_reject_2025_001_empty_reject",
                "review_index": 0,
            }
        ],
    }
    for name, payload in {
        "base.json": base,
        "bad_targeted.json": bad_targeted,
        "good_targeted.json": good_targeted,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[str(tmp_path / "bad_targeted.json"), str(tmp_path / "good_targeted.json")],
            segment_qa_repair=[],
            refill=[],
            pdf_dir=str(tmp_path / "pdfs"),
        )
    )

    assert dataset["icml_reject_2025_001_empty_reject"]["reviews"][0]["strengths"] == ["Recovered strength."]
    assert stats.targeted_records_replaced == 1
    assert stats.unresolved == []


def test_apply_repairs_refuses_duplicate_refill_paper_url(tmp_path):
    base = {
        "icml_reject_2025_001_base_reject": make_record("reject", "Base Reject", "dup"),
    }
    refill = {
        "icml_reject_2025_099_dup": make_record("reject", "Other Title", "dup")
    }
    plan = {
        "missing_slots": [
            {
                "conference": "ICML",
                "bucket": "reject",
                "missing_slots": ["002"],
                "duplicate_slots": [],
            }
        ],
        "empty_segment_reviews": [],
    }
    for name, payload in {
        "base.json": base,
        "refill.json": refill,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[],
            segment_qa_repair=[],
            refill=[str(tmp_path / "refill.json")],
            pdf_dir=str(tmp_path / "pdfs"),
        )
    )

    assert dataset == base
    assert stats.missing_slots_filled == 0
    assert stats.unresolved == ["not enough refill candidates for ICML reject: need 1, got 0"]
    assert stats.skipped_refill_candidates == ["icml_reject_2025_099_dup: duplicate paper_url"]


def test_apply_repairs_skips_low_quality_refill_and_uses_later_candidate(tmp_path):
    base = {
        "icml_reject_2025_001_base_reject": make_record("reject", "Base Reject", "base_reject"),
    }
    good_refill = make_record("reject", "Good Refill", "good_refill")
    good_refill["reviews"].append(
        {
            "reviewer_id": "Reviewer_2",
            "strengths": ["Second strength."],
            "weaknesses": ["Second weakness."],
            "rating": 4.0,
            "confidence": 3.0,
            "decision": "reject",
            "rebuttal": "",
        }
    )
    refill = {
        "icml_reject_2025_098_short_refill": make_record("reject", "Short Refill", "short_refill"),
        "icml_reject_2025_099_good_refill": good_refill,
    }
    plan = {
        "missing_slots": [
            {
                "conference": "ICML",
                "bucket": "reject",
                "missing_slots": ["002"],
                "duplicate_slots": [],
            }
        ],
        "empty_segment_reviews": [],
    }
    for name, payload in {
        "base.json": base,
        "refill.json": refill,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[],
            segment_qa_repair=[],
            refill=[str(tmp_path / "refill.json")],
            pdf_dir=str(tmp_path / "pdfs"),
            reviews_per_paper=2,
        )
    )

    assert "icml_reject_2025_002_good_refill" in dataset
    assert "icml_reject_2025_002_short_refill" not in dataset
    assert stats.missing_slots_filled == 1
    assert stats.skipped_refill_candidates == [
        "icml_reject_2025_098_short_refill: expected 2 reviews, found 1"
    ]
    assert stats.unresolved == []


def test_apply_repairs_skips_refill_with_record_audit_error(tmp_path):
    base = {
        "icml_reject_2025_001_base_reject": make_record("reject", "Base Reject", "base_reject"),
    }
    bad_label = make_record("accept", "Bad Label Refill", "bad_label")
    bad_label["collection_decision_category"] = "reject"
    refill = {
        "icml_reject_2025_098_bad_label_refill": bad_label,
        "icml_reject_2025_099_good_refill": make_record("reject", "Good Refill", "good_refill"),
    }
    plan = {
        "missing_slots": [
            {
                "conference": "ICML",
                "bucket": "reject",
                "missing_slots": ["002"],
                "duplicate_slots": [],
            }
        ],
        "empty_segment_reviews": [],
    }
    for name, payload in {
        "base.json": base,
        "refill.json": refill,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[],
            segment_qa_repair=[],
            refill=[str(tmp_path / "refill.json")],
            pdf_dir=str(tmp_path / "pdfs"),
            reviews_per_paper=1,
        )
    )

    assert "icml_reject_2025_002_good_refill" in dataset
    assert "icml_reject_2025_002_bad_label_refill" not in dataset
    assert stats.missing_slots_filled == 1
    assert len(stats.skipped_refill_candidates) == 1
    assert "key bucket is reject, but accept_or_not is accept" in stats.skipped_refill_candidates[0]
    assert stats.unresolved == []


def test_apply_repairs_optionally_overlays_segment_qa_when_missing_side_is_filled(tmp_path):
    base = {
        "icml_reject_2025_001_one_sided_reject": make_record(
            "reject",
            "One Sided Reject",
            "one_sided",
            strengths=["Clear issue."],
            weaknesses=[],
        ),
    }
    segment_qa = {
        "icml_reject_2025_001_one_sided_reject": make_record(
            "reject",
            "One Sided Reject",
            "one_sided",
            strengths=["Clear issue."],
            weaknesses=["Recovered weakness."],
        )
    }
    plan = {
        "missing_slots": [],
        "empty_segment_reviews": [],
        "one_sided_segment_reviews": [
            {
                "key": "icml_reject_2025_001_one_sided_reject",
                "review_index": 0,
                "missing_side": "weaknesses",
            }
        ],
    }
    for name, payload in {
        "base.json": base,
        "segment_qa.json": segment_qa,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[],
            segment_qa_repair=[str(tmp_path / "segment_qa.json")],
            refill=[],
            pdf_dir=str(tmp_path / "pdfs"),
        )
    )

    assert dataset["icml_reject_2025_001_one_sided_reject"]["reviews"][0]["weaknesses"] == ["Recovered weakness."]
    assert stats.segment_qa_records_replaced == 1
    assert stats.segment_qa_records_skipped == 0


def test_apply_repairs_uses_later_segment_qa_that_fills_missing_side(tmp_path):
    base = {
        "icml_reject_2025_001_one_sided_reject": make_record(
            "reject",
            "One Sided Reject",
            "one_sided",
            strengths=["Clear issue."],
            weaknesses=[],
        ),
    }
    bad_segment_qa = {
        "icml_reject_2025_001_one_sided_reject": make_record(
            "reject",
            "One Sided Reject",
            "one_sided",
            strengths=["Clear issue."],
            weaknesses=[],
        )
    }
    good_segment_qa = {
        "icml_reject_2025_001_one_sided_reject": make_record(
            "reject",
            "One Sided Reject",
            "one_sided",
            strengths=["Clear issue."],
            weaknesses=["Recovered weakness."],
        )
    }
    plan = {
        "missing_slots": [],
        "empty_segment_reviews": [],
        "one_sided_segment_reviews": [
            {
                "key": "icml_reject_2025_001_one_sided_reject",
                "review_index": 0,
                "missing_side": "weaknesses",
            }
        ],
    }
    for name, payload in {
        "base.json": base,
        "bad_segment_qa.json": bad_segment_qa,
        "good_segment_qa.json": good_segment_qa,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[],
            segment_qa_repair=[str(tmp_path / "bad_segment_qa.json"), str(tmp_path / "good_segment_qa.json")],
            refill=[],
            pdf_dir=str(tmp_path / "pdfs"),
        )
    )

    assert dataset["icml_reject_2025_001_one_sided_reject"]["reviews"][0]["weaknesses"] == ["Recovered weakness."]
    assert stats.segment_qa_records_replaced == 1
    assert stats.segment_qa_records_skipped == 0


def test_apply_repairs_skips_segment_qa_when_only_some_planned_sides_are_filled(tmp_path):
    base_record = make_record(
        "reject",
        "One Sided Reject",
        "one_sided",
        strengths=["Clear issue."],
        weaknesses=[],
    )
    base_record["reviews"].append(
        {
            "reviewer_id": "Reviewer_2",
            "strengths": [],
            "weaknesses": ["Missing baselines."],
            "rating": 4.0,
            "confidence": 3.0,
            "decision": "reject",
            "rebuttal": "",
        }
    )
    partial_record = json.loads(json.dumps(base_record))
    partial_record["reviews"][0]["weaknesses"] = ["Recovered weakness."]
    base = {"icml_reject_2025_001_one_sided_reject": base_record}
    segment_qa = {"icml_reject_2025_001_one_sided_reject": partial_record}
    plan = {
        "missing_slots": [],
        "empty_segment_reviews": [],
        "one_sided_segment_reviews": [
            {
                "key": "icml_reject_2025_001_one_sided_reject",
                "review_index": 0,
                "missing_side": "weaknesses",
            },
            {
                "key": "icml_reject_2025_001_one_sided_reject",
                "review_index": 1,
                "missing_side": "strengths",
            },
        ],
    }
    for name, payload in {
        "base.json": base,
        "segment_qa.json": segment_qa,
        "plan.json": plan,
    }.items():
        (tmp_path / name).write_text(applier.json.dumps(payload), encoding="utf-8")

    dataset, stats = applier.apply_repairs(
        Namespace(
            base=str(tmp_path / "base.json"),
            plan=str(tmp_path / "plan.json"),
            targeted_repair=[],
            segment_qa_repair=[str(tmp_path / "segment_qa.json")],
            refill=[],
            pdf_dir=str(tmp_path / "pdfs"),
        )
    )

    assert dataset["icml_reject_2025_001_one_sided_reject"]["reviews"][0]["weaknesses"] == []
    assert stats.segment_qa_records_replaced == 0
    assert stats.segment_qa_records_skipped == 1


def test_load_json_object_reports_missing_inputs(tmp_path):
    with pytest.raises(SystemExit, match="JSON input not found"):
        applier.load_json_object(tmp_path / "missing.json")


def test_main_audits_candidate_before_writing_output(tmp_path, monkeypatch):
    base = {
        "icml_accept_2025_001_base_accept": make_record("accept", "Base Accept", "base_accept"),
        "icml_reject_2025_001_base_reject": make_record("reject", "Base Reject", "base_reject"),
    }
    plan = {"missing_slots": [], "empty_segment_reviews": []}
    base_path = tmp_path / "base.json"
    plan_path = tmp_path / "plan.json"
    output_path = tmp_path / "candidate.json"
    base_path.write_text(json.dumps(base), encoding="utf-8")
    plan_path.write_text(json.dumps(plan), encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "apply_openreview_eval_dataset_repairs.py",
            "--base",
            str(base_path),
            "--plan",
            str(plan_path),
            "--output",
            str(output_path),
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
        ],
    )

    applier.main()

    audit_report = json.loads((tmp_path / "candidate.audit.json").read_text(encoding="utf-8"))
    assert output_path.exists()
    assert audit_report["passed"] is True
    assert audit_report["records"] == 2
    assert audit_report["criteria"]["expected_year"] == 2025


def test_main_refuses_to_write_when_post_apply_audit_fails(tmp_path, monkeypatch):
    base = {
        "icml_accept_2025_001_base_accept": make_record("accept", "Base Accept", "base_accept"),
    }
    plan = {"missing_slots": [], "empty_segment_reviews": []}
    base_path = tmp_path / "base.json"
    plan_path = tmp_path / "plan.json"
    output_path = tmp_path / "candidate.json"
    base_path.write_text(json.dumps(base), encoding="utf-8")
    plan_path.write_text(json.dumps(plan), encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "apply_openreview_eval_dataset_repairs.py",
            "--base",
            str(base_path),
            "--plan",
            str(plan_path),
            "--output",
            str(output_path),
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
        ],
    )

    with pytest.raises(SystemExit, match="post-apply audit failed"):
        applier.main()

    audit_report = json.loads((tmp_path / "candidate.audit.json").read_text(encoding="utf-8"))
    assert not output_path.exists()
    assert audit_report["passed"] is False
    assert "expected 2 records, found 1" in audit_report["errors"]


def test_main_refuses_to_write_when_strict_one_sided_gate_fails(tmp_path, monkeypatch):
    base = {
        "icml_accept_2025_001_base_accept": make_record("accept", "Base Accept", "base_accept"),
        "icml_reject_2025_001_one_sided_reject": make_record(
            "reject",
            "One Sided Reject",
            "one_sided",
            strengths=["Useful analysis."],
            weaknesses=[],
        ),
    }
    plan = {"missing_slots": [], "empty_segment_reviews": [], "one_sided_segment_reviews": []}
    base_path = tmp_path / "base.json"
    plan_path = tmp_path / "plan.json"
    output_path = tmp_path / "candidate.json"
    base_path.write_text(json.dumps(base), encoding="utf-8")
    plan_path.write_text(json.dumps(plan), encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "apply_openreview_eval_dataset_repairs.py",
            "--base",
            str(base_path),
            "--plan",
            str(plan_path),
            "--output",
            str(output_path),
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
            "--max-one-sided-segments",
            "0",
            "--pdf-dir",
            str(tmp_path / "pdfs"),
        ],
    )

    with pytest.raises(SystemExit, match="post-apply audit failed"):
        applier.main()

    audit_report = json.loads((tmp_path / "candidate.audit.json").read_text(encoding="utf-8"))
    assert not output_path.exists()
    assert "expected at most 0 one-sided segment reviews, found 1" in audit_report["errors"]
