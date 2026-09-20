from loopfix.moneyops import moneyfmt


def test_moneyfmt_thousands_separators():
    assert moneyfmt(1234567.89) == "$1,234,567.89"
    assert moneyfmt(2500000.0) == "$2,500,000.00"
