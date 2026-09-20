"""Reproduction test for gh-36: titlecase must split on any whitespace."""

from loopfix.textops import titlecase


def test_titlecase_splits_on_any_whitespace():
    assert titlecase("hello\tworld") == "Hello World"
    assert titlecase("first line\nsecond line") == "First Line Second Line"
