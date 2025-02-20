import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_find_palindromic_substrings():
    # Test empty string
    assert find_palindromic_substrings("") == []
    
    # Test single character string
    assert find_palindromic_substrings("a") == ["a"]
    
    # Test string with no palindromes except single characters
    assert set(find_palindromic_substrings("abc")) == {"a", "b", "c"}
    
    # Test string with multiple palindromes
    result = find_palindromic_substrings("racecar")
    assert set(result) == {"r", "a", "c", "e", "racecar", "aceca", "cec"}
    
    # Test string with repeating characters
    result = find_palindromic_substrings("abbaab")
    assert set(result) == {"a", "b", "bb", "abba", "bba"}
    
    # Test case sensitivity and non-alphabetic characters
    result = find_palindromic_substrings("A man a plan a canal Panama")
    assert "A man a" in result
    assert "a man a" in result
    
    # Test longer string with complex palindromes
    result = find_palindromic_substrings("aabaa")
    assert set(result) == {"a", "aa", "aba", "aabaa"}

def test_unique_results():
    # Ensure no duplicate palindromes are returned
    result = find_palindromic_substrings("abbaab")
    assert len(result) == len(set(result))

def test_result_type():
    # Ensure result is a list
    result = find_palindromic_substrings("hello")
    assert isinstance(result, list)

def test_corner_cases():
    # Test very long repeated character string
    result = find_palindromic_substrings("aaaaaaa")
    assert len(result) > 0
    
    # Test string with special characters
    result = find_palindromic_substrings("a!!a")
    assert "a!!a" in result