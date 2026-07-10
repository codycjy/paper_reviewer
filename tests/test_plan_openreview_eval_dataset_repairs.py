from argparse import Namespace
from pathlib import Path

import scripts.plan_openreview_eval_dataset_repairs as planner


def make_record(label, title):
    return {
        "title": title,
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
                "strengths": ["Clear."],
                "weaknesses": ["Short."],
                "rating": 4.0,
                "confidence": 3.0,
                "decision": label,
                "rebuttal": "",
            }
        ],
    }


def test_repair_plan_reports_missing_slots_and_empty_reviews(tmp_path):
    data = {
        "icml_accept_2025_001_a": make_record("accept", "a"),
        "icml_reject_2025_001_b": make_record("reject", "b"),
        "icml_reject_2025_002_c": make_record("reject", "c"),
    }
    data["icml_accept_2025_001_a"]["reviews"][0]["weaknesses"] = []
    data["icml_reject_2025_002_c"]["reviews"][0]["strengths"] = []
    data["icml_reject_2025_002_c"]["reviews"][0]["weaknesses"] = []
    path = tmp_path / "dataset.json"
    path.write_text(planner.json.dumps(data), encoding="utf-8")

    plan = planner.build_plan(
        Namespace(
            input=str(path),
            expected_year=2025,
            expected_conference=["ICML"],
            expected_per_collection_label=2,
            output=None,
        )
    )

    assert plan["expected_year"] == 2025
    assert plan["missing_slots"] == [
        {
            "conference": "ICML",
            "bucket": "accept",
            "missing_slots": ["002"],
            "duplicate_slots": [],
        }
    ]
    assert plan["empty_segment_reviews"][0]["key"] == "icml_reject_2025_002_c"
    assert plan["one_sided_segment_reviews"][0]["key"] == "icml_accept_2025_001_a"
    assert plan["one_sided_segment_reviews"][0]["missing_side"] == "weaknesses"
    assert "--json-output" in plan["commands"]["audit"]
    assert "--expected-year 2025" in plan["commands"]["audit"]
    assert "dataset.audit.json" in plan["commands"]["audit"]
    assert "scripts/preflight_openreview_eval_repairs.py" in plan["commands"]["preflight_external_repairs"]
    assert "--expected-year 2025" in plan["commands"]["preflight_external_repairs"]
    assert "--json-output eval/openreview_2025_300_qwen.preflight.json" in plan["commands"]["preflight_external_repairs"]
    assert "--only-key icml_reject_2025_002_c" in plan["commands"]["repair_empty_reviews"]
    assert "repair_one_sided_segments_optional" in plan["commands"]
    assert "--only-key icml_accept_2025_001_a" in plan["commands"]["repair_one_sided_segments_optional"]
    assert "scripts/build_openreview_eval_dataset.py" in plan["commands"]["rebuild_missing_conference"]
    assert "--venues ICML:2025" in plan["commands"]["rebuild_missing_conference"]
    assert "--output eval/openreview_2025_icml_refill.json" in plan["commands"]["rebuild_missing_conference"]
    assert "scripts/apply_openreview_eval_dataset_repairs.py" in plan["commands"]["apply_repairs"]
    assert "--targeted-repair eval/openreview_2025_300_qwen.targeted_repair.json" in plan["commands"]["apply_repairs"]
    assert "--refill eval/openreview_2025_icml_refill.json" in plan["commands"]["apply_repairs"]
    assert "--expected-year 2025" in plan["commands"]["apply_repairs"]
    assert "--audit-json-output eval/openreview_2025_300_qwen.final_candidate.audit.json" in plan["commands"]["apply_repairs"]
    assert "--segment-qa-repair eval/openreview_2025_300_qwen.segment_qa_repair.json" in plan["commands"]["apply_repairs_with_segment_qa_optional"]
    assert "final_candidate.json" in plan["commands"]["audit_final_candidate"]
    assert "--expected-year 2025" in plan["commands"]["audit_final_candidate"]
    assert "final_candidate.audit.json" in plan["commands"]["audit_final_candidate"]
    assert "--max-one-sided-segments 0" in plan["commands"]["audit_final_candidate_strict_segments_optional"]
    assert "scripts/promote_openreview_eval_dataset.py" in plan["commands"]["promote_final_candidate"]
    assert "--expected-year 2025" in plan["commands"]["promote_final_candidate"]
    assert "--manifest-output eval/openreview_2025_300_qwen.manifest.json" in plan["commands"]["promote_final_candidate"]
    assert "--max-one-sided-segments 0" in plan["commands"]["promote_final_candidate_strict_segments_optional"]


def test_repair_plan_apply_command_omits_unneeded_inputs(tmp_path):
    empty_only = {
        "icml_accept_2025_001_a": make_record("accept", "a"),
        "icml_accept_2025_002_b": make_record("accept", "b"),
        "icml_reject_2025_001_c": make_record("reject", "c"),
        "icml_reject_2025_002_d": make_record("reject", "d"),
    }
    empty_only["icml_reject_2025_002_d"]["reviews"][0]["strengths"] = []
    empty_only["icml_reject_2025_002_d"]["reviews"][0]["weaknesses"] = []
    empty_path = tmp_path / "empty_only.json"
    empty_path.write_text(planner.json.dumps(empty_only), encoding="utf-8")

    empty_plan = planner.build_plan(
        Namespace(
            input=str(empty_path),
            expected_year=2025,
            expected_conference=["ICML"],
            expected_per_collection_label=2,
            output=None,
        )
    )

    assert "--targeted-repair eval/openreview_2025_300_qwen.targeted_repair.json" in empty_plan["commands"]["apply_repairs"]
    assert "--refill" not in empty_plan["commands"]["apply_repairs"]

    missing_only = {
        "icml_accept_2025_001_a": make_record("accept", "a"),
        "icml_reject_2025_001_b": make_record("reject", "b"),
        "icml_reject_2025_002_c": make_record("reject", "c"),
    }
    missing_path = tmp_path / "missing_only.json"
    missing_path.write_text(planner.json.dumps(missing_only), encoding="utf-8")

    missing_plan = planner.build_plan(
        Namespace(
            input=str(missing_path),
            expected_year=2025,
            expected_conference=["ICML"],
            expected_per_collection_label=2,
            output=None,
        )
    )

    assert "--targeted-repair" not in missing_plan["commands"]["apply_repairs"]
    assert "--refill eval/openreview_2025_icml_refill.json" in missing_plan["commands"]["apply_repairs"]
