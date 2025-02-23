import pytest
from src.unique_sorted_chars import get_unique_sorted_chars

def test_get_unique_sorted_chars():
    # Test normal string with mixed case
    assert get_unique_sorted_chars("hello") == ['e', 'h', 'l', 'o']
    
    # Test string with mixed case preserving case sensitivity
    assert get_unique_sorted_chars("Python") == ['P', 'h', 'n', 'o', 't', 'y']
    
    # Test empty string
    assert get_unique_sorted_chars("") == []
    
    # Test string with repeated characters
    assert get_unique_sorted_chars("banana") == ['a', 'b', 'n']
    
    # Test string with special characters and numbers
    assert get_unique_sorted_chars("Hello, World! 123") == [' ', '!', ',', '1', '2', '3', 'H', 'W', 'd', 'e', 'l', 'o', 'r']

def test_get_unique_sorted_chars_types():
    # Test with non-string input raises TypeError
    with pytest.raises(TypeError):
        get_unique_sorted_chars(123)
    
    with pytest.raises(TypeError):
        get_unique_sorted_chars(None)