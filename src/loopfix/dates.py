"""Date and time utilities for loopfix."""

from datetime import datetime, timezone


def parse_iso8601(value: str) -> datetime:
    """Parse an ISO 8601 timestamp string into a :class:`datetime`.

    Accepts both naive timestamps (``2026-09-11T10:30:00``) and UTC timestamps
    with a trailing ``Z`` (``2026-09-11T10:30:00Z``).
    """
    if value.endswith("Z"):
        # Strip the trailing "Z" and parse the rest, which also accepts an
        # optional fractional-second component (e.g. "...10:30:00.5Z").
        return datetime.fromisoformat(value[:-1]).replace(tzinfo=timezone.utc)
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
