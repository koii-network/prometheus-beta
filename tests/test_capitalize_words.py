import pytest
from src.capitalize_words import capitalize_words

def test_basic_capitalization():
    assert capitalize_words("hello world") == "Hello World"

def test_already_capitalized():
    assert capitalize_words("Hello World") == "Hello World"

def test_mixed_case():
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_multiple_spaces():
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_empty_string():
    assert capitalize_words("") == ""

def test_single_word():
    assert capitalize_words("python") == "Python"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        capitalize_words(123)
    
    with pytest.raises(TypeError):
        capitalize_words(None)