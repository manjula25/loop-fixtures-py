"""Reproduction for gh-18: parse_iso8601 should handle fractional seconds on naive timestamps."""

from datetime import datetime

from loopfix import parse_iso8601


def test_parse_iso8601_accepts_fractional_seconds_naive():
    """A naive timestamp with fractional seconds (no trailing Z) parses."""
    result = parse_iso8601("2026-09-11T10:30:00.5")
    assert result == datetime(2026, 9, 11, 10, 30, 0, 500000)


def test_parse_iso8601_whole_second_naive_still_works():
    """Whole-second naive timestamps keep parsing exactly as before."""
    assert parse_iso8601("2026-09-11T10:30:00") == datetime(2026, 9, 11, 10, 30, 0)
