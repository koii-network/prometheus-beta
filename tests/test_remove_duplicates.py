import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic duplicate removal."""
    assert remove_duplicate_chars('hello') == 'helo'
    assert remove_duplicate_chars('aabbcc') == 'abc'
    assert remove_duplicate_chars('abcde') == 'abcde'

def test_remove_duplicate_chars_empty_string():
    """Test handling of empty string."""
    assert remove_duplicate_chars('') == ''

def test_remove_duplicate_chars_single_char():
    """Test handling of single character string."""
    assert remove_duplicate_chars('a') == 'a'

def test_remove_duplicate_chars_preserve_order():
    """Test that the order of first occurrence is preserved."""
    assert remove_duplicate_chars('cabbage') == 'cabge'

def test_remove_duplicate_chars_invalid_input():
    """Test that uppercase or mixed case input raises an error."""
    with pytest.raises(ValueError, match="Input string must contain only lowercase characters"):
        remove_duplicate_chars('Hello')
    
    with pytest.raises(ValueError, match="Input string must contain only lowercase characters"):
        remove_duplicate_chars('aBc')