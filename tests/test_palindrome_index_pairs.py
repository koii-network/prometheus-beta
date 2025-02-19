import pytest
from src.palindrome_index_pairs import find_palindrome_index_pairs

def test_find_palindrome_index_pairs():
    # Test basic palindrome pairs
    words1 = ["abc", "cba", "def", "fed"]
    assert set(find_palindrome_index_pairs(words1)) == {(0, 1), (2, 3)}

    # Test no palindrome pairs
    words2 = ["hello", "world", "foo", "bar"]
    assert find_palindrome_index_pairs(words2) == []

    # Test empty list
    words3 = []
    assert find_palindrome_index_pairs(words3) == []

    # Test mixed case and single-character palindromes
    words4 = ["racecar", "racecar", "level", "travel"]
    assert set(find_palindrome_index_pairs(words4)) == {(0, 1)}

    # Test duplicate palindrome pairs
    words5 = ["abc", "cba", "abc", "cba"]
    assert set(find_palindrome_index_pairs(words5)) == {(0, 1), (0, 3), (1, 2), (2, 3)}