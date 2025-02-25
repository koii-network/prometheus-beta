import pytest
from src.most_frequent_word import most_frequent_word

def test_basic_case():
    """Test finding the most frequent word in a simple string."""
    assert most_frequent_word("the cat is in the hat") == "the"

def test_single_word():
    """Test a string with a single word."""
    assert most_frequent_word("hello") == "hello"

def test_multiple_max_frequency():
    """Test when multiple words have the same highest frequency."""
    result = most_frequent_word("cat dog cat dog")
    assert result in ["cat", "dog"]

def test_empty_string():
    """Test behavior with an empty string."""
    assert most_frequent_word("") == ""

def test_all_unique_words():
    """Test a string where all words appear once."""
    result = most_frequent_word("quick brown fox")
    assert result in ["quick", "brown", "fox"]