"""Collect the checked-in offline evaluation in the normal test suite."""

from scripts.evaluate_routing import main


def test_offline_evaluation() -> None:
    main()
