import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pairs scenario."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert (0, 1) in result  # "bat" + "tab" is a palindrome
    assert (1, 0) in result  # "tab" + "bat" is a palindrome
    assert len(result) == 2

def test_empty_list():
    """Test with an empty list."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word_list():
    """Test with a single word list."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_complex_palindrome_pairs():
    """Test more complex palindrome pair scenarios."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected_pairs = [(0, 1), (1, 0), (2, 4), (4, 2)]
    
    for pair in expected_pairs:
        assert pair in result

def test_no_palindrome_pairs():
    """Test when no palindrome pairs exist."""
    words = ["dog", "cat", "mouse"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_self_palindrome_exclusion():
    """Ensure a word is not paired with itself."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []