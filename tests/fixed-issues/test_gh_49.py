from loopfix.nameops import initials


def test_initials_uppercased():
    assert initials("ada lovelace") == "A.L"
