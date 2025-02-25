import pytest
from src.word_utils import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic duplicate word removal."""
    assert remove_duplicate_words("hello hello world") == "hello world"

def test_remove_duplicate_words_multiple_duplicates():
    """Test removing multiple duplicate words."""
    assert remove_duplicate_words("the quick brown fox jumps the quick fox") == "the quick brown fox jumps"

def test_remove_duplicate_words_empty_string():
    """Test handling of empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_words("python is awesome") == "python is awesome"

def test_remove_duplicate_words_case_sensitive():
    """Test that word removal is case-sensitive."""
    assert remove_duplicate_words("Hello hello HELLO") == "Hello hello HELLO"

def test_remove_duplicate_words_single_word():
    """Test a single word with duplicates."""
    assert remove_duplicate_words("word word word") == "word"

def test_remove_duplicate_words_mixed_duplicates():
    """Test removing duplicates in a mixed scenario."""
    assert remove_duplicate_words("a b c a d b e") == "a b c d e"