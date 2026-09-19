"""Reproduction for gh-26: to_cents truncates to whole dollars."""

from loopfix.moneyops import to_cents


def test_to_cents():
    assert to_cents(1.50) == 150
    assert to_cents(0.07) == 7
    assert to_cents(2.0) == 200
