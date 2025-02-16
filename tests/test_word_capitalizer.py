import pytest
from src.word_capitalizer import capitalize_words

def test_capitalize_words_normal_case():
    """Test capitalizing words in a standard sentence."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_already_capitalized():
    """Test sentence with some words already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_mixed_case():
    """Test handling of mixed case words."""
    assert capitalize_words("hELLo wORLd") == "Hello World"

def test_capitalize_words_empty_string():
    """Test handling of an empty string."""
    assert capitalize_words("") == ""

def test_capitalize_words_single_word():
    """Test handling of a single word."""
    assert capitalize_words("hello") == "Hello"

def test_capitalize_words_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(None)