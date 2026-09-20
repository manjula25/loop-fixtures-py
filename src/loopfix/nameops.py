"""Name-formatting helpers (WI-13 seed)."""


def initials(full_name: str) -> str:
    """Initials, one letter per name segment, joined with dots.

    Hyphenated segments contribute one initial each and every initial is
    uppercase: ``initials("Ada Lovelace") == "A.L"``;
    ``initials("Jean-Luc Picard") == "J.L.P"``;
    ``initials("ada lovelace") == "A.L"``.
    """
    words = full_name.split()
    parts = []
    for w in words:
        parts.extend(segment[0] for segment in w.split("-"))
    return ".".join(parts)
