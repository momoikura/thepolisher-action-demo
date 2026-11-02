from tinyslug import slugify


def test_lowercases_and_joins_words():
    assert slugify("Hello World") == "hello-world"


def test_strips_punctuation_at_the_ends():
    assert slugify("!Hello!") == "hello"
