"""Reproduction for gh-14: parse_iso8601 should handle fractional seconds before trailing Z."""

from datetime import datetime, timezone

from loopfix import parse_iso8601


def test_parse_iso8601_accepts_fractional_seconds_with_z():
    """A UTC timestamp with fractional seconds before the trailing Z parses."""
    result = parse_iso8601("2026-09-11T10:30:00.5Z")
    assert result == datetime(2026, 9, 11, 10, 30, 0, 500000, tzinfo=timezone.utc)
