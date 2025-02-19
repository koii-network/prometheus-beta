import pytest
from src.most_frequent_word import most_frequent_word

def test_most_frequent_word_basic():
    """Test basic functionality of finding most frequent word."""
    assert most_frequent_word("cat dog cat bird") == "cat"

def test_most_frequent_word_single_word():
    """Test when there's only one word."""
    assert most_frequent_word("hello") == "hello"

def test_most_frequent_word_all_unique():
    """Test when all words appear once."""
    result = most_frequent_word("apple banana cherry")
    assert result in ["apple", "banana", "cherry"]

def test_most_frequent_word_empty_string():
    """Test empty string input."""
    assert most_frequent_word("") is None

def test_most_frequent_word_multiple_max_freq():
    """Test when multiple words have the same max frequency."""
    result = most_frequent_word("cat dog cat dog")
    assert result in ["cat", "dog"]