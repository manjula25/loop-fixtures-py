from loopfix.numops import percentfmt


def test_percentfmt_over_100_leading_plus():
    assert percentfmt(5, 3) == "+166.7%"
    assert percentfmt(4, 3) == "+133.3%"
