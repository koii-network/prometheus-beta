import pytest
from src.unique_sorted_chars import get_unique_sorted_chars

def test_unique_sorted_chars():
    # Test with a mixed-case string
    assert get_unique_sorted_chars("Hello, World!") == [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'o', 'r']
    
    # Test with only lowercase string
    assert get_unique_sorted_chars("abracadabra") == ['a', 'b', 'c', 'd', 'r']
    
    # Test with empty string
    assert get_unique_sorted_chars("") == []
    
    # Test with None input
    assert get_unique_sorted_chars(None) == []
    
    # Test with a string of all uppercase 
    assert get_unique_sorted_chars("PYTHON") == ['H', 'N', 'O', 'P', 'T', 'Y']
    
    # Test with a string containing numbers and symbols
    assert get_unique_sorted_chars("a1b2c3!@#") == ['!', '#', '@', '1', '2', '3', 'a', 'b', 'c']

def test_case_sensitivity():
    # Verify case-sensitive sorting
    result = get_unique_sorted_chars("aBcDeF")
    assert result == ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
    
    # Ensuring uppercase comes before lowercase in sorted order
    result = get_unique_sorted_chars("aA")
    assert result == ['A', 'a']