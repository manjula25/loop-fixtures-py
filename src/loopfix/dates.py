"""Date and time utilities for loopfix."""

from datetime import datetime, timezone


def parse_iso8601(value: str) -> datetime:
    """Parse an ISO 8601 timestamp string into a :class:`datetime`.

    Accepts both naive timestamps (``2026-09-11T10:30:00``) and UTC timestamps
    with a trailing ``Z`` (``2026-09-11T10:30:00Z``), including fractional
    seconds (``2026-09-11T10:30:00.5Z``).
    """
    if value.endswith("Z"):
        # fromisoformat handles optional fractional seconds; the Z suffix is
        # normalized to the equivalent +00:00 offset first.
        return datetime.fromisoformat(f"{value[:-1]}+00:00")
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
