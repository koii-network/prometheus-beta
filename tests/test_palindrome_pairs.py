import pytest
from src.palindrome_pairs import find_close_palindrome_pairs

def test_find_close_palindrome_pairs():
    # Test case 1: Basic scenario with close palindrome pairs
    input_strings = ["racecar", "abcda", "xyzyx", "abcde"]
    result = find_close_palindrome_pairs(input_strings)
    # Expecting pairs where each string is close to being a palindrome
    assert len(result) > 0, "Should find close palindrome pairs"
    
    # Test case 2: No close palindrome pairs
    input_strings = ["hello", "world", "python"]
    result = find_close_palindrome_pairs(input_strings)
    assert len(result) == 0, "Should return empty list when no close pairs"
    
    # Test case 3: Mixed strings with some close palindrome pairs
    input_strings = ["raddar", "abcba", "coding", "helloeh"]
    result = find_close_palindrome_pairs(input_strings)
    assert len(result) > 0, "Should find close palindrome pairs"
    
    # Test case 4: Empty input list
    input_strings = []
    result = find_close_palindrome_pairs(input_strings)
    assert result == [], "Should handle empty input list"
    
    # Test case 5: Verify pair content
    input_strings = ["abcda", "xyzyx", "abcde"]
    result = find_close_palindrome_pairs(input_strings)
    for pair in result:
        assert len(pair) == 2, "Each result should be a pair of strings"

def test_close_to_palindrome_examples():
    # Test specific examples of strings close to palindromes
    test_cases = [
        ["abcda", "code"],  # can become "abcba" or "coded"
        ["radar", "hello"],  # "radar" is already a palindrome, others can be close
    ]
    
    for input_strings in test_cases:
        result = find_close_palindrome_pairs(input_strings)
        assert len(result) > 0, f"Should find close palindrome pairs in {input_strings}"

def test_edge_cases():
    # Test edge cases and boundary conditions
    test_cases = [
        ["a", "b", "c"],  # very short strings
        ["abcdefghijklmnop"],  # single string
        [""] # empty string
    ]
    
    for input_strings in test_cases:
        result = find_close_palindrome_pairs(input_strings)
        assert isinstance(result, list), "Should always return a list"