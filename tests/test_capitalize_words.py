import pytest
from src.capitalize_words import capitalize_words

def test_normal_string():
    """Test capitalizing a normal string with multiple words."""
    assert capitalize_words("hello world") == "Hello World"

def test_single_word():
    """Test capitalizing a single word."""
    assert capitalize_words("python") == "Python"

def test_empty_string():
    """Test an empty string returns an empty string."""
    assert capitalize_words("") == ""

def test_already_capitalized():
    """Test a string that is already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_mixed_case():
    """Test a string with mixed case."""
    assert capitalize_words("hELLo wORLd") == "Hello World"

def test_multiple_spaces():
    """Test a string with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        capitalize_words(None)