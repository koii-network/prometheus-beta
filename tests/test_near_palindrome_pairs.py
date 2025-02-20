import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_find_near_palindrome_pairs_basic():
    # Test case with near-palindrome pairs
    input_strings = ["abcda", "racecar", "abcde", "abcba"]
    expected = [["abcda", "abcde"]]
    assert find_near_palindrome_pairs(input_strings) == expected

def test_find_near_palindrome_pairs_empty():
    # Test with empty input
    assert find_near_palindrome_pairs([]) == []

def test_find_near_palindrome_pairs_no_pairs():
    # Test with no near-palindrome pairs
    input_strings = ["hello", "world", "python"]
    assert find_near_palindrome_pairs(input_strings) == []

def test_find_near_palindrome_pairs_multiple_pairs():
    # Test case with multiple near-palindrome pairs
    input_strings = ["abcda", "abcde", "bcdab", "bcdef"]
    expected = [["abcda", "abcde"], ["bcdab", "bcdef"]]
    result = find_near_palindrome_pairs(input_strings)
    assert sorted(result) == sorted(expected)

def test_find_near_palindrome_pairs_palindrome_excluded():
    # Test that actual palindromes are not considered near-palindromes
    input_strings = ["racecar", "abcda", "abcde"]
    expected = [["abcda", "abcde"]]
    assert find_near_palindrome_pairs(input_strings) == expected

def test_find_near_palindrome_pairs_case_sensitive():
    # Test case sensitivity
    input_strings = ["Abcda", "abcda"]
    assert find_near_palindrome_pairs(input_strings) == []