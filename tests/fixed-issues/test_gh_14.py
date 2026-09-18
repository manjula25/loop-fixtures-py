"""Reproduction for gh-14: parse_iso8601 fails on fractional-second Z timestamps."""

from datetime import datetime, timezone

from loopfix import parse_iso8601


def test_parse_fractional_second_z():
    """A UTC timestamp with fractional seconds before the trailing Z parses."""
    result = parse_iso8601("2026-09-11T10:30:00.5Z")
    assert result == datetime(2026, 9, 11, 10, 30, 0, 500000, tzinfo=timezone.utc)
    assert result.tzinfo is timezone.utc


def test_whole_second_z_still_works():
    """Whole-second Z timestamps that previously worked keep working."""
    result = parse_iso8601("2026-09-11T10:30:00Z")
    assert result == datetime(2026, 9, 11, 10, 30, 0, tzinfo=timezone.utc)


def test_naive_timestamp_still_works():
    """Naive timestamps without a trailing Z keep working."""
    result = parse_iso8601("2026-09-11T10:30:00")
    assert result == datetime(2026, 9, 11, 10, 30, 0)
