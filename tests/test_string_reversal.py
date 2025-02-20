import pytest
from src.string_reversal import recursive_reverse_string

def test_recursive_reverse_string_basic():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"
    assert recursive_reverse_string("world") == "dlrow"

def test_recursive_reverse_string_empty():
    """Test empty string reversal"""
    assert recursive_reverse_string("") == ""

def test_recursive_reverse_string_single_char():
    """Test single character string reversal"""
    assert recursive_reverse_string("a") == "a"

def test_recursive_reverse_string_with_spaces():
    """Test string reversal with spaces"""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_recursive_reverse_string_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        recursive_reverse_string(123)
    
    with pytest.raises(TypeError):
        recursive_reverse_string(None)
    
    with pytest.raises(TypeError):
        recursive_reverse_string(["list"])