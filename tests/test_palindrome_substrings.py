import pytest
from src.palindrome_substrings import find_shortest_palindromic_substrings

def test_find_shortest_palindromic_substrings():
    # Test case 1: Simple palindrome
    assert find_shortest_palindromic_substrings("babad") == ["b", "a", "d"]
    
    # Test case 2: Entire string is a palindrome
    assert find_shortest_palindromic_substrings("racecar") == ["r"]
    
    # Test case 3: Multiple single-character palindromes
    assert find_shortest_palindromic_substrings("abcde") == ["a", "b", "c", "d", "e"]
    
    # Test case 4: Empty string
    assert find_shortest_palindromic_substrings("") == []
    
    # Test case 5: Repeated characters
    assert find_shortest_palindromic_substrings("aaa") == ["a"]
    
    # Test case 6: Mixed case string
    assert find_shortest_palindromic_substrings("AbcBa") == ["A", "b", "c", "B", "a"]
    
    # Test case 7: String with special characters
    assert find_shortest_palindromic_substrings("a!b@c#") == ["a", "!", "b", "@", "c", "#"]

def test_edge_cases():
    # Test None input
    assert find_shortest_palindromic_substrings(None) == []
    
    # Test single character
    assert find_shortest_palindromic_substrings("x") == ["x"]