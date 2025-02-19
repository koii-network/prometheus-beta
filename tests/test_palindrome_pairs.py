import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    pairs = find_palindrome_pairs(words)
    assert (0, 1) in pairs  # "abcd" + "dcba" is a palindrome
    assert (1, 0) in pairs  # "dcba" + "abcd" is a palindrome

def test_empty_input():
    assert find_palindrome_pairs([]) == []

def test_single_word():
    words = ["radar"]
    assert find_palindrome_pairs(words) == []

def test_multiple_palindrome_pairs():
    words = ["bat", "tab", "cat"]
    pairs = find_palindrome_pairs(words)
    assert (0, 1) in pairs
    assert (1, 0) in pairs

def test_no_palindrome_pairs():
    words = ["hello", "world", "python"]
    assert find_palindrome_pairs(words) == []

def test_repeated_words():
    words = ["a", "a"]
    pairs = find_palindrome_pairs(words)
    assert len(pairs) == 0  # No self-pairing

def test_complex_palindrome_pairs():
    words = ["abc", "cba", "bac"]
    pairs = find_palindrome_pairs(words)
    assert (0, 1) in pairs
    assert (1, 0) in pairs
    assert (2, 1) in pairs
    assert (1, 2) in pairs