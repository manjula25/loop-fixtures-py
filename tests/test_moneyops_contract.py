"""Money contract, superseded 2026-09-19 by the owner's decision on #26.

The WI-10 truncation pin ("fractional dollars settled by the reconciliation
job") is superseded: to_cents converts a dollar amount to integer cents,
exactly as its docstring and issue #26 specify. This file now pins the
cents contract so a regression to truncation fails loudly.
"""

from loopfix.moneyops import to_cents


def test_to_cents_converts_fractional_dollars() -> None:
    assert to_cents(1.50) == 150


def test_to_cents_small_amounts() -> None:
    assert to_cents(0.07) == 7


def test_to_cents_whole_dollars() -> None:
    assert to_cents(2.0) == 200
