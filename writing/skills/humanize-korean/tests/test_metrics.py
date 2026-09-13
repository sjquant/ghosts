import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


METRICS_PATH = Path(__file__).parents[1] / "references" / "metrics.py"
SPEC = importlib.util.spec_from_file_location("humanize_korean_metrics", METRICS_PATH)
assert SPEC is not None and SPEC.loader is not None
metrics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(metrics)


class MetricsBehaviorTests(unittest.TestCase):
    def test_change_rate_reports_deleted_content_against_longer_input(self):
        """Given content is deleted, change_rate measures the deleted share."""
        # Given: a source whose final 40% is removed.
        before = "가나다라마바사아자차카타파하" * 1000
        after = before[: int(len(before) * 0.6)]

        # When: the source and rewrite are compared.
        rate = metrics.change_rate(before, after)

        # Then: the one-sided deletion is not diluted by similarity scoring.
        self.assertAlmostEqual(rate, 0.4, places=2)

    def test_change_rate_keeps_warning_boundaries_exact(self):
        """Given exact boundary deletions, change_rate preserves their thresholds."""
        # Given: a ten-character source and rewrites at each documented boundary.
        before = "가" * 10
        after_thirty = before[:7]
        after_fifty = before[:5]

        # When: each rewrite is compared with the same source.
        warning_boundary = metrics.change_rate(before, after_thirty)
        rollback_boundary = metrics.change_rate(before, after_fifty)

        # Then: 30% remains the warning boundary and 50% the rollback boundary.
        self.assertAlmostEqual(warning_boundary, metrics.CHANGE_RATE_WARN, places=7)
        self.assertAlmostEqual(rollback_boundary, metrics.CHANGE_RATE_ABORT, places=7)

    def test_change_rate_ignores_markdown_decoration(self):
        """Given only Markdown decoration changes, the visible change is zero."""
        # Given: the same visible text with a heading and divider removed.
        before = "# 제목\n본문\n---\n"
        after = "제목\n본문\n"

        # When: Markdown-only differences are ignored.
        rate = metrics.change_rate(before, after, ignore_markup=True)

        # Then: no content change is reported.
        self.assertEqual(rate, 0.0)

    def test_cli_reports_change_rate_from_before_and_after_files(self):
        """Given two files, the CLI exposes the same change-rate gate."""
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            before_path = directory / "before.md"
            after_path = directory / "after.md"
            before_path.write_text("가나다", encoding="utf-8")
            after_path.write_text("가나", encoding="utf-8")

            # When: comparison mode is invoked through the documented CLI.
            completed = subprocess.run(
                [
                    sys.executable,
                    str(METRICS_PATH),
                    "--before",
                    str(before_path),
                    "--after",
                    str(after_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

        # Then: the CLI prints the normalized changed-content rate.
        self.assertEqual(completed.stdout.strip(), "0.333333")

    def test_new_pattern_diagnostics_avoid_nested_metaphor_matches(self):
        """Given target and near-miss phrases, diagnostics count real matches once."""
        # Given: target phrases alongside an adverbial near miss.
        text = (
            "정리하자면 문제는 명확하다. 문제를 명확히 설명한다. 더 이상 미루지 않는다. "
            "토대를 마련한다. 발판을 마련한다. 손을 움켜쥐다. 권리를 쥐다. "
            "간과할 수 없다. 이것은 장식이 아니라 정보다."
        )

        # When: all diagnostic metrics and evidence are collected.
        result = metrics.compute_all(text, genre="report")

        # Then: near misses and nested terms do not inflate the result.
        self.assertEqual(result["metrics"]["conclusion_pivot_count"], 1)
        self.assertEqual(result["metrics"]["antithesis_count"], 1)
        self.assertEqual(result["metrics"]["clear_predicate_count"], 1)
        self.assertEqual(result["metrics"]["not_longer_count"], 1)
        self.assertEqual(result["metrics"]["foundation_metaphor_count"], 2)
        self.assertEqual(result["metrics"]["conceptual_metaphor_count"], 2)
        self.assertEqual(
            result["evidence"]["conceptual_metaphors"], ["움켜쥐다", "쥐다"]
        )
        self.assertEqual(result["metrics"]["signature_phrase_count"], 1)

    def test_new_pattern_diagnostics_ignore_near_misses(self):
        """Given similar wording without the target construction, counters stay zero."""
        # Given: phrases that resemble the new patterns but do not satisfy them.
        text = "문제가 명확히 보인다. 더는 언급하지 않는다. 토대를 분석한다."

        # When: the diagnostic counters inspect the text.
        result = metrics.compute_all(text)

        # Then: only the exact, semantically constrained patterns are counted.
        self.assertEqual(result["metrics"]["antithesis_count"], 0)
        self.assertEqual(result["metrics"]["clear_predicate_count"], 0)
        self.assertEqual(result["metrics"]["not_longer_count"], 0)
        self.assertEqual(result["metrics"]["foundation_metaphor_count"], 0)
        self.assertEqual(result["metrics"]["conceptual_metaphor_count"], 0)
        self.assertEqual(result["metrics"]["signature_phrase_count"], 0)

    def test_single_risk_family_cannot_produce_high_risk(self):
        """Given one unusually high family, risk stays below high."""
        # Given: punctuation is extreme while every other family is quiet.
        base_metrics = {
            "ending_comma_rate": 1.0,
            "comma_inclusion_rate": 1.0,
            "conclusion_pivot_count": 0,
            "safe_balance_count": 0,
            "hanja_nominalizer_density": 0.0,
            "normalisation_score": 0.0,
            "da_streak_count": 0,
        }

        # When: the coarse risk band is classified.
        risk_band, _ = metrics.classify_risk(base_metrics, {"weighted_total": 0.0})

        # Then: a single family cannot yield a high verdict.
        self.assertNotEqual(risk_band, "high")

        # Given: two independent high-signal families are present.
        base_metrics["conclusion_pivot_count"] = 3
        base_metrics["safe_balance_count"] = 3

        # When: the same score gate is evaluated again.
        risk_band, _ = metrics.classify_risk(base_metrics, {"weighted_total": 0.0})

        # Then: the high band remains available when the independent-family gate is met.
        self.assertEqual(risk_band, "high")

    def test_pronoun_density_remains_diagnostic_only(self):
        """Given high pronoun density, the interference score does not increase."""
        # Given: all interference inputs are neutral except pronoun density.
        current_metrics = {
            "inanimate_subject_rate": 0.0,
            "by_passive_count": 0,
            "double_passive_count": 0,
            "pronoun_density": 1.0,
            "deul_overuse_rate": 0.0,
            "relative_clause_nesting_count": 0,
            "have_make_literal_count": 0,
            "double_particle_count": 0,
            "progressive_aspect_rate": 0.0,
        }

        # When: the weighted interference index is calculated.
        result = metrics.interference_index("본문", current_metrics)

        # Then: pronoun density is visible but contributes no risk weight.
        self.assertEqual(result["weighted_total"], 0.0)
        self.assertEqual(result["diagnostic_only"], ["T3_pronoun_density"])


if __name__ == "__main__":
    unittest.main()
