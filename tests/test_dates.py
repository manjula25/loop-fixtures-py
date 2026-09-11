"""Tests for loopfix.dates."""

from datetime import datetime, timezone

from loopfix.dates import parse_iso8601


class TestParseIso8601:
    def test_naive_timestamp(self):
        assert parse_iso8601("2026-09-11T10:30:00") == datetime(2026, 9, 11, 10, 30, 0)

    def test_utc_timestamp_with_z(self):
        assert parse_iso8601("2026-09-11T10:30:00Z") == datetime(
            2026, 9, 11, 10, 30, 0, tzinfo=timezone.utc
        )
