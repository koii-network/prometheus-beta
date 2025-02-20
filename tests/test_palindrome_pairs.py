import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert [0, 1] in result or [1, 0] in result, "Should find palindrome pair 'bat' and 'tab'"

def test_empty_input():
    """Test with an empty input list."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == [], "Should return an empty list for empty input"

def test_single_word():
    """Test with a single word input."""
    words = ["abc"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should return an empty list for single word input"

def test_multiple_palindrome_pairs():
    """Test finding multiple palindrome pairs."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected_pairs = [[0, 1], [1, 0], [2, 4], [4, 2]]
    
    # Check that each expected pair is in the result
    for pair in expected_pairs:
        assert pair in result, f"Should find palindrome pair at indices {pair}"

def test_no_palindrome_pairs():
    """Test with words that have no palindrome pairs."""
    words = ["hello", "world", "python"]
    result = find_palindrome_pairs(words)
    assert result == [], "Should return an empty list when no palindrome pairs exist"