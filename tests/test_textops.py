"""Tests for loopfix.textops."""

from loopfix.textops import slugify, titlecase, word_count


class TestSlugify:
    def test_basic_phrase(self):
        assert slugify("Hello, World!") == "hello-world"


class TestTitlecase:
    def test_capitalizes_each_word(self):
        assert titlecase("hello world") == "Hello World"


class TestWordCount:
    def test_counts_words(self):
        assert word_count("one two three") == 3

    def test_empty_string(self):
        assert word_count("") == 0

    def test_whitespace_runs(self):
        assert word_count("  spaced   out  ") == 2
