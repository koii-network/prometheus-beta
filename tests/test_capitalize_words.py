import pytest
from src.capitalize_words import capitalize_words

def test_capitalize_words_normal_case():
    """Test capitalizing a standard sentence."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_already_capitalized():
    """Test a sentence that's already partially capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_empty_string():
    """Test handling of an empty string."""
    assert capitalize_words("") == ""

def test_capitalize_words_single_word():
    """Test handling of a single word."""
    assert capitalize_words("python") == "Python"

def test_capitalize_words_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        capitalize_words(123)
    with pytest.raises(TypeError):
        capitalize_words(None)