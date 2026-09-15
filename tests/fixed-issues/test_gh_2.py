"""Reproduction for gh-2: parse_iso8601 should accept trailing-Z UTC timestamps."""

from datetime import datetime, timezone

from loopfix import parse_iso8601


def test_parse_iso8601_accepts_trailing_z():
    """A UTC timestamp ending in Z parses instead of raising ValueError."""
    result = parse_iso8601("2026-09-11T10:30:00Z")
    assert result == datetime(2026, 9, 11, 10, 30, 0, tzinfo=timezone.utc)
