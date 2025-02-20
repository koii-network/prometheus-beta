import pytest
from src.word_occurrences import find_word_occurrences

def test_find_word_occurrences_basic():
    text = "hello world hello there hello"
    target_word = "hello"
    expected = [(0, "hello"), (12, "hello"), (25, "hello")]
    assert find_word_occurrences(text, target_word) == expected

def test_find_word_occurrences_no_matches():
    text = "hello world python"
    target_word = "java"
    assert find_word_occurrences(text, target_word) == []

def test_find_word_occurrences_empty_inputs():
    assert find_word_occurrences("", "word") == []
    assert find_word_occurrences("hello world", "") == []

def test_find_word_occurrences_type_errors():
    with pytest.raises(TypeError):
        find_word_occurrences(123, "word")
    with pytest.raises(TypeError):
        find_word_occurrences("hello", 123)

def test_find_word_occurrences_single_occurrence():
    text = "unique words in this string"
    target_word = "words"
    expected = [(12, "words")]
    assert find_word_occurrences(text, target_word) == expected

def test_find_word_occurrences_case_sensitive():
    text = "Hello hello HELLO"
    target_word = "hello"
    expected = [(6, "hello")]
    assert find_word_occurrences(text, target_word) == expected