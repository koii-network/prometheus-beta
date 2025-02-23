import pytest
from src.capitalize_words import capitalize_words

def test_capitalize_words_normal_case():
    """Test capitalizing words in a normal sentence."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_already_capitalized():
    """Test a string that's already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_mixed_case():
    """Test a string with mixed capitalization."""
    assert capitalize_words("hElLo wORlD") == "Hello World"

def test_capitalize_words_empty_string():
    """Test an empty string."""
    assert capitalize_words("") == ""

def test_capitalize_words_multiple_spaces():
    """Test a string with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_single_word():
    """Test a single word."""
    assert capitalize_words("hello") == "Hello"

def test_capitalize_words_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(["hello", "world"])