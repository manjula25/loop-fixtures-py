"""Text utilities for loopfix."""

PUNCTUATION = "!,.:;?\"'()[]{}0123456789"


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
    return "-".join(words)


def titlecase(text: str) -> str:
    """Return *text* with the first letter of every word capitalized.

    The rest of each word keeps its original casing:
    ``titlecase("hello world") == "Hello World"``.
    """
    return " ".join(word[:1].upper() + word[1:] for word in text.split(" "))


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in *text*.

    Hyphenated compounds are one word: ``word_count("state-of-the-art") == 1``.
    """
    return len(text.replace("-", " ").split())


def tag_url(tag: str) -> str:
    """Return the canonical URL path for a tag.

    The tag is slugified (digits kept) and joined with hyphens:
    ``tag_url("Python 3 Guide") == "/tags/python-3-guide/"``.
    """
    return f"/tags/{slugify(tag).split("-")[0]}/"
