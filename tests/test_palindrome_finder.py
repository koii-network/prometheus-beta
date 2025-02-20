import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_find_palindromic_substrings():
    # Test case 1: Basic palindromes
    assert set(find_palindromic_substrings("abba")) == {"a", "b", "bb", "abba"}
    
    # Test case 2: Single character palindromes
    assert set(find_palindromic_substrings("abc")) == {"a", "b", "c"}
    
    # Test case 3: Multiple palindromes
    assert set(find_palindromic_substrings("racecar")) == {
        "r", "a", "c", "e", "racecar", "aceca", "cec"
    }
    
    # Test case 4: Empty string
    assert find_palindromic_substrings("") == []
    
    # Test case 5: No palindromes beyond single characters
    assert set(find_palindromic_substrings("xyz")) == {"x", "y", "z"}
    
    # Test case 6: Longer string with multiple palindromes
    result = set(find_palindromic_substrings("aabbaa"))
    expected = {"a", "b", "aa", "bb", "aabbaa", "abba"}
    assert result == expected