"""Humanize Korean quantitative metrics.

Standard-library-only helper for the humanize-korean skill. The numbers are
not a detector verdict by themselves; they give the model a compact read on
comma habits, repeated AI phrases, translationese, and post-editese signals.

CLI:
    python metrics.py --input input.txt --genre essay
    python metrics.py --text $'첫 문장입니다.\n둘째 문장입니다.' --genre essay
    python metrics.py --before original.md --after revised.md --ignore-markup
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from collections.abc import Sequence
from statistics import StatisticsError, mean
from typing import Any

VERSION = "2.1-standalone"

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[\.!?。])\s+")
_PARAGRAPH_SPLIT_RE = re.compile(r"\n\s*\n")
_EOJEOL_SPLIT_RE = re.compile(r"\s+")
_PUNCT_STRIP_RE = re.compile(r"[\.,!?;:\(\)\[\]\{\}\"'`~、。“”‘’\-]+")
_ENDING_COMMA_RE = re.compile(r"(?:고|며|지만|면서|아서|어서)\s*,")
_ENDING_BOUNDARY_RE = re.compile(r"(?:고|며|지만|면서|아서|어서)(?=[\s,\.!?、。]|$)")
_ENDING_FINAL_RE = re.compile(r"([가-힣]{1,3})[\.!?。]?\s*$")

_CONCLUSION_PIVOTS = (
    "결론적으로",
    "따라서",
    "이를 통해",
    "그러므로",
    "요약하면",
    "정리하면",
    "정리하자면",
)
_SIGNATURE_PHRASES = (
    "시사하는 바가 크다",
    "주목할 만하다",
    "간과할 수 없다",
)
_SAFE_BALANCES = ("양쪽 모두", "두 가지 모두", "장점도 있지만", "신중하게", "균형")
_HANJA_SUFFIXES = ("성", "적", "화", "도", "력", "감", "원")
_DECLARATIVE_ENDINGS = ("한다", "된다", "이다")
_PROGRESSIVE_RE = re.compile(r"고\s*있(?:다|었|는|을|던|는다)")
_DOUBLE_PARTICLE_RE = re.compile(r"(?:에서의|에로의|으로의|에의|으로부터의|로부터의)")
_BY_PASSIVE_RE = re.compile(
    r"에\s*의(?:해|하여)\s+\S{0,12}?(?:되|받|당하|지)(?:다|었|어|ㄴ다|는다|는|ㄹ|을)"
)
_PRONOUN_RE = re.compile(
    r"(?:그녀(?:는|가|를|의|에게|와|도|만)?"
    r"|그것(?:은|이|을|의|에|에게)?"
    r"|그들(?:은|이|을|의|에게|과|도)?"
    r"|그(?:는|가|를|의|에게|와|도|만)(?=\s|[\.,!?]|$))"
)

_DOUBLE_PASSIVE_TOKENS = (
    "되어진다",
    "되어졌다",
    "되어진",
    "되어지는",
    "여지다",
    "여진다",
    "여졌다",
    "잊혀진",
    "보여진다",
    "보여졌다",
    "보여진",
    "쓰여진다",
    "쓰여졌다",
    "쓰여진",
    "닫혀진",
    "열려진",
)
_INANIMATE_DEUL_TOKENS = (
    "데이터들",
    "정보들",
    "결과들",
    "연구들",
    "아이디어들",
    "방법들",
    "문제들",
    "의견들",
    "시스템들",
    "기술들",
    "사실들",
    "사례들",
    "이론들",
    "개념들",
    "현상들",
    "특징들",
    "요소들",
    "원인들",
    "영향들",
    "변화들",
)
_HAVE_MAKE_LITERAL_TOKENS = (
    "가지고 있다",
    "가지고있다",
    "가지고 있는",
    "갖고 있다",
    "갖고있는",
    "을 가지다",
    "를 가지다",
    "을 가졌",
    "를 가졌",
    "회의를 가지",
    "결정을 내리",
    "결정을 내렸",
)

# Later upstream calibration treats these as review evidence, not automatic
# rewrite verdicts. They are intentionally exposed separately from the
# coarse risk score so a human can inspect their context.
_ANTITHESIS_RE = re.compile(
    r"(?:가|이)\s*아니라|이기\s*이전에|되기\s*이전에|이기보다|것은\s*아니다"
)
_CLEAR_PREDICATE_RE = re.compile(r"(?:은|는|이|가)\s*(?:명확|분명)(?:하다|합니다|하며|하고|해졌|하지만)")
_NOT_LONGER_RE = re.compile(r"더\s*이상[^.!?。]{0,25}(?:않|아니|없|못하|불가)")
_FOUNDATION_METAPHOR_RE = re.compile(
    r"(?:발판|토대|초석|주춧돌|교두보)(?:을|를)\s?(?:마련|놓|다지)|"
    r"(?:지평|활로)(?:을|를)\s?(?:열|연다|열었|열어)"
)
_CONCEPTUAL_METAPHORS = (
    "잠식",
    "청사진",
    "적신호",
    "경고등",
    "신호탄",
    "움켜쥐다",
    "뿌리내리다",
    "짓누르다",
    "청구서",
    "과실",
    "짊어지다",
    "쥐다",
)

_MARKUP_ONLY_LINE_RE = re.compile(
    r"^\s*(?:```.*|~~~.*|-{3,}|\*{3,}|={3,}|\|[\s:\-|]*)\s*$"
)
_MARKUP_PREFIX_RE = re.compile(
    r"^\s*(?:#{1,6}\s+|>\s?|[-*+]\s+|\d{1,3}[.)]\s+)"
)

CHANGE_RATE_WARN = 0.30
CHANGE_RATE_ABORT = 0.50
_CHANGE_RATE_EXACT_LIMIT = 2_000
_CHANGE_RATE_CHUNK_SIZE = 64


def _main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Humanize Korean metric runner")
    input_group = parser.add_mutually_exclusive_group(required=False)
    input_group.add_argument("--input", help="Input text file path")
    input_group.add_argument("--text", help="Raw input text; newlines are allowed")
    parser.add_argument("--before", help="Original text file for change-rate comparison")
    parser.add_argument("--after", help="Rewritten text file for change-rate comparison")
    parser.add_argument(
        "--ignore-markup",
        action="store_true",
        help="Ignore Markdown-only lines and prefixes during comparison",
    )
    parser.add_argument("--genre", default="essay", help="essay/report/blog/formal")
    parser.add_argument("--output", default=None, help="Optional JSON output path")
    args = parser.parse_args(argv)

    if args.before is not None or args.after is not None:
        if args.before is None or args.after is None:
            parser.error("--before and --after must be supplied together")
        if args.input is not None or args.text is not None:
            parser.error("comparison mode cannot be combined with --input or --text")
        if args.output is not None:
            parser.error("--output is only available for metric mode")
        before = read_text_file(args.before)
        after = read_text_file(args.after)
        print(f"{change_rate(before, after, ignore_markup=args.ignore_markup):.6f}")
        return 0

    if args.input is None and args.text is None:
        parser.error("one of --input, --text, or --before/--after is required")

    text = read_cli_text(args)
    result = compute_all(text, genre=args.genre)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as output_file:
            json.dump(result, output_file, ensure_ascii=False, indent=2)

    print(result["risk_band"])
    return 0


def read_cli_text(args: argparse.Namespace) -> str:
    """Return text from either a file path or a raw CLI argument."""
    if args.text is not None:
        return args.text

    return read_text_file(args.input)


def read_text_file(path: str) -> str:
    """Read UTF-8 text from a path supplied to the CLI."""
    with open(path, "r", encoding="utf-8") as input_file:
        return input_file.read()


def compute_all(text: str, genre: str = "essay") -> dict[str, Any]:
    """Compute all supported metrics and a heuristic risk band."""
    metrics = {
        "comma_inclusion_rate": comma_inclusion_rate(text),
        "comma_usage_rate": comma_usage_rate(text),
        "ending_comma_rate": ending_comma_rate(text),
        "comma_segment_length": comma_segment_length(text),
        "conclusion_pivot_count": conclusion_pivot_count(text),
        "signature_phrase_count": signature_phrase_count(text),
        "safe_balance_count": safe_balance_count(text),
        "hanja_nominalizer_density": hanja_nominalizer_density(text),
        "lexical_diversity": lexical_diversity(text),
        "lexical_density": lexical_density(text),
        "ending_diversity": ending_diversity(text),
        "normalisation_score": normalisation_score(text),
        "da_streak_count": da_streak_count(text),
        "inanimate_subject_rate": inanimate_subject_rate(text),
        "by_passive_count": by_passive_count(text),
        "double_passive_count": double_passive_count(text),
        "pronoun_density": pronoun_density(text),
        "deul_overuse_rate": deul_overuse_rate(text),
        "relative_clause_nesting_count": relative_clause_nesting_count(text),
        "have_make_literal_count": have_make_literal_count(text),
        "double_particle_count": double_particle_count(text),
        "progressive_aspect_rate": progressive_aspect_rate(text),
        "antithesis_count": antithesis_count(text),
        "clear_predicate_count": clear_predicate_count(text),
        "not_longer_count": not_longer_count(text),
        "foundation_metaphor_count": foundation_metaphor_count(text),
        "conceptual_metaphor_count": conceptual_metaphor_count(text),
    }
    interference = interference_index(text, metrics)
    risk_band, risk_score = classify_risk(metrics, interference)

    return {
        "version": VERSION,
        "genre": genre,
        "char_count": len(text),
        "sentence_count": len(split_sentences(text)),
        "metrics": metrics,
        "interference_index": interference,
        "risk_band": risk_band,
        "risk_score": risk_score,
        "evidence": evidence(text),
    }


def change_rate(before: str, after: str, ignore_markup: bool = False) -> float:
    """Return deterministic changed-content rate between two texts.

    Short inputs use a character-level diff whose denominator is the longer
    input, so one-sided deletions are not diluted by a similarity-ratio
    denominator. Long inputs use fixed-size chunks to keep pathological,
    repetitive comparisons bounded and deterministic. This is a comparison
    helper, not a quality verdict. The skill uses 30% as a warning threshold
    and 50% as a rollback threshold. Markup can be ignored when heading/list
    changes would otherwise dominate the reading.
    """
    if ignore_markup:
        before = _strip_markup(before)
        after = _strip_markup(after)
    if not before and not after:
        return 0.0
    if max(len(before), len(after)) <= _CHANGE_RATE_EXACT_LIMIT:
        opcodes = difflib.SequenceMatcher(
            None, before, after, autojunk=False
        ).get_opcodes()
        changed = sum(
            max(i2 - i1, j2 - j1)
            for tag, i1, i2, j1, j2 in opcodes
            if tag != "equal"
        )
        return changed / max(len(before), len(after))
    return _chunked_change_rate(before, after)


def _chunked_change_rate(before: str, after: str) -> float:
    """Return a bounded, conservative rate for long inputs."""
    total = max(len(before), len(after))
    changed = 0
    for start in range(0, total, _CHANGE_RATE_CHUNK_SIZE):
        before_chunk = before[start : start + _CHANGE_RATE_CHUNK_SIZE]
        after_chunk = after[start : start + _CHANGE_RATE_CHUNK_SIZE]
        if before_chunk != after_chunk:
            changed += max(len(before_chunk), len(after_chunk))
    return changed / total


def _strip_markup(text: str) -> str:
    """Remove common Markdown decoration while preserving visible text."""
    kept: list[str] = []
    for line in text.splitlines():
        if _MARKUP_ONLY_LINE_RE.match(line):
            continue
        kept.append(_MARKUP_PREFIX_RE.sub("", line))
    return "\n".join(kept)


def comma_inclusion_rate(text: str) -> float:
    """Return the ratio of sentences containing at least one comma."""
    sentences = split_sentences(text)
    if not sentences:
        return 0.0
    return sum(1 for sentence in sentences if "," in sentence) / len(sentences)


def comma_usage_rate(text: str) -> float:
    """Return average comma count per sentence."""
    sentences = split_sentences(text)
    if not sentences:
        return 0.0
    return sum(sentence.count(",") for sentence in sentences) / len(sentences)


def ending_comma_rate(text: str) -> float:
    """Return the ratio of connective endings immediately followed by a comma."""
    endings = _ENDING_BOUNDARY_RE.findall(text)
    if not endings:
        return 0.0
    return len(_ENDING_COMMA_RE.findall(text)) / len(endings)


def comma_segment_length(text: str) -> float:
    """Return average eojeol count in comma-delimited segments."""
    segment_lengths: list[int] = []
    for sentence in split_sentences(text):
        segments = sentence.split(",") if "," in sentence else [sentence]
        for segment in segments:
            tokens = eojeols(segment)
            if tokens:
                segment_lengths.append(len(tokens))
    if not segment_lengths:
        return 0.0
    return sum(segment_lengths) / len(segment_lengths)


def conclusion_pivot_count(text: str) -> int:
    """Count conclusion-pivot phrases."""
    return count_lexicon(text, _CONCLUSION_PIVOTS)


def signature_phrase_count(text: str) -> int:
    """Count signature phrases that need contextual review."""
    return count_lexicon(text, _SIGNATURE_PHRASES)


def safe_balance_count(text: str) -> int:
    """Count safe-balance hedge phrases."""
    return count_lexicon(text, _SAFE_BALANCES)


def hanja_nominalizer_density(text: str) -> float:
    """Return token-level density of 한자어 nominalizer-like endings."""
    tokens = stripped_eojeols(text)
    if not tokens:
        return 0.0
    hits = sum(
        1 for token in tokens if len(token) >= 2 and token[-1] in _HANJA_SUFFIXES
    )
    return hits / len(tokens)


def lexical_diversity(text: str) -> float:
    """Return type-token ratio over eojeols."""
    tokens = stripped_eojeols(text)
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def lexical_density(text: str) -> float:
    """Return a standard-library proxy for content-word density."""
    tokens = stripped_eojeols(text)
    if not tokens:
        return 0.0

    content_endings = (
        "한다",
        "된다",
        "이다",
        "했다",
        "였다",
        "었다",
        "답다",
        "스럽다",
        "롭다",
    )
    stopwords = {
        "그리고",
        "그러나",
        "하지만",
        "또한",
        "또는",
        "혹은",
        "즉",
        "이는",
        "따라서",
    }
    hits = 0
    for token in tokens:
        if len(token) < 2 or token in stopwords:
            continue
        if token[-1] in _HANJA_SUFFIXES or token.endswith(content_endings):
            hits += 1
    return hits / len(tokens)


def ending_diversity(text: str) -> float:
    """Return unique sentence-ending keys divided by sentence count."""
    keys: list[str] = []
    for sentence in split_sentences(text):
        match = _ENDING_FINAL_RE.search(sentence)
        if match:
            keys.append(match.group(1))
    if not keys:
        return 0.0
    return len(set(keys)) / len(keys)


def normalisation_score(text: str) -> float:
    """Return concentration of canonical declarative endings."""
    sentences = split_sentences(text)
    if not sentences:
        return 0.0
    hits = 0
    for sentence in sentences:
        last = last_eojeol(sentence)
        if last.endswith(_DECLARATIVE_ENDINGS):
            hits += 1
    return hits / len(sentences)


def da_streak_count(text: str) -> int:
    """Count sentence runs where '-다' endings repeat four or more times."""
    streaks = 0
    current = 0
    for sentence in split_sentences(text):
        if last_eojeol(sentence).endswith("다"):
            current += 1
            continue
        if current >= 4:
            streaks += 1
        current = 0
    if current >= 4:
        streaks += 1
    return streaks


def inanimate_subject_rate(text: str) -> float:
    """Return rate of sentences with abstract subjects and universal verbs."""
    sentences = split_sentences(text)
    if not sentences:
        return 0.0

    subjects = (
        "연구",
        "데이터",
        "분석",
        "결과",
        "시스템",
        "기술",
        "사례",
        "현상",
        "이론",
        "정책",
        "보고서",
        "AI",
        "인공지능",
        "모델",
        "알고리즘",
        "변화",
        "위기",
        "혁신",
    )
    verbs = (
        "보여준다",
        "보여줬다",
        "시사한다",
        "만든다",
        "드러낸다",
        "제시한다",
        "나타낸다",
        "증명한다",
        "말해준다",
        "의미한다",
        "가져온다",
    )
    hits = 0
    for sentence in sentences:
        tokens = stripped_eojeols(sentence)
        if not tokens:
            continue
        head = trim_subject_marker(tokens[0])
        if (
            head in subjects or (len(head) >= 2 and head[-1] in _HANJA_SUFFIXES)
        ) and any(any(verb in token for verb in verbs) for token in tokens[1:]):
            hits += 1
    return hits / len(sentences)


def by_passive_count(text: str) -> int:
    """Count '~에 의해' followed by passive-like verbs."""
    return len(_BY_PASSIVE_RE.findall(text))


def double_passive_count(text: str) -> int:
    """Count surface forms of double passive expressions."""
    return count_lexicon(text, _DOUBLE_PASSIVE_TOKENS)


def pronoun_density(text: str) -> float:
    """Return mean paragraph density of translated personal pronouns."""
    densities: list[float] = []
    for paragraph in split_paragraphs(text):
        tokens = stripped_eojeols(paragraph)
        if tokens:
            densities.append(len(_PRONOUN_RE.findall(paragraph)) / len(tokens))
    if not densities:
        return 0.0
    try:
        return mean(densities)
    except StatisticsError:
        return 0.0


def deul_overuse_rate(text: str) -> float:
    """Return density of inanimate or abstract nouns with mechanical '-들'."""
    tokens = stripped_eojeols(text)
    if not tokens:
        return 0.0
    hits = sum(1 for token in tokens if is_deul_overuse_token(token))
    return hits / len(tokens)


def relative_clause_nesting_count(text: str) -> int:
    """Count sentences with likely left-branching relative-clause nesting."""
    nested = 0
    adnominal = re.compile(r"[가-힣]+(?:ㄴ|는|ㄹ|던|한|된|할|될|온|간)\s+[가-힣]")
    for sentence in split_sentences(text):
        if len(adnominal.findall(sentence)) >= 3:
            nested += 1
    return nested


def have_make_literal_count(text: str) -> int:
    """Count literal have/make light-verb constructions."""
    return count_lexicon(text, _HAVE_MAKE_LITERAL_TOKENS)


def double_particle_count(text: str) -> int:
    """Count double-particle forms while excluding simple '~의'."""
    return len(_DOUBLE_PARTICLE_RE.findall(text))


def progressive_aspect_rate(text: str) -> float:
    """Return '~고 있다' surface-form hits per sentence."""
    sentences = split_sentences(text)
    if not sentences:
        return 0.0
    return sum(len(_PROGRESSIVE_RE.findall(sentence)) for sentence in sentences) / len(
        sentences
    )


def antithesis_count(text: str) -> int:
    """Count common negative-positive parallel constructions for review.

    C-8 is not a verdict by itself: a writer may use this rhetoric naturally.
    The value only helps the model inspect repeated or tightly clustered use.
    """
    return len(_ANTITHESIS_RE.findall(text))


def clear_predicate_count(text: str) -> int:
    """Count ``명확하다/분명하다`` predicate overlays, excluding adverbs."""
    return len(_CLEAR_PREDICATE_RE.findall(text))


def not_longer_count(text: str) -> int:
    """Count likely ``더 이상 ... 않다/아니다`` change constructions."""
    return len(_NOT_LONGER_RE.findall(text))


def foundation_metaphor_count(text: str) -> int:
    """Count foundation/opening metaphors that need contextual review."""
    return len(_FOUNDATION_METAPHOR_RE.findall(text))


def conceptual_metaphor_count(text: str) -> int:
    """Count a conservative family of conceptual-metaphor surface forms."""
    return len(conceptual_metaphor_hits(text))


def conceptual_metaphor_hits(text: str) -> list[str]:
    """Return longest-first, non-overlapping conceptual-metaphor matches."""
    occupied: list[tuple[int, int]] = []
    matches: list[tuple[int, str]] = []
    for term in sorted(_CONCEPTUAL_METAPHORS, key=len, reverse=True):
        for match in re.finditer(re.escape(term), text):
            start, end = match.span()
            overlaps = any(
                start < occupied_end and end > occupied_start
                for occupied_start, occupied_end in occupied
            )
            if overlaps:
                continue
            occupied.append((start, end))
            matches.append((start, term))
    return [term for _, term in sorted(matches)]


def interference_index(
    text: str, metrics: dict[str, float | int] | None = None
) -> dict[str, Any]:
    """Return weighted post-editese interference components."""
    current_metrics = metrics or compute_all(text)["metrics"]
    chars = max(len(text), 1)
    components = {
        "T1_inanimate_subject_rate": float(current_metrics["inanimate_subject_rate"]),
        "T2a_by_passive_per_1k": float(current_metrics["by_passive_count"])
        / chars
        * 1000,
        "T2b_double_passive_per_1k": float(current_metrics["double_passive_count"])
        / chars
        * 1000,
        "T3_pronoun_density": float(current_metrics["pronoun_density"]),
        "T4_deul_overuse_rate": float(current_metrics["deul_overuse_rate"]),
        "T5_nested_clause_count": float(
            current_metrics["relative_clause_nesting_count"]
        ),
        "T6_have_make_per_1k": float(current_metrics["have_make_literal_count"])
        / chars
        * 1000,
        "T7_double_particle_per_1k": float(current_metrics["double_particle_count"])
        / chars
        * 1000,
        "T8b_progressive_rate": float(current_metrics["progressive_aspect_rate"]),
    }
    weights = {
        "T1_inanimate_subject_rate": 1.0,
        "T2a_by_passive_per_1k": 0.2,
        "T2b_double_passive_per_1k": 0.2,
        # Upstream calibration found raw pronoun density is higher in some
        # human Korean prose. Keep it observable, but never let it drive risk.
        "T3_pronoun_density": 0.0,
        "T4_deul_overuse_rate": 4.0,
        "T5_nested_clause_count": 0.05,
        "T6_have_make_per_1k": 0.2,
        "T7_double_particle_per_1k": 0.5,
        "T8b_progressive_rate": 1.0,
    }
    total = sum(
        min(1.0, max(0.0, components[key] * weights[key])) for key in components
    )
    return {
        "components": components,
        "weighted_total": total,
        "diagnostic_only": ["T3_pronoun_density"],
    }


def classify_risk(
    metrics: dict[str, float | int], interference: dict[str, Any]
) -> tuple[str, int]:
    """Classify metrics while requiring more than one independent signal.

    Comma-related signals share one family because a writer's punctuation
    habit can be highly individual. A high band therefore needs both a high
    score and at least two families, rather than one unusually high metric.
    """
    punctuation = 0
    if metrics["ending_comma_rate"] > 0.35:
        punctuation += 2
    if metrics["comma_inclusion_rate"] > 0.55:
        punctuation += 1
    punctuation = min(punctuation, 3)

    rhetoric = 0
    if metrics["conclusion_pivot_count"] >= 3:
        rhetoric += 2
    if metrics["safe_balance_count"] >= 3:
        rhetoric += 1

    lexical = 0
    if metrics["hanja_nominalizer_density"] > 0.12:
        lexical += 1
    if metrics["normalisation_score"] > 0.7 or metrics["da_streak_count"] >= 1:
        lexical += 1

    translation = 0
    if interference["weighted_total"] >= 2.0:
        translation += 2
    elif interference["weighted_total"] >= 1.0:
        translation += 1

    score = punctuation + rhetoric + lexical + translation
    families = sum(
        family > 0 for family in (punctuation, rhetoric, lexical, translation)
    )

    if score >= 6 and families >= 2:
        return "high", score
    if score >= 3:
        return "medium", score
    return "low", score


def evidence(text: str) -> dict[str, list[str]]:
    """Return matched lexicon evidence that can be shown in summaries."""
    return {
        "conclusion_pivots": lexicon_hits(text, _CONCLUSION_PIVOTS),
        "signature_phrases": lexicon_hits(text, _SIGNATURE_PHRASES),
        "safe_balances": lexicon_hits(text, _SAFE_BALANCES),
        "double_passives": lexicon_hits(text, _DOUBLE_PASSIVE_TOKENS),
        "have_make_literals": lexicon_hits(text, _HAVE_MAKE_LITERAL_TOKENS),
        "conceptual_metaphors": conceptual_metaphor_hits(text),
        "foundation_metaphors": _FOUNDATION_METAPHOR_RE.findall(text),
    }


def split_sentences(text: str) -> list[str]:
    """Split Korean prose into approximate sentences."""
    stripped = text.strip()
    if not stripped:
        return []
    sentences: list[str] = []
    for part in _SENTENCE_SPLIT_RE.split(stripped):
        for line in part.splitlines():
            line = line.strip()
            if line:
                sentences.append(line)
    return sentences


def split_paragraphs(text: str) -> list[str]:
    """Split text by blank-line paragraph boundaries."""
    stripped = text.strip()
    if not stripped:
        return []
    return [
        paragraph.strip()
        for paragraph in _PARAGRAPH_SPLIT_RE.split(stripped)
        if paragraph.strip()
    ]


def eojeols(text: str) -> list[str]:
    """Split text into whitespace-separated eojeols."""
    return [token for token in _EOJEOL_SPLIT_RE.split(text.strip()) if token]


def stripped_eojeols(text: str) -> list[str]:
    """Return eojeols with surrounding punctuation removed."""
    return [
        token
        for token in (_PUNCT_STRIP_RE.sub("", raw) for raw in eojeols(text))
        if token
    ]


def last_eojeol(sentence: str) -> str:
    """Return the final punctuation-stripped eojeol in a sentence."""
    tokens = stripped_eojeols(sentence)
    return tokens[-1] if tokens else ""


def trim_subject_marker(token: str) -> str:
    """Remove a short Korean subject/topic marker from one token."""
    for marker in ("은", "는", "이", "가", "도"):
        if token.endswith(marker) and len(token) > len(marker):
            return token[: -len(marker)]
    return token


def is_deul_overuse_token(token: str) -> bool:
    """Return true for abstract '-들' tokens with optional 조사 attached."""
    if token in _INANIMATE_DEUL_TOKENS:
        return True
    for base in _INANIMATE_DEUL_TOKENS:
        if token.startswith(base) and 1 <= len(token) - len(base) <= 2:
            return all("가" <= char <= "힣" for char in token[len(base) :])
    return False


def count_lexicon(text: str, lexicon: Sequence[str]) -> int:
    """Count every occurrence of the supplied lexicon items."""
    return sum(text.count(item) for item in lexicon)


def lexicon_hits(text: str, lexicon: Sequence[str]) -> list[str]:
    """Return lexicon items present in text, preserving lexicon order."""
    return [item for item in lexicon if item in text]


if __name__ == "__main__":
    sys.exit(_main())
