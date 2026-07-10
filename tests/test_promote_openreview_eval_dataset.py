import json
import sys

import pytest

import scripts.promote_openreview_eval_dataset as promoter


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


def base_cli(candidate_path, output_path):
    return [
        "promote_openreview_eval_dataset.py",
        "--candidate",
        str(candidate_path),
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
        str(candidate_path.parent / "pdfs"),
    ]


def test_promote_writes_output_audit_and_manifest_for_passing_candidate(tmp_path, monkeypatch):
    candidate = {
        "icml_accept_2025_001_good_accept": make_record("accept", "Good Accept", "accept1"),
        "icml_reject_2025_001_good_reject": make_record("reject", "Good Reject", "reject1"),
    }
    candidate_path = tmp_path / "candidate.json"
    output_path = tmp_path / "canonical.json"
    candidate_path.write_text(json.dumps(candidate), encoding="utf-8")

    monkeypatch.setattr(sys, "argv", base_cli(candidate_path, output_path))

    promoter.main()

    audit_report = json.loads((tmp_path / "canonical.audit.json").read_text(encoding="utf-8"))
    manifest = json.loads((tmp_path / "canonical.manifest.json").read_text(encoding="utf-8"))
    assert json.loads(output_path.read_text(encoding="utf-8")) == candidate
    assert audit_report["passed"] is True
    assert audit_report["records"] == 2
    assert audit_report["criteria"]["expected_year"] == 2025
    assert manifest["audit_passed"] is True
    assert manifest["candidate"] == str(candidate_path)
    assert manifest["output"] == str(output_path)
    assert manifest["records"] == 2
    assert manifest["expected"]["expected_year"] == 2025
    assert manifest["candidate_sha256"] == promoter.sha256_file(candidate_path)
    assert manifest["output_sha256"] == promoter.sha256_file(output_path)


def test_promote_refuses_to_replace_output_when_audit_fails(tmp_path, monkeypatch):
    candidate = {
        "icml_accept_2025_001_bad_accept": make_record("accept", "Bad Accept", "accept1"),
    }
    candidate_path = tmp_path / "candidate.json"
    output_path = tmp_path / "canonical.json"
    candidate_path.write_text(json.dumps(candidate), encoding="utf-8")

    monkeypatch.setattr(sys, "argv", base_cli(candidate_path, output_path))

    with pytest.raises(SystemExit, match="promotion audit failed"):
        promoter.main()

    audit_report = json.loads((tmp_path / "canonical.audit.json").read_text(encoding="utf-8"))
    assert not output_path.exists()
    assert not (tmp_path / "canonical.manifest.json").exists()
    assert audit_report["passed"] is False
    assert "expected 2 records, found 1" in audit_report["errors"]
