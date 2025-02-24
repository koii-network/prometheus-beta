import pytest
from src.string_reversal import recursive_reverse_string

def test_empty_string():
    """Test reversing an empty string."""
    assert recursive_reverse_string("") == ""

def test_single_character():
    """Test reversing a single character."""
    assert recursive_reverse_string("a") == "a"

def test_simple_string():
    """Test reversing a simple string."""
    assert recursive_reverse_string("hello") == "olleh"

def test_string_with_spaces():
    """Test reversing a string with spaces."""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_mixed_case():
    """Test reversing a string with mixed case."""
    assert recursive_reverse_string("HeLLo") == "oLLeH"

def test_invalid_characters():
    """Test that an error is raised for invalid characters."""
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_reverse_string("hello123")
    
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_reverse_string("hello!")

def test_multiple_words():
    """Test reversing multiple words."""
    assert recursive_reverse_string("Python is awesome") == "emosewa si nohtyP"