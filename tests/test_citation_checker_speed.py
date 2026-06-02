import time
import unittest
from unittest.mock import patch

from citation_checker.checker import _check_single, check_references
from citation_checker.doi_checker import check_via_doi
from citation_checker.models import Reference, VerificationStatus


class CitationCheckerSpeedTests(unittest.TestCase):
    def test_parallel_check_preserves_input_order(self):
        refs = [
            Reference(raw_text="a", title="Title A", year="2020"),
            Reference(raw_text="b", title="Title B", year="2020"),
            Reference(raw_text="c", title="Title C", year="2020"),
        ]

        def fake_check(ref, enable_openreview=False):
            if ref.title == "Title A":
                time.sleep(0.03)
            elif ref.title == "Title B":
                time.sleep(0.01)
            return ref.title

        with patch("citation_checker.checker._check_single", side_effect=fake_check):
            results = check_references(refs, show_progress=False, max_workers=3, use_cache=False)

        self.assertEqual(results, ["Title A", "Title B", "Title C"])

    def test_duplicate_titles_are_checked_once_when_cache_enabled(self):
        refs = [
            Reference(raw_text="[1] Same title. In ICLR, 2024.", title="Same title", year="2024"),
            Reference(raw_text="[2] Same title. In ICLR, 2024.", title="Same title", year="2024"),
        ]

        with patch("citation_checker.checker._check_single", return_value="checked") as mock_check:
            results = check_references(refs, show_progress=False, max_workers=2, use_cache=True)

        self.assertEqual(results, ["checked", "checked"])
        mock_check.assert_called_once()

    def test_doi_lookup_skips_title_search_when_doi_present(self):
        raw_text = "A title. doi: 10.1000/test-doi"
        with patch("citation_checker.doi_checker._request_json", return_value={"message": {"URL": "https://doi.org/10.1000/test-doi"}}), \
             patch("citation_checker.doi_checker._query_by_title") as mock_title_query:
            found, url = check_via_doi("A title", raw_text=raw_text, year="2024")

        self.assertTrue(found)
        self.assertEqual(url, "https://doi.org/10.1000/test-doi")
        mock_title_query.assert_not_called()

    def test_explicit_arxiv_reference_skips_openreview(self):
        ref = Reference(
            raw_text="[1] Example Paper. arXiv:2403.11237, 2024.",
            title="Example Paper",
            year="2024",
        )

        with patch("citation_checker.checker.check_on_arxiv", return_value=(True, "https://arxiv.org/abs/2403.11237")) as mock_arxiv, \
             patch("citation_checker.checker.check_on_openreview") as mock_openreview, \
             patch("citation_checker.checker.check_via_doi") as mock_crossref:
            result = _check_single(ref)

        self.assertEqual(result.status, VerificationStatus.VERIFIED)
        self.assertEqual(result.verified_by, "arXiv")
        mock_arxiv.assert_called_once()
        mock_openreview.assert_not_called()
        mock_crossref.assert_not_called()

    def test_openreview_is_disabled_by_default_in_checker(self):
        ref = Reference(
            raw_text="[1] Some Paper. In International Conference on Learning Representations, 2024.",
            title="Some Paper",
            year="2024",
        )

        with patch("citation_checker.checker.check_on_openreview") as mock_openreview, \
             patch("citation_checker.checker.check_on_arxiv", return_value=(False, None)), \
             patch("citation_checker.checker.check_via_doi", return_value=(False, None)), \
             patch("citation_checker.checker.check_on_dblp", return_value=(False, None)), \
             patch("citation_checker.checker.check_url_accessible", return_value=(False, "Invalid or missing URL")):
            _check_single(ref)

        mock_openreview.assert_not_called()

    def test_book_or_tutorial_reference_skips_openreview(self):
        ref = Reference(
            raw_text="[86] Fabio Zinno. ML Tutorial Day: From Motion Matching to Motion Synthesis. Proc. of GDC 2019, 2019.",
            title="ML Tutorial Day: From Motion Matching to Motion Synthesis",
            year="2019",
        )

        with patch("citation_checker.checker.check_on_openreview") as mock_openreview, \
             patch("citation_checker.checker.check_on_arxiv", return_value=(False, None)), \
             patch("citation_checker.checker.check_via_doi", return_value=(False, None)), \
             patch("citation_checker.checker.check_url_accessible", return_value=(False, "Invalid or missing URL")):
            _check_single(ref)

        mock_openreview.assert_not_called()

    def test_dblp_fallback_verifies_cs_paper_when_other_backends_miss(self):
        ref = Reference(
            raw_text="[36] Lucas Kovar, Michael Gleicher, and Frédéric Pighin. Motion graphs. In ACM SIGGRAPH 2008 classes, 2008.",
            title="Motion graphs",
            year="2008",
        )

        with patch("citation_checker.checker.check_on_arxiv", return_value=(False, None)), \
             patch("citation_checker.checker.check_via_doi", return_value=(False, None)), \
             patch("citation_checker.checker.check_on_dblp", return_value=(True, "https://dblp.org/rec/conf/siggraph/KovarGP08")) as mock_dblp:
            result = _check_single(ref)

        self.assertEqual(result.status, VerificationStatus.VERIFIED)
        self.assertEqual(result.verified_by, "DBLP")
        mock_dblp.assert_called_once()

    def test_openreview_disables_after_403(self):
        from citation_checker.openreview_checker import check_on_openreview, configure_openreview

        response = type("Resp", (), {"status_code": 403})()
        with patch("citation_checker.openreview_checker.requests.get", return_value=response) as mock_get:
            configure_openreview(reset_cache=True)
            self.assertEqual(check_on_openreview("Some ICLR Paper"), (False, None))
            self.assertEqual(check_on_openreview("Another ICLR Paper"), (False, None))

        mock_get.assert_called_once()

    def test_arxiv_disables_after_429(self):
        from citation_checker.arxiv_checker import check_on_arxiv, configure_arxiv

        response = type("Resp", (), {"status_code": 429})()
        with patch("citation_checker.arxiv_checker.requests.get", return_value=response) as mock_get:
            configure_arxiv(reset_cache=True)
            self.assertEqual(check_on_arxiv("Some Paper"), (False, None))
            self.assertEqual(check_on_arxiv("Another Paper"), (False, None))

        mock_get.assert_called_once()

    def test_parallel_execution_is_faster_than_sequential(self):
        refs = [
            Reference(raw_text=f"[{i}] Ref {i}", title=f"Ref {i}", year="2024")
            for i in range(6)
        ]

        def slow_check(_, enable_openreview=False):
            time.sleep(0.05)
            return "ok"

        with patch("citation_checker.checker._check_single", side_effect=slow_check):
            start = time.perf_counter()
            check_references(refs, show_progress=False, max_workers=1, use_cache=False)
            sequential = time.perf_counter() - start

        with patch("citation_checker.checker._check_single", side_effect=slow_check):
            start = time.perf_counter()
            check_references(refs, show_progress=False, max_workers=4, use_cache=False)
            parallel = time.perf_counter() - start

        self.assertLess(parallel, sequential * 0.75)


if __name__ == "__main__":
    unittest.main()
