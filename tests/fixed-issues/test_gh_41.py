from loopfix.moneyops import moneyfmt


def test_moneyfmt_negative_sign():
    assert moneyfmt(-5.25) == "-$5.25"
    assert moneyfmt(-1234567.89) == "-$1,234,567.89"
