import pytest
from src.capitalize_words import capitalize_words

def test_normal_sentence():
    assert capitalize_words("hello world") == "Hello World"

def test_multiple_words():
    assert capitalize_words("python is awesome") == "Python Is Awesome"

def test_empty_string():
    assert capitalize_words("") == ""

def test_single_word():
    assert capitalize_words("hello") == "Hello"

def test_already_capitalized():
    assert capitalize_words("Hello World") == "Hello World"

def test_mixed_case():
    assert capitalize_words("hELLo wORLd") == "Hello World"

def test_extra_whitespaces():
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_non_string_input():
    with pytest.raises(AttributeError):
        capitalize_words(123)  # Should raise an AttributeError