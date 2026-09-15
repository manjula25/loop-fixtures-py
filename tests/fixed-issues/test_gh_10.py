"""Reproduction for gh-10: word_count breaks on empty string and multi-space runs."""

from loopfix import word_count


def test_word_count_empty_string():
    """An empty string contains no words."""
    assert word_count("") == 0


def test_word_count_multi_space_run():
    """Runs of whitespace (including leading/trailing) do not produce empty words."""
    assert word_count("  spaced   out  ") == 2


def test_word_count_single_spaces_still_works():
    """Regular single-space-separated text still counts correctly."""
    assert word_count("one two three") == 3
