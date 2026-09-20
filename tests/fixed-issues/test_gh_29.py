from loopfix.textops import slugify


def test_slugify_keeps_digits():
    assert slugify("version 2") == "version-2"
    assert slugify("python 3 guide") == "python-3-guide"
    assert slugify("Hello, World!") == "hello-world"
