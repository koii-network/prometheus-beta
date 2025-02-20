import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    # Basic case of removing duplicates
    assert remove_duplicate_words("the quick brown fox jumps the quick fox") == "the quick brown fox jumps"

def test_remove_duplicate_words_no_duplicates():
    # Case with no duplicates
    assert remove_duplicate_words("hello world programming") == "hello world programming"

def test_remove_duplicate_words_all_duplicates():
    # Case where all words are duplicates
    assert remove_duplicate_words("apple apple apple") == "apple"

def test_remove_duplicate_words_mixed_case():
    # Case with mixed case (case-sensitive comparison)
    assert remove_duplicate_words("hello Hello HELLO") == "hello Hello HELLO"

def test_remove_duplicate_words_empty_string():
    # Empty string case
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_single_word():
    # Single word case
    assert remove_duplicate_words("python") == "python"

def test_remove_duplicate_words_invalid_input():
    # Invalid input type
    with pytest.raises(TypeError):
        remove_duplicate_words(123)
    with pytest.raises(TypeError):
        remove_duplicate_words(None)