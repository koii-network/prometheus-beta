import pytest
from src.unique_chars import count_unique_characters

def test_unique_characters_normal_string():
    """Test counting unique characters in a normal string."""
    assert count_unique_characters('hello') == 4
    assert count_unique_characters('world') == 5

def test_unique_characters_case_sensitivity():
    """Test case-sensitive unique character counting."""
    assert count_unique_characters('Hello') == 4  # H, e, l, o
    assert count_unique_characters('hELLo') == 4  # h, E, L, o
    
def test_unique_characters_empty_input():
    """Test handling of empty strings and None."""
    assert count_unique_characters('') == 0
    assert count_unique_characters(None) == 0
    assert count_unique_characters('   ') == 0

def test_unique_characters_repeated_chars():
    """Test strings with repeated characters."""
    assert count_unique_characters('aabbcc') == 3
    assert count_unique_characters('AbCabc') == 5  # A, b, C, a, c

def test_unique_characters_special_chars():
    """Test strings with special characters and punctuation."""
    assert count_unique_characters('!@#$%^&*()') == 10
    assert count_unique_characters('hello, world!') == 10  # including comma and space