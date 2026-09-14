"""Reproduction test for gh-2: parse_iso8601 ValueError on UTC timestamps ending in Z."""

from datetime import datetime, timezone

from loopfix.dates import parse_iso8601


def test_parse_iso8601_utc_z_suffix():
    """parse_iso8601 should accept a trailing-Z UTC timestamp."""
    assert parse_iso8601("2026-09-11T10:30:00Z") == datetime(
        2026, 9, 11, 10, 30, 0, tzinfo=timezone.utc
    )
