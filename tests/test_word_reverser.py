import pytest
from src.word_reverser import reverse_words

def test_multiple_words():
    """Test reversing multiple words."""
    assert reverse_words("Hello World") == "World Hello"
    assert reverse_words("Python is awesome") == "awesome is Python"

def test_single_word():
    """Test single word input remains unchanged."""
    assert reverse_words("SingleWord") == "SingleWord"

def test_empty_string():
    """Test empty string returns empty string."""
    assert reverse_words("") == ""

def test_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert reverse_words("  Hello   World  ") == "World Hello"

def test_input_types():
    """Test input type validation."""
    with pytest.raises(AttributeError):
        reverse_words(None)
    with pytest.raises(AttributeError):
        reverse_words(123)