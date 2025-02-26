import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_basic_near_palindrome_pairs():
    """Test finding near palindrome pairs in a simple list."""
    input_strings = ["racecar", "radar", "hello", "world"]
    result = find_near_palindrome_pairs(input_strings)
    assert result == [["racecar", "radar"]]

def test_empty_input():
    """Test with an empty input list."""
    assert find_near_palindrome_pairs([]) == []

def test_no_near_palindrome_pairs():
    """Test when no near palindrome pairs exist."""
    input_strings = ["hello", "world", "python"]
    assert find_near_palindrome_pairs(input_strings) == []

def test_multiple_near_palindrome_pairs():
    """Test finding multiple near palindrome pairs."""
    input_strings = ["raccar", "radar", "hello", "wprld"]
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) == 2
    assert ["raccar", "radar"] in result
    assert ["hello", "wprld"] in result

def test_single_character_strings():
    """Test with single character strings."""
    input_strings = ["a", "b", "c"]
    assert find_near_palindrome_pairs(input_strings) == []

def test_near_palindrome_with_repeated_characters():
    """Test near palindromes with repeated characters."""
    input_strings = ["abcba", "abcde"]
    result = find_near_palindrome_pairs(input_strings)
    assert result == [["abcba", "abcde"]]