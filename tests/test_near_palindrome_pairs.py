import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs, is_palindrome, is_near_palindrome

def test_is_palindrome():
    """Test palindrome detection."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_is_near_palindrome():
    """Test near-palindrome detection."""
    assert is_near_palindrome("racecax") == True  # one char from "racecar"
    assert is_near_palindrome("hello") == False
    assert is_near_palindrome("abcda") == True   # "abcda" can become "abcba"
    assert is_near_palindrome("racecar") == False  # exact palindrome is not "near"

def test_find_near_palindrome_pairs():
    """Test finding near-palindrome pairs."""
    # Basic scenario
    result = find_near_palindrome_pairs(["racecax", "abcda", "hello", "world"])
    assert len(result) == 2
    assert ["racecax", "abcda"] in result or ["abcda", "racecax"] in result

def test_find_near_palindrome_pairs_edge_cases():
    """Test edge cases for near-palindrome pairs."""
    # Empty list
    assert find_near_palindrome_pairs([]) == []
    
    # Single element
    assert find_near_palindrome_pairs(["hello"]) == []

def test_find_near_palindrome_pairs_invalid_input():
    """Test invalid input handling."""
    # Non-list input
    with pytest.raises(TypeError):
        find_near_palindrome_pairs("not a list")
    
    # List with non-string elements
    with pytest.raises(ValueError):
        find_near_palindrome_pairs(["hello", 123, "world"])