"""Reproduction for gh-3: titlecase returns ALL CAPS instead of Title Case."""

from loopfix import titlecase


def test_titlecase_capitalizes_each_word():
    """Each word's first letter is capitalized, the rest left unchanged."""
    assert titlecase("hello world") == "Hello World"


def test_titlecase_preserves_remaining_casing():
    """Letters after the first are not uppercased (no ALL CAPS)."""
    assert titlecase("pyTest suite") == "PyTest Suite"


def test_titlecase_single_word():
    """A single word still gets only its first letter capitalized."""
    assert titlecase("loopfix text utils") == "Loopfix Text Utils"
