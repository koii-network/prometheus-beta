import pytest
from src.string_utils import reverse_words

def test_basic_reverse_words():
    """Test basic word reversal."""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_words():
    """Test reversing sentences with multiple words."""
    assert reverse_words("Python is awesome") == "awesome is Python"

def test_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert reverse_words("Hello    World  Python") == "Python World Hello"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words("") == ""

def test_single_word():
    """Test single word input."""
    assert reverse_words("Hello") == "Hello"

def test_none_input():
    """Test handling of None input."""
    assert reverse_words(None) == ""

def test_whitespace_only():
    """Test input with only whitespace."""
    assert reverse_words("   ") == ""

def test_mixed_case():
    """Test mixed case word reversal."""
    assert reverse_words("Hello WORLD Python") == "Python WORLD Hello"