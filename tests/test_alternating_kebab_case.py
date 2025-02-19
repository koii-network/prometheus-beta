import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_basic_conversion():
    assert to_alternating_kebab_case("hello world") == "hello-WORLD"
    assert to_alternating_kebab_case("python programming") == "python-PROGRAMMING"

def test_special_characters():
    assert to_alternating_kebab_case("hello! world@") == "hello-WORLD"
    assert to_alternating_kebab_case("  spaces  around  ") == "spaces-AROUND"

def test_multiple_words():
    assert to_alternating_kebab_case("one two three four") == "one-TWO-three-FOUR"

def test_single_word():
    assert to_alternating_kebab_case("hello") == "hello"

def test_empty_string():
    assert to_alternating_kebab_case("") == ""

def test_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_kebab_case(123)
    with pytest.raises(TypeError):
        to_alternating_kebab_case(None)