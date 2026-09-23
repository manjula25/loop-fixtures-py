"""Name-formatting helpers (WI-13 seed)."""


def initials(full_name: str, split_hyphens: bool = True) -> str:
    """Initials, one letter per name segment, joined with dots.

    Hyphenated segments contribute one initial each and every initial is
    uppercase: ``initials("Ada Lovelace") == "A.L"``;
    ``initials("Jean-Luc Picard") == "J.L.P"``;
    ``initials("ada lovelace") == "A.L"``.

    ``split_hyphens`` controls how a hyphenated name segment is treated.
    With ``split_hyphens=True`` (the default) each hyphenated part is its own
    segment, so ``initials("Jean-Luc Picard") == "J.L.P"`` (legal-documents
    exporter). With ``split_hyphens=False`` a hyphenated name counts as one
    segment, so ``initials("Jean-Luc Picard", split_hyphens=False) == "J.P"``
    (badge renderer).
    """
    words = full_name.split()
    parts = []
    for w in words:
        if split_hyphens:
            parts.extend(segment[0].upper() for segment in w.split("-"))
        else:
            parts.append(w[0].upper())
    return ".".join(parts)
