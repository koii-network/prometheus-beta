import pytest
from src.capitalize_words import capitalize_comma_words

def test_basic_capitalization():
    """Test basic word capitalization."""
    assert capitalize_comma_words("hello,world") == "Hello,World"

def test_already_capitalized():
    """Test when words are already capitalized."""
    assert capitalize_comma_words("Hello,World") == "Hello,World"

def test_multiple_words():
    """Test capitalization with multiple words."""
    assert capitalize_comma_words("python,is,awesome") == "Python,Is,Awesome"

def test_single_word():
    """Test capitalization of a single word."""
    assert capitalize_comma_words("python") == "Python"

def test_invalid_input_with_whitespace():
    """Test that whitespace raises a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello, world")

def test_invalid_input_with_numbers():
    """Test that numbers raise a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello123,world")

def test_invalid_input_with_punctuation():
    """Test that punctuation raises a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello!,world")

def test_empty_string():
    """Test handling of an empty string."""
    assert capitalize_comma_words("") == ""