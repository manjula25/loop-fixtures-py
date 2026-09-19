"""Contract pinned by the billing team (WI-10 conflicting requirement).

to_cents must return the whole-dollar part as an integer; fractional
dollars are settled by the reconciliation job, never here.
"""

from loopfix.moneyops import to_cents


def test_to_cents_truncates_fractional_dollars() -> None:
    assert to_cents(19.99) == 19


def test_to_cents_whole_dollars() -> None:
    assert to_cents(2.0) == 2
