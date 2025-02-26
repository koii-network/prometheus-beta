import pytest
from src.string_reversal import reverse_string

def test_reverse_string_normal():
    """Test reversing a normal string"""
    s = list('hello')
    reverse_string(s)
    assert s == ['o', 'l', 'l', 'e', 'h']

def test_reverse_string_empty():
    """Test reversing an empty list"""
    s = []
    reverse_string(s)
    assert s == []

def test_reverse_string_single_char():
    """Test reversing a single character"""
    s = ['a']
    reverse_string(s)
    assert s == ['a']

def test_reverse_string_even_length():
    """Test reversing a string with even number of characters"""
    s = list('abcd')
    reverse_string(s)
    assert s == ['d', 'c', 'b', 'a']

def test_reverse_string_palindrome():
    """Test reversing a palindrome"""
    s = list('racecar')
    reverse_string(s)
    assert s == list('racecar')

def test_invalid_input_type():
    """Test that an invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        reverse_string('not a list')

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces"""
    s = list('hello world')
    reverse_string(s)
    assert s == ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']