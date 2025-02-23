import pytest
from src.string_reversal import recursive_reverse_string

def test_recursive_reverse_string_basic():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"

def test_recursive_reverse_string_with_spaces():
    """Test string reversal with spaces"""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_recursive_reverse_string_mixed_case():
    """Test string reversal with mixed case"""
    assert recursive_reverse_string("Hello World") == "dlroW olleH"

def test_recursive_reverse_string_single_char():
    """Test single character string"""
    assert recursive_reverse_string("a") == "a"

def test_recursive_reverse_string_empty():
    """Test empty string"""
    assert recursive_reverse_string("") == ""

def test_recursive_reverse_string_invalid_input():
    """Test that invalid characters raise a ValueError"""
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_reverse_string("hello123")
    
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_reverse_string("hello!")