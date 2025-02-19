import pytest
from src.most_frequent_word import most_frequent_word

def test_most_frequent_word_basic():
    """Test basic functionality of finding the most frequent word."""
    assert most_frequent_word("cat dog cat bird") == "cat"

def test_most_frequent_word_single_word():
    """Test when there's only one word in the input."""
    assert most_frequent_word("hello") == "hello"

def test_most_frequent_word_empty_string():
    """Test behavior with an empty string."""
    assert most_frequent_word("") == ""

def test_most_frequent_word_tie_scenario():
    """Test when multiple words have the same frequency."""
    result = most_frequent_word("apple banana apple banana")
    assert result in ["apple", "banana"]

def test_most_frequent_word_all_unique():
    """Test scenario where all words occur once."""
    result = most_frequent_word("a b c d")
    assert result in ["a", "b", "c", "d"]