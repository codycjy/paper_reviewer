import json
from argparse import Namespace

import scripts.preflight_openreview_eval_repairs as preflight


def make_record(label, title, strengths=None, weaknesses=None):
    return {
        "title": title,
        "paper_dir": f"data/openreview_pdf/{title}.pdf",
        "paper_url": f"https://openreview.net/forum?id={title}",
        "pdf_url": f"https://openreview.net/pdf?id={title}",
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


def make_args(path):
    return Namespace(
        input=str(path),
        expected_year=2025,
        expected_conference=["ICML"],
        expected_total=4,
        expected_per_conference=4,
        expected_per_collection_label=2,
        expected_per_final_label=2,
        reviews_per_paper=1,
        max_one_sided_segments=None,
        pdf_dir=None,
        llm_api_key_env="DASHSCOPE_API_KEY",
    )


def test_preflight_reports_missing_env_and_required_repair_targets(tmp_path, monkeypatch):
    monkeypatch.delenv("OPENREVIEW_USERNAME", raising=False)
    monkeypatch.delenv("OPENREVIEW_PASSWORD", raising=False)
    monkeypatch.delenv("DASHSCOPE_API_KEY", raising=False)
    monkeypatch.delenv("QWEN_API_KEY", raising=False)
    data = {
        "icml_accept_2025_001_a": make_record("accept", "a"),
        "icml_reject_2025_001_b": make_record("reject", "b", strengths=[], weaknesses=[]),
    }
    path = tmp_path / "dataset.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    report = preflight.build_preflight(make_args(path))

    assert report["repair_targets"]["missing_slots"] == 2
    assert report["repair_targets"]["empty_segment_reviews"] == 1
    assert report["audit"]["warning_breakdown"] == {"distribution": 3}
    assert report["environment"]["openreview_credentials_complete"] is False
    assert report["environment"]["qwen_api_key_available"] is False
    assert report["ready_for_required_external_repairs"] is False
    assert any("No Qwen/DashScope API key" in note for note in report["notes"])


def test_preflight_reports_ready_when_required_env_is_present(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENREVIEW_USERNAME", "user")
    monkeypatch.setenv("OPENREVIEW_PASSWORD", "password")
    monkeypatch.setenv("DASHSCOPE_API_KEY", "key")
    data = {
        "icml_accept_2025_001_a": make_record("accept", "a"),
        "icml_reject_2025_001_b": make_record("reject", "b", strengths=[], weaknesses=[]),
    }
    path = tmp_path / "dataset.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    report = preflight.build_preflight(make_args(path))

    assert report["environment"]["openreview_credentials_complete"] is True
    assert report["environment"]["qwen_api_key_available"] is True
    assert report["ready_for_required_external_repairs"] is True
