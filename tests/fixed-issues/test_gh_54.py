"""Reproduction for gh-54: word_count must count hyphen-separated terms separately."""

from loopfix import word_count


def test_word_count_skips_pure_separator_run():
    """A separator run like ``---`` contains no alphanumeric character and must not count."""
    assert word_count("hello --- world") == 2


def test_word_count_plain_words_unchanged():
    """Normal whitespace-separated text is still counted word by word."""
    assert word_count("one two three") == 3


def test_word_count_hyphenated_compound_unchanged():
    """A hyphenated compound still counts as a single word."""
    assert word_count("state-of-the-art") == 1


def test_word_count_empty_and_spaced_unchanged():
    """Empty input and whitespace padding still behave as before."""
    assert word_count("") == 0
    assert word_count("  spaced   out  ") == 2
