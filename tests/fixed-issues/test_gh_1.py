"""Reproduction test for gh-1: slugify drops the first character of its result."""

from loopfix import slugify


def test_slugify_keeps_first_character():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_keeps_first_character_multi_word():
    assert slugify("ten green bottles") == "ten-green-bottles"
