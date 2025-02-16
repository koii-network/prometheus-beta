import pytest
from src.capitalize_words import capitalize_words

def test_capitalize_words_normal_case():
    """Test capitalization of a normal string with multiple words."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_already_capitalized():
    """Test string where some words are already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_mixed_case():
    """Test string with mixed case."""
    assert capitalize_words("hELLo wORLd") == "Hello World"

def test_capitalize_words_single_word():
    """Test capitalization of a single word."""
    assert capitalize_words("hello") == "Hello"

def test_capitalize_words_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_capitalize_words_multiple_spaces():
    """Test string with multiple spaces between words."""
    assert capitalize_words("hello   world") == "Hello World"

def test_capitalize_words_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
        capitalize_words(None)
        capitalize_words(["hello", "world"])