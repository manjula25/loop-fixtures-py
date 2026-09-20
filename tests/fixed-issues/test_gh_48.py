from loopfix.nameops import initials


def test_initials_hyphenated_segments():
    assert initials("Jean-Luc Picard") == "J.L.P"
