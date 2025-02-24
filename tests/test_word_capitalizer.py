import pytest
from src.word_capitalizer import capitalize_words

def test_standard_input():
    """Test capitalization of a standard sentence."""
    assert capitalize_words("hello world") == "Hello World"

def test_already_capitalized():
    """Test input with already capitalized words."""
    assert capitalize_words("Hello World") == "Hello World"

def test_mixed_case():
    """Test input with mixed case."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_multiple_spaces():
    """Test input with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_single_word():
    """Test single word input."""
    assert capitalize_words("hello") == "Hello"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
        capitalize_words(None)
        capitalize_words(["hello", "world"])