import pytest
from src.near_palindrome import find_near_palindrome_pairs

def test_near_palindrome_pairs_basic():
    # Test basic near-palindrome pairs
    input_strings = ["racecar", "abcda", "hello", "radar"]
    result = find_near_palindrome_pairs(input_strings)
    
    # Expect pairs that include near-palindromes
    assert len(result) > 0
    for pair in result:
        assert len(pair) == 2
        assert pair[0] in input_strings
        assert pair[1] in input_strings

def test_near_palindrome_pairs_edge_cases():
    # Test edge cases
    test_cases = [
        [],  # Empty list
        ["a"],  # Single element
        ["abc", "def", "ghi"]  # No near palindromes
    ]
    
    for case in test_cases:
        result = find_near_palindrome_pairs(case)
        assert len(result) == 0

def test_specific_near_palindrome_pairs():
    # Test specific known near-palindrome cases
    input_strings = ["abcda", "abxda", "hello", "hallo"]
    result = find_near_palindrome_pairs(input_strings)
    
    expected_pairs = [
        ["abcda", "abxda"]
    ]
    
    # Check that expected pairs are in the result
    for pair in expected_pairs:
        assert pair in result or pair[::-1] in result

def test_palindrome_exclusion():
    # Ensure true palindromes are not considered near-palindromes
    input_strings = ["racecar", "radar", "level", "abcda"]
    result = find_near_palindrome_pairs(input_strings)
    
    # Palindromes should not be part of near-palindrome pairs
    for pair in result:
        assert not (pair[0] == pair[0][::-1] and pair[1] == pair[1][::-1])