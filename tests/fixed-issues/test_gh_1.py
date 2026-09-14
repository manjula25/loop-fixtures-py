"""Reproduction test for gh-1: slugify drops the first character."""

from loopfix import slugify


def test_slugify_keeps_first_character():
    # Reported in gh-1: the leading character was stripped, so
    # "Hello, World!" became "ello-world" instead of "hello-world".
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_keeps_first_character_simple_phrase():
    # Also reported: slugify("ten green bottles") gave "en-green-bottles".
    assert slugify("ten green bottles") == "ten-green-bottles"
