import pytest
from src.palindrome_utils import find_palindromic_substrings

def test_find_palindromic_substrings():
    # Basic test cases
    assert set(find_palindromic_substrings("abc")) == {"a", "b", "c"}
    assert set(find_palindromic_substrings("racecar")) == {"r", "a", "c", "e", "racecar", "aceca", "cec"}
    
    # Empty string
    assert find_palindromic_substrings("") == []
    
    # All characters unique
    assert set(find_palindromic_substrings("abcd")) == {"a", "b", "c", "d"}
    
    # Multiple character palindromes
    assert set(find_palindromic_substrings("aaa")) == {"a", "aa", "aaa"}
    
    # Mixed case palindromes
    assert set(find_palindromic_substrings("Abba")) == {"A", "b", "B", "a", "bb", "Abba"}
    
    # Long palindrome
    assert "abcba" in find_palindromic_substrings("abcbaxyz")

def test_find_palindromic_substrings_error_handling():
    # Test non-string input
    with pytest.raises(TypeError):
        find_palindromic_substrings(123)
    
    with pytest.raises(TypeError):
        find_palindromic_substrings(None)