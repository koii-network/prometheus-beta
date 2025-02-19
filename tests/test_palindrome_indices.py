import pytest
from src.palindrome_indices import find_palindrome_reverse_indices

def test_find_palindrome_reverse_indices_basic():
    words = ["cat", "tac", "dog", "god"]
    assert find_palindrome_reverse_indices(words) == [(0, 1), (2, 3)]

def test_find_palindrome_reverse_indices_no_matches():
    words = ["hello", "world", "test"]
    assert find_palindrome_reverse_indices(words) == []

def test_find_palindrome_reverse_indices_multiple_matches():
    words = ["race", "ecar", "code", "edoc", "same"]
    assert set(find_palindrome_reverse_indices(words)) == {(0, 1), (2, 3)}

def test_find_palindrome_reverse_indices_empty_list():
    words = []
    assert find_palindrome_reverse_indices(words) == []

def test_find_palindrome_reverse_indices_single_word():
    words = ["hello"]
    assert find_palindrome_reverse_indices(words) == []

def test_find_palindrome_reverse_indices_case_sensitive():
    words = ["Cat", "cat"]
    assert find_palindrome_reverse_indices(words) == []