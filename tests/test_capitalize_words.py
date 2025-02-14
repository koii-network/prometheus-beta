import pytest
from src.capitalize_words import capitalize_words

def test_capitalize_words_normal_case():
    """Test capitalization of a normal sentence."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_already_capitalized():
    """Test with already capitalized words."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_mixed_case():
    """Test with mixed case input."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_capitalize_words_empty_string():
    """Test with an empty string."""
    assert capitalize_words("") == ""

def test_capitalize_words_multiple_spaces():
    """Test with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
        
def test_capitalize_words_single_word():
    """Test capitalization of a single word."""
    assert capitalize_words("python") == "Python"