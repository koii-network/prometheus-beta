import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic functionality of removing duplicate characters."""
    assert remove_duplicate_chars('hello') == 'helo'
    assert remove_duplicate_chars('aabbccdd') == 'abcd'
    assert remove_duplicate_chars('abcdefg') == 'abcdefg'

def test_remove_duplicate_chars_empty_string():
    """Test behavior with an empty string."""
    assert remove_duplicate_chars('') == ''

def test_remove_duplicate_chars_single_char():
    """Test behavior with a single character."""
    assert remove_duplicate_chars('a') == 'a'

def test_remove_duplicate_chars_invalid_input():
    """Test that the function raises an error for non-lowercase input."""
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars('Hello')
    
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars('hello123')
    
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars('hello!')