from loopfix.textops import titlecase


def test_titlecase_capitalizes_first_letter_past_punctuation():
    assert titlecase('"hello world"') == '"Hello World"'
    assert titlecase("'quoted text'") == "'Quoted Text'"
