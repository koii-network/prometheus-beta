import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    assert remove_duplicate_words("the quick brown fox jumps over the lazy dog") == "the quick brown fox jumps over lazy dog"

def test_remove_duplicate_words_consecutive_duplicates():
    assert remove_duplicate_words("hello hello world world") == "hello world"

def test_remove_duplicate_words_mixed_case():
    assert remove_duplicate_words("Hello hello HELLO world") == "Hello world"

def test_remove_duplicate_words_empty_string():
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_single_word():
    assert remove_duplicate_words("python") == "python"

def test_remove_duplicate_words_all_duplicates():
    assert remove_duplicate_words("cat cat cat cat") == "cat"

def test_remove_duplicate_words_invalid_input():
    with pytest.raises(TypeError):
        remove_duplicate_words(123)
    with pytest.raises(TypeError):
        remove_duplicate_words(None)