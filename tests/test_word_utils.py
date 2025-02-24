import pytest
from src.word_utils import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    assert remove_duplicate_words("hello world hello python world") == "hello world python"

def test_remove_duplicate_words_no_duplicates():
    """Test string with no duplicate words."""
    assert remove_duplicate_words("the quick brown fox") == "the quick brown fox"

def test_remove_duplicate_words_empty_string():
    """Test empty string input."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_all_duplicates():
    """Test string with all words being duplicates."""
    assert remove_duplicate_words("hello hello hello") == "hello"

def test_remove_duplicate_words_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(123)
        remove_duplicate_words(None)

def test_remove_duplicate_words_case_sensitive():
    """Test that word removal is case-sensitive."""
    assert remove_duplicate_words("Hello hello HELLO") == "Hello hello HELLO"

def test_remove_duplicate_words_complex():
    """Test a more complex scenario with multiple duplicates."""
    assert remove_duplicate_words("the cat and the dog and the bird") == "the cat and dog bird"