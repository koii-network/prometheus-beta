import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_string_normal():
    """Test reversal of a normal string"""
    assert reverse_string_in_place("hello") == "olleh"

def test_reverse_string_empty():
    """Test reversal of an empty string"""
    assert reverse_string_in_place("") == ""

def test_reverse_string_single_char():
    """Test reversal of a single character"""
    assert reverse_string_in_place("a") == "a"

def test_reverse_string_palindrome():
    """Test reversal of a palindrome"""
    assert reverse_string_in_place("racecar") == "racecar"

def test_reverse_string_with_spaces():
    """Test reversal of a string with spaces"""
    assert reverse_string_in_place("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversal of a string with special characters"""
    assert reverse_string_in_place("a1b2c3") == "3c2b1a"

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError):
        reverse_string_in_place(123)
    
    with pytest.raises(TypeError):
        reverse_string_in_place(None)
    
    with pytest.raises(TypeError):
        reverse_string_in_place(["hello"])