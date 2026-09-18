"""Reproduction for gh-20: parse_iso8601 should handle fractional seconds on naive timestamps."""

from datetime import datetime

from loopfix import parse_iso8601


def test_parse_iso8601_accepts_fractional_seconds_naive():
    """A naive timestamp with fractional seconds parses to the corresponding datetime."""
    result = parse_iso8601("2026-09-11T10:30:00.5")
    assert result == datetime(2026, 9, 11, 10, 30, 0, 500000)
