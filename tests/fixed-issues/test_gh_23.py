"""Reproduction for gh-23: mean should return the true arithmetic average."""

from loopfix.numops import mean


def test_mean_is_true_average():
    """mean([1, 2]) is 1.5, not floor-divided to 1."""
    assert mean([1, 2]) == 1.5


def test_mean_of_even_average():
    """mean([2, 4, 6]) is 4.0 (a float, not an int)."""
    assert mean([2, 4, 6]) == 4.0
