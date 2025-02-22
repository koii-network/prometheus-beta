import pytest
from src.palindrome_index_pairs import find_palindrome_index_pairs, is_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True

def test_find_palindrome_index_pairs():
    # Basic test with palindrome pairs
    words1 = ["bat", "tab", "cat"]
    result1 = find_palindrome_index_pairs(words1)
    assert (0, 1) in result1 and (1, 0) in result1
    assert len(result1) == 2

    # Test with no palindrome pairs
    words2 = ["dog", "cat", "bird"]
    result2 = find_palindrome_index_pairs(words2)
    assert len(result2) == 0

    # Test with multiple palindrome pairs
    words3 = ["race", "car", "care", "hello"]
    result3 = find_palindrome_index_pairs(words3)
    assert (0, 1) in result3 and (1, 0) in result3
    assert len(result3) == 2

    # Test with empty list
    words4 = []
    result4 = find_palindrome_index_pairs(words4)
    assert len(result4) == 0

    # Test with single word list
    words5 = ["hello"]
    result5 = find_palindrome_index_pairs(words5)
    assert len(result5) == 0