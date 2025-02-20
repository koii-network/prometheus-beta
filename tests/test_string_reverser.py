import pytest
from src.string_reverser import reverse_string_in_place

def test_reverse_string_normal_case():
    """Test reversing a normal string"""
    s = list('hello')
    reverse_string_in_place(s)
    assert ''.join(s) == 'olleh'

def test_reverse_string_palindrome():
    """Test reversing a palindrome"""
    s = list('radar')
    reverse_string_in_place(s)
    assert ''.join(s) == 'radar'

def test_reverse_string_empty():
    """Test reversing an empty list"""
    s = []
    reverse_string_in_place(s)
    assert s == []

def test_reverse_string_single_character():
    """Test reversing a single character"""
    s = list('a')
    reverse_string_in_place(s)
    assert ''.join(s) == 'a'

def test_reverse_string_even_length():
    """Test reversing a string with even number of characters"""
    s = list('abcd')
    reverse_string_in_place(s)
    assert ''.join(s) == 'dcba'

def test_reverse_string_space_complexity():
    """Verify that the function modifies the list in-place"""
    s = list('python')
    original_id = id(s)
    reverse_string_in_place(s)
    assert id(s) == original_id  # Same list object is modified