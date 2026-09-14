"""Reproduction test for gh-1: slugify drops the first character."""

from loopfix import slugify


def test_slugify_keeps_first_character():
    """slugify should return the whole phrase, not one character short."""
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_keeps_first_character_multiline():
    assert slugify("ten green bottles") == "ten-green-bottles"
