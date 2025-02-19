import pytest
from src.palindrome_substrings import find_shortest_palindromic_substrings

def test_find_shortest_palindromic_substrings():
    # Test empty string
    assert find_shortest_palindromic_substrings("") == []
    
    # Test single character string (always a palindrome)
    assert find_shortest_palindromic_substrings("a") == ["a"]
    
    # Test string with multiple shortest palindromes
    result = find_shortest_palindromic_substrings("abcba")
    assert set(result) == {"a", "b", "c"}
    
    # Test string with even-length shortest palindromes
    result = find_shortest_palindromic_substrings("abba")
    assert set(result) == {"bb", "aa"}
    
    # Test string with no palindromes longer than 1
    result = find_shortest_palindromic_substrings("abcd")
    assert set(result) == {"a", "b", "c", "d"}
    
    # Test string with multiple repeated palindromes
    result = find_shortest_palindromic_substrings("racecar")
    assert set(result) == {"r", "a", "c", "e"}
    
    # Test case sensitivity
    result = find_shortest_palindromic_substrings("AbBa")
    assert set(result) == {"A", "b", "B", "a"}

def test_function_returns_smallest_palindromes():
    # Ensure the function returns the smallest palindromes first
    result = find_shortest_palindromic_substrings("abcdefg")
    assert result == ["a", "b", "c", "d", "e", "f", "g"]
    
    result = find_shortest_palindromic_substrings("abcba")
    assert set(result) == {"a", "b", "c"}
    
    result = find_shortest_palindromic_substrings("abba")
    assert set(result) == {"bb", "aa"}