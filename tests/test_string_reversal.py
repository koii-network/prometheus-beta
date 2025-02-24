import pytest
from src.string_reversal import recursive_reverse_string

def test_recursive_reverse_string_empty():
    """Test reversing an empty string"""
    assert recursive_reverse_string("") == ""

def test_recursive_reverse_string_single_char():
    """Test reversing a single character"""
    assert recursive_reverse_string("a") == "a"

def test_recursive_reverse_string_basic():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"

def test_recursive_reverse_string_with_spaces():
    """Test string reversal with spaces"""
    assert recursive_reverse_string("hello world") == "dlrow olleh"

def test_recursive_reverse_string_mixed_case():
    """Test string reversal with mixed case"""
    assert recursive_reverse_string("HeLLo WoRLD") == "DLRoW oLLeH"

def test_recursive_reverse_string_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(TypeError):
        recursive_reverse_string(123)
    
    with pytest.raises(TypeError):
        recursive_reverse_string(None)