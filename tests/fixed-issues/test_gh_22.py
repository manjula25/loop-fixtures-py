"""Reproduction for gh-22: clamp should respect the lower bound."""

from loopfix.numops import clamp


def test_clamp_respects_lower_bound():
    """Values below lo are clamped up to lo."""
    assert clamp(-5, 0, 10) == 0


def test_clamp_respects_upper_bound():
    """Values above hi are clamped down to hi."""
    assert clamp(15, 0, 10) == 10


def test_clamp_between_bounds_untouched():
    """Values already in [lo, hi] are returned unchanged."""
    assert clamp(5, 0, 10) == 5


def test_clamp_at_lo():
    """A value equal to lo stays lo."""
    assert clamp(0, 0, 10) == 0
