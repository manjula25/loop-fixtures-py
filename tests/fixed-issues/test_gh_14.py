"""Regression test for gh-14: fractional-second UTC timestamps ending in Z."""

from datetime import datetime, timezone

from loopfix.dates import parse_iso8601


def test_parse_fractional_second_utc_z():
    assert parse_iso8601("2026-09-11T10:30:00.5Z") == datetime(
        2026, 9, 11, 10, 30, 0, 500000, tzinfo=timezone.utc
    )


def test_parse_fractional_second_utc_z_microsecond_precision():
    assert parse_iso8601("2026-09-11T10:30:00.123456Z") == datetime(
        2026, 9, 11, 10, 30, 0, 123456, tzinfo=timezone.utc
    )
