"""Reproduction test for gh-3: titlecase returns ALL CAPS instead of Title Case."""

from loopfix import titlecase


def test_titlecase_not_all_caps():
    # titlecase should capitalize the first letter of each word and leave
    # the rest of each word untouched -- not uppercase the whole string.
    assert titlecase("hello world") == "Hello World"


def test_titlecase_preserves_inner_casing():
    # The rest of each word keeps its original casing.
    assert titlecase("pyTest suite") == "PyTest Suite"
