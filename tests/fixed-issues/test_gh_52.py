from loopfix.nameops import initials


def test_badge_mode_treats_hyphenated_name_as_one_segment():
    # The badge renderer treats a hyphenated name as ONE name segment, so it
    # needs initials("Jean-Luc Picard") == "J.P".
    assert initials("Jean-Luc Picard", split_hyphens=False) == "J.P"


def test_legal_mode_treats_hyphenated_parts_as_segments():
    # The legal-documents exporter treats each hyphenated part as its own
    # segment, so it needs initials("Jean-Luc Picard") == "J.L.P". This is also
    # the default behavior pinned by gh-48, which must stay unweakened.
    assert initials("Jean-Luc Picard") == "J.L.P"
    assert initials("Jean-Luc Picard", split_hyphens=True) == "J.L.P"
