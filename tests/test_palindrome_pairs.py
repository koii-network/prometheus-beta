import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    # Test case with simple palindrome pairs
    words = ["bat", "tab", "cat"]
    expected = [(0, 1), (1, 0)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_empty_list():
    # Test with an empty list
    words = []
    assert find_palindrome_pairs(words) == []

def test_single_word():
    # Test with a single word
    words = ["hello"]
    assert find_palindrome_pairs(words) == []

def test_complex_palindrome_pairs():
    # Test with more complex palindrome combinations
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [(0, 1), (1, 0), (2, 4), (3, 2)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_no_palindrome_pairs():
    # Test with no palindrome pairs
    words = ["abc", "def", "ghi"]
    assert find_palindrome_pairs(words) == []

def test_repeated_words():
    # Test with repeated words
    words = ["a", "a"]
    expected = [(0, 1), (1, 0)]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_large_input():
    # Test with a larger input
    words = ["a", "b", "c", "ab", "ac", "aa"]
    # Generate expected pairs based on concatenation
    expected = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and (words[i] + words[j]) == (words[i] + words[j])[::-1]:
                expected.append((i, j))
    
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)