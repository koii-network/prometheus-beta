import pytest
from src.remove_duplicates import remove_duplicate_words

def test_remove_duplicate_words_basic():
    assert remove_duplicate_words("hello world hello python world") == "hello world python"

def test_remove_duplicate_words_no_duplicates():
    assert remove_duplicate_words("the quick brown fox") == "the quick brown fox"

def test_remove_duplicate_words_all_duplicates():
    assert remove_duplicate_words("a a a a a") == "a"

def test_remove_duplicate_words_empty_string():
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_single_word():
    assert remove_duplicate_words("python") == "python"

def test_remove_duplicate_words_invalid_input():
    with pytest.raises(TypeError):
        remove_duplicate_words(123)
    with pytest.raises(TypeError):
        remove_duplicate_words(None)