"""Scoring helpers for the naive-vs-agentic Q&A eval.

Reuses the confusion-matrix / F1 logic from `scripts/validate_run.py` but
generalized to take arbitrary `{key: level}` dicts instead of the audit
matrix shape, and adds a Q&A-flavored level extractor for naive answers.
"""
from __future__ import annotations

import re
from collections import defaultdict

from sentinel.config import PRICING
from sentinel.models import normalize_level  # re-exported for eval callers

LEVEL_ORDER = {"compliant": 0, "partial": 1, "gap": 2}


def to_binary_level(level: str | None) -> str | None:
    """Collapse compliant/partial/gap to compliant/non_compliant.

    Binary scoring is the headline sop_compliance metric because the
    partial-vs-gap distinction is severity granularity, not an audit-action
    boundary — both partial and gap mean "something needs remediation".
    """
    if not level:
        return None
    normalized = normalize_level(level)
    return "compliant" if normalized == "compliant" else "non_compliant"


def extract_compliance_level(text: str) -> str | None:
    """Heuristically pull a compliance verdict out of a freeform answer.

    Used to score `sop_compliance` questions when the model wasn't asked to
    emit JSON. Looks for tagged phrases first ("Compliance level: gap"),
    then falls back to keyword frequency.
    """
    if not text:
        return None
    lowered = text.lower()

    tagged = re.search(
        r"(?:compliance[ _-]?level|verdict|assessment|conclusion)\s*[:\-]\s*"
        r"(compliant|partial|partially compliant|gap|non[- _]?compliant)",
        lowered,
    )
    if tagged:
        return normalize_level(tagged.group(1).replace("partially compliant", "partial"))

    # "compliant" must not match inside "non-compliant"/"non compliant"/"not
    # compliant" — the hyphen/space before it is a word boundary, so without
    # the lookbehinds every negative mention also counts as compliant.
    # "missing" is deliberately not a gap keyword: it routinely appears in
    # compliant answers ("no controls are missing").
    counts = {
        "gap": len(re.findall(r"\b(gap|non[- _]?compliant|not (?:fully )?compliant|fails to)\b", lowered)),
        "partial": len(re.findall(r"\bpartial(?:ly)?\b", lowered)),
        "compliant": len(re.findall(r"(?<!non-)(?<!non )(?<!not )(?<!not fully )\bcompliant\b", lowered)),
    }
    if not any(counts.values()):
        return None
    return max(counts, key=counts.get)


def compute_metrics(gt: dict, predicted: dict) -> dict:
    """Confusion matrix + FP/FN against a `{key: level}` ground truth.

    Mirrors `scripts/validate_run.py:compute_metrics`. `key` is opaque
    (we use `question_id` for Q&A eval; `(sop_id, regulation)` for the
    full audit eval). Missing predictions are counted in `missing_in_run`.
    """
    matched = 0
    total = 0
    missing_in_run = []
    extra_in_run = 0
    mismatches = []
    confusion: dict = defaultdict(int)
    false_positives = 0
    false_negatives = 0

    for key, gt_level in gt.items():
        if key in predicted:
            pred_level = predicted[key]
            total += 1
            confusion[(gt_level, pred_level)] += 1
            if gt_level == pred_level:
                matched += 1
            else:
                direction = LEVEL_ORDER.get(pred_level, 0) - LEVEL_ORDER.get(gt_level, 0)
                if direction > 0:
                    false_positives += 1
                else:
                    false_negatives += 1
                mismatches.append({"key": key, "expected": gt_level, "predicted": pred_level})
        else:
            missing_in_run.append(key)

    for key in predicted:
        if key not in gt:
            extra_in_run += 1

    return {
        "matched": matched,
        "total": total,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "mismatches": mismatches,
        "missing_in_run": missing_in_run,
        "extra_in_run": extra_in_run,
        "confusion": dict(confusion),
    }


def binary_compliance_metrics(gt: dict, predicted: dict) -> dict:
    """Binary compliant/non-compliant scoring with `non_compliant` as the positive class.

    Maps the 3-class GT and predictions through `to_binary_level` before
    scoring. Returns confusion-matrix counts plus precision/recall/F1 for
    both classes (the "compliant" class is the minority in audit datasets, so
    its own F1 is worth reporting alongside the majority class).
    """
    tp = fp = tn = fn = 0
    matched = 0
    mismatches = []

    for key, gt_level in gt.items():
        if key not in predicted:
            continue
        exp_bin = to_binary_level(gt_level)
        pred_bin = to_binary_level(predicted[key])
        if exp_bin is None or pred_bin is None:
            continue
        if exp_bin == pred_bin:
            matched += 1
        else:
            mismatches.append({"key": key, "expected": exp_bin, "predicted": pred_bin})

        if exp_bin == "non_compliant" and pred_bin == "non_compliant":
            tp += 1
        elif exp_bin == "non_compliant" and pred_bin == "compliant":
            fn += 1
        elif exp_bin == "compliant" and pred_bin == "non_compliant":
            fp += 1
        else:
            tn += 1

    n = tp + fp + tn + fn
    accuracy = matched / n if n else 0.0
    prec_nc = tp / (tp + fp) if (tp + fp) else 0.0
    rec_nc = tp / (tp + fn) if (tp + fn) else 0.0
    f1_nc = 2 * prec_nc * rec_nc / (prec_nc + rec_nc) if (prec_nc + rec_nc) else 0.0
    prec_c = tn / (tn + fn) if (tn + fn) else 0.0
    rec_c = tn / (tn + fp) if (tn + fp) else 0.0
    f1_c = 2 * prec_c * rec_c / (prec_c + rec_c) if (prec_c + rec_c) else 0.0
    return {
        "n": n,
        "matched": matched,
        "accuracy": accuracy,
        "tp_non_compliant": tp,
        "fp_non_compliant": fp,
        "tn_compliant": tn,
        "fn_non_compliant": fn,
        "precision_non_compliant": prec_nc,
        "recall_non_compliant": rec_nc,
        "f1_non_compliant": f1_nc,
        "precision_compliant": prec_c,
        "recall_compliant": rec_c,
        "f1_compliant": f1_c,
        "macro_f1": (f1_nc + f1_c) / 2,
        "mismatches": mismatches,
    }


def macro_f1(confusion: dict, classes: tuple[str, ...] = ("compliant", "partial", "gap")) -> float:
    """Unweighted macro F1 across the named classes."""
    f1s = []
    for cls in classes:
        tp = confusion.get((cls, cls), 0)
        fp = sum(confusion.get((g, cls), 0) for g in classes if g != cls)
        fn = sum(confusion.get((cls, p), 0) for p in classes if p != cls)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        f1s.append(f1)
    return sum(f1s) / len(f1s) if f1s else 0.0


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Tokens × `PRICING` (USD per 1M tokens)."""
    prices = PRICING.get(model, {"input": 0, "output": 0})
    return (input_tokens / 1_000_000) * prices["input"] + (output_tokens / 1_000_000) * prices["output"]
