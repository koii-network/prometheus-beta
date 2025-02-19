import pytest
from src.palindrome_index_pairs import find_palindrome_index_pairs

def test_basic_palindrome_pairs():
    words = ["bat", "tab", "cat"]
    expected = [(0, 1), (1, 0)]
    assert sorted(find_palindrome_index_pairs(words)) == sorted(expected)

def test_empty_list():
    words = []
    assert find_palindrome_index_pairs(words) == []

def test_no_palindrome_pairs():
    words = ["hello", "world", "python"]
    assert find_palindrome_index_pairs(words) == []

def test_multiple_palindrome_pairs():
    words = ["abc", "cba", "def", "fed"]
    expected = [(0, 1), (1, 0), (2, 3), (3, 2)]
    assert sorted(find_palindrome_index_pairs(words)) == sorted(expected)

def test_single_word_list():
    words = ["radar"]
    assert find_palindrome_index_pairs(words) == []

def test_case_sensitive():
    words = ["Bat", "tab"]
    assert find_palindrome_index_pairs(words) == []