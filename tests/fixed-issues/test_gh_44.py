from loopfix.numops import percentfmt


def test_percentfmt_whole_numbers_drop_decimal():
    assert percentfmt(1, 4) == "25%"
    assert percentfmt(1, 2) == "50%"
