import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert (0, 1) in result and (1, 0) in result
    assert len(result) == 2

def test_empty_list():
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_no_palindrome_pairs():
    words = ["hello", "world", "python"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_same_word_prevention():
    words = ["hello", "hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_char_words():
    words = ["a", "b", "c"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_multiple_palindrome_pairs():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected_pairs = [(0, 1), (1, 0), (2, 4)]
    for pair in expected_pairs:
        assert pair in result