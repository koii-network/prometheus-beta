import pytest
from src.word_capitalizer import capitalize_words

def test_basic_capitalization():
    """Test standard word capitalization."""
    assert capitalize_words("hello world") == "Hello World"

def test_already_capitalized():
    """Test string with already capitalized words."""
    assert capitalize_words("Hello World") == "Hello World"

def test_mixed_case():
    """Test string with mixed case."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_single_word():
    """Test single word capitalization."""
    assert capitalize_words("hello") == "Hello"

def test_multiple_spaces():
    """Test string with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_non_string_input():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        capitalize_words(123)
    
    with pytest.raises(TypeError):
        capitalize_words(None)

def test_string_with_numbers():
    """Test capitalization with numbers in the string."""
    assert capitalize_words("hello 123 world") == "Hello 123 World"

def test_string_with_special_characters():
    """Test capitalization with special characters."""
    assert capitalize_words("hello! world@") == "Hello! World@"