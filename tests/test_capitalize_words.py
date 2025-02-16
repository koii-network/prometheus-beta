import pytest
from src.capitalize_words import capitalize_words

def test_capitalize_words_normal_case():
    """Test capitalization of a normal sentence."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_already_capitalized():
    """Test sentence that is already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_mixed_case():
    """Test sentence with mixed case."""
    assert capitalize_words("hELLo wORLd") == "Hello World"

def test_capitalize_words_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_capitalize_words_single_word():
    """Test single word input."""
    assert capitalize_words("python") == "Python"

def test_capitalize_words_multiple_spaces():
    """Test input with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(None)