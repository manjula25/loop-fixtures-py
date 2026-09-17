"""Reproduction for spec-titlecase-returns-all-caps-instead-of-title-case.

``titlecase`` should capitalize the first letter of each word and leave the
rest of each word's casing untouched, but it instead upper-cases the whole
string.
"""

from loopfix import titlecase


def test_titlecase_basic_two_words():
    """``titlecase("hello world")`` must be ``"Hello World"`` not ``"HELLO WORLD"``."""
    assert titlecase("hello world") == "Hello World"


def test_titlecase_preserves_inner_casing():
    """Interior letters keep their original casing: ``pyTest suite`` -> ``PyTest Suite``."""
    assert titlecase("pyTest suite") == "PyTest Suite"


def test_titlecase_loopfix_text_utils():
    assert titlecase("loopfix text utils") == "Loopfix Text Utils"


def test_titlecase_single_letter():
    assert titlecase("a") == "A"
