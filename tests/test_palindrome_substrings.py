import pytest
from src.palindrome_substrings import find_shortest_palindromic_substrings

def test_find_shortest_palindromic_substrings_basic():
    assert set(find_shortest_palindromic_substrings("abc")) == {"a", "b", "c"}
    
def test_find_shortest_palindromic_substrings_multiple_palindromes():
    result = set(find_shortest_palindromic_substrings("abba"))
    assert result == {"a", "b", "bb"}
    
def test_find_shortest_palindromic_substrings_empty_string():
    assert find_shortest_palindromic_substrings("") == []
    
def test_find_shortest_palindromic_substrings_repeated_chars():
    result = set(find_shortest_palindromic_substrings("aaa"))
    assert result == {"a", "aa"}
    
def test_find_shortest_palindromic_substrings_mixed_case():
    result = set(find_shortest_palindromic_substrings("AbcbA"))
    assert result == {"A", "b", "c"}
    
def test_find_shortest_palindromic_substrings_single_char():
    result = find_shortest_palindromic_substrings("hello")
    assert set(result) == {"h", "e", "l", "o"}
    
def test_find_shortest_palindromic_substrings_complex():
    result = find_shortest_palindromic_substrings("racecar")
    assert set(result) == {"r", "a", "c", "e"}