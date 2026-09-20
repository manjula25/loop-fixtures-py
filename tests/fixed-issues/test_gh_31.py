from loopfix.textops import tag_url


def test_tag_url_keeps_full_slug():
    assert tag_url("python 3 guide") == "/tags/python-3-guide/"
    assert tag_url("data science") == "/tags/data-science/"


def test_tag_url_single_word_unchanged():
    assert tag_url("css") == "/tags/css/"
