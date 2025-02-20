import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_standard_string():
    """Test reversing a standard string."""
    chars = ['h', 'e', 'l', 'l', 'o']
    reverse_string_in_place(chars)
    assert chars == ['o', 'l', 'l', 'e', 'h']

def test_reverse_single_character():
    """Test reversing a single character list."""
    chars = ['a']
    reverse_string_in_place(chars)
    assert chars == ['a']

def test_reverse_empty_list():
    """Test reversing an empty list."""
    chars = []
    reverse_string_in_place(chars)
    assert chars == []

def test_reverse_even_length_string():
    """Test reversing a string with even number of characters."""
    chars = ['a', 'b', 'c', 'd']
    reverse_string_in_place(chars)
    assert chars == ['d', 'c', 'b', 'a']

def test_reverse_with_different_characters():
    """Test reversing a list with various character types."""
    chars = ['1', '2', '3', '!', '@']
    reverse_string_in_place(chars)
    assert chars == ['@', '!', '3', '2', '1']