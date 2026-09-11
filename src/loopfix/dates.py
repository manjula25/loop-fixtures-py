"""Date and time utilities for loopfix."""

from datetime import datetime


def parse_iso8601(value: str) -> datetime:
    """Parse an ISO 8601 timestamp string into a :class:`datetime`.

    Accepts both naive timestamps (``2026-09-11T10:30:00``) and UTC timestamps
    with a trailing ``Z`` (``2026-09-11T10:30:00Z``).
    """
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
