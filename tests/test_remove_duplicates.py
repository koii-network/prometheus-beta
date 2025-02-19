import pytest
from src.remove_duplicates import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    assert remove_duplicate_words("hello world hello python world") == "hello world python"

def test_remove_duplicate_words_no_duplicates():
    """Test a string with no duplicate words."""
    assert remove_duplicate_words("the quick brown fox") == "the quick brown fox"

def test_remove_duplicate_words_all_duplicates():
    """Test a string where all words are duplicates."""
    assert remove_duplicate_words("hello hello hello") == "hello"

def test_remove_duplicate_words_empty_string():
    """Test an empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_case_sensitive():
    """Test that the function is case-sensitive."""
    assert remove_duplicate_words("Hello hello HELLO") == "Hello hello HELLO"

def test_remove_duplicate_words_whitespace():
    """Test handling of multiple whitespaces."""
    assert remove_duplicate_words("  hello   world  hello  ") == "hello world"