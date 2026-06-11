"""Bootstrap CIs for the binary compliance metrics (Eval screen error bars)."""
from __future__ import annotations

from sentinel.eval.metrics import binary_bootstrap_ci, binary_bootstrap_ci_from_pairs


class TestBinaryBootstrapCi:
    PAIRS = (
        [("non_compliant", "non_compliant")] * 23
        + [("non_compliant", "compliant")] * 2
        + [("compliant", "non_compliant")] * 4
        + [("compliant", "compliant")] * 6
    )

    def test_point_estimates_inside_intervals(self):
        ci = binary_bootstrap_ci_from_pairs(self.PAIRS, n_boot=500, seed=1)
        assert ci["n"] == 35
        rec = 23 / 25
        prec = 23 / 27
        assert ci["recall_non_compliant"][0] <= rec <= ci["recall_non_compliant"][1]
        assert ci["precision_non_compliant"][0] <= prec <= ci["precision_non_compliant"][1]
        assert ci["accuracy"][0] < ci["accuracy"][1]  # genuine spread at n=35

    def test_empty_pairs(self):
        assert binary_bootstrap_ci_from_pairs([]) == {}

    def test_dict_wrapper_filters_unscored(self):
        gt = {"q1": "gap", "q2": "compliant", "q3": "partial"}
        pred = {"q1": "gap", "q2": "gap"}  # q3 unscored
        ci = binary_bootstrap_ci(gt, pred, n_boot=200)
        assert ci["n"] == 2
