import json
from unittest.mock import patch

import mas_loop


def _review(name):
    return json.dumps({
        "reviewer": name,
        "decision": "reject",
        "scores": {},
        "strengths": [],
        "weaknesses": [],
        "summary_comment": "summary",
    })


class FakeReviewer:
    def __init__(self, paper, reviewer_type, topic, api_key, provider, model):
        self.name = "Reviewer"
        self.prompts = []

    def call(self, prompt):
        self.prompts.append(prompt)
        return _review(self.name)


class FakeAuthor:
    name = "Author"

    def __init__(self, paper, topic, api_key, provider, model):
        pass

    def call(self, prompt):
        return "author response"


class FakeConferenceRecommender(FakeAuthor):
    name = "Conference Recommender"

    def call(self, prompt):
        return json.dumps({"ICML": {"fit_score": 1}})


def _run(enable_ai_detector, detector_class):
    with patch.object(mas_loop, "Reviewer", FakeReviewer), \
         patch.object(mas_loop, "Author", FakeAuthor), \
         patch.object(mas_loop, "AIDetector", detector_class), \
         patch.object(mas_loop, "ConferenceRecommender", FakeConferenceRecommender):
        return mas_loop.main(
            paper="# Paper",
            topic="NLP",
            n_iter=2,
            reviewer_types=["reviewer_a"],
            api_key="key",
            run_citation_check=False,
            enable_ai_detector=enable_ai_detector,
        )


def test_ai_detector_is_disabled_by_default():
    class UnexpectedDetector(FakeAuthor):
        def __init__(self, *args, **kwargs):
            raise AssertionError("AI Detector should not be instantiated")

    result = _run(False, UnexpectedDetector)

    assert "AICHECKER_RESPONSE" not in result["reviewers"][0].get("raw", "")


def test_ai_detector_can_be_enabled():
    calls = []

    class FakeDetector(FakeAuthor):
        name = "AI Detector"

        def call(self, prompt):
            calls.append(prompt)
            return "detector response"

    _run(True, FakeDetector)

    assert len(calls) == 1
    assert calls[0]


def test_reviewer_prompt_omits_detector_section_when_disabled():
    prompt = mas_loop.construct_reviewer_prompt("author response")
    assert "###AUTHOR_RESPONSE###" in prompt
    assert "###AICHECKER_RESPONSE###" not in prompt

    enabled_prompt = mas_loop.construct_reviewer_prompt("author response", "detector response")
    assert "###AICHECKER_RESPONSE###\ndetector response" in enabled_prompt
