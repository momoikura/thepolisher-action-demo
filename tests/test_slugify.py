from tinyslug import slugify


def test_lowercases_and_joins_words():
    assert slugify("Hello World") == "hello-world"


def test_strips_punctuation_at_the_ends():
    assert slugify("!Hello!") == "hello"


def test_runs_of_spaces_and_punctuation_become_one_hyphen():
    assert slugify("Hello,  World") == "hello-world"
