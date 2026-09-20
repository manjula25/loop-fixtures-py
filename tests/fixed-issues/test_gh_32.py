"""Reproduction for gh-32: word_count splits hyphenated compounds."""

from loopfix.textops import word_count


def test_word_count_hyphenated_is_one_word():
    assert word_count("state-of-the-art") == 1
    assert word_count("e-mail address") == 2


def test_word_count_unchanged_cases():
    assert word_count("one two three") == 3
    assert word_count("") == 0
