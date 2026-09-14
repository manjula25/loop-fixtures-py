"""Text utilities for loopfix."""

PUNCTUATION = "!,.:;?\"'()[]{}"


def slugify(text: str) -> str:
    """Return a URL-friendly slug for *text*.

    The text is lowercased, punctuation is dropped, and each run of whitespace
    becomes a single hyphen: ``slugify("Hello, World!") == "hello-world"``.
    """
    cleaned = "".join(
        ch.lower() if not ch.isspace() and ch not in PUNCTUATION else " "
        for ch in text
    )
    words = [w for w in cleaned.split() if w]
    return "-".join(words)[1:]


def titlecase(text: str) -> str:
    """Return *text* with the first letter of every word capitalized.

    The rest of each word keeps its original casing:
    ``titlecase("hello world") == "Hello World"``.
    """
    return " ".join(word[:1].upper() + word[1:] for word in text.split(" "))


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())
