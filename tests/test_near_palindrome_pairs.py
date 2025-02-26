import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_near_palindrome_criteria():
    """Explore the near-palindrome definition."""
    # These are the exact test cases from the original task description
    assert find_near_palindrome_pairs(["racecar", "radar"]) == [["racecar", "radar"]]
    assert find_near_palindrome_pairs(["raccar", "radar", "hello", "wprld"]) == [["raccar", "radar"]]
    assert find_near_palindrome_pairs(["abcba", "abcde"]) == [["abcba", "abcde"]]

def test_empty_input():
    """Test with an empty input list."""
    assert find_near_palindrome_pairs([]) == []

def test_no_near_palindrome_pairs():
    """Test when no near palindrome pairs exist."""
    input_strings = ["hello", "world", "python"]
    assert find_near_palindrome_pairs(input_strings) == []

def test_single_character_strings():
    """Test with single character strings."""
    input_strings = ["a", "b", "c"]
    assert find_near_palindrome_pairs(input_strings) == []

def test_multiple_pairs():
    """Test finding multiple near-palindrome pairs."""
    input_strings = ["raccar", "racecar", "radar", "hello", "wprld"]
    result = find_near_palindrome_pairs(input_strings)
    assert len(result) == 2
    assert ["raccar", "racecar"] in result
    assert ["raccar", "radar"] in result