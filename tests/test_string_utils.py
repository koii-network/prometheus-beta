import pytest
from src.string_utils import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic duplicate word removal."""
    assert remove_duplicate_words("hello world hello") == "hello world"
    assert remove_duplicate_words("the quick brown fox quick brown") == "the quick brown fox"

def test_remove_duplicate_words_empty_string():
    """Test behavior with empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_words("unique words only") == "unique words only"

def test_remove_duplicate_words_multiple_duplicates():
    """Test removing multiple duplicate words."""
    assert remove_duplicate_words("a b c a d b e") == "a b c d e"

def test_remove_duplicate_words_case_sensitive():
    """Test that word removal is case-sensitive."""
    assert remove_duplicate_words("Hello hello HELLO") == "Hello hello HELLO"