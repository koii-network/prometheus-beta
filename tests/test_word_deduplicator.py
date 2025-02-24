import pytest
from src.word_deduplicator import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic duplicate word removal."""
    assert remove_duplicate_words("hello world hello python world") == "hello world python"

def test_remove_duplicate_words_no_duplicates():
    """Test string with no duplicate words."""
    assert remove_duplicate_words("unique words only") == "unique words only"

def test_remove_duplicate_words_empty_string():
    """Test empty string input."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_single_word():
    """Test input with a single word."""
    assert remove_duplicate_words("hello") == "hello"

def test_remove_duplicate_words_all_duplicates():
    """Test input with all duplicate words."""
    assert remove_duplicate_words("hello hello hello") == "hello"

def test_remove_duplicate_words_mixed_case():
    """Test word removal is case-sensitive."""
    assert remove_duplicate_words("Hello hello HELLO") == "Hello hello HELLO"

def test_remove_duplicate_words_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        remove_duplicate_words(123)
    
    with pytest.raises(TypeError):
        remove_duplicate_words(None)