import pytest
from src.word_occurrence_finder import find_word_occurrences

def test_basic_occurrence():
    result = find_word_occurrences("hello world hello", "hello")
    assert result == [(0, "hello"), (12, "hello")]

def test_single_occurrence():
    result = find_word_occurrences("python is awesome", "awesome")
    assert result == [(12, "awesome")]

def test_no_occurrences():
    result = find_word_occurrences("python is great", "java")
    assert result == []

def test_empty_string():
    result = find_word_occurrences("", "word")
    assert result == []

def test_empty_target():
    result = find_word_occurrences("hello world", "")
    assert result == []

def test_type_error():
    with pytest.raises(TypeError):
        find_word_occurrences(123, "word")
    
    with pytest.raises(TypeError):
        find_word_occurrences("hello", 123)

def test_complex_string():
    result = find_word_occurrences("the quick brown fox jumps over the lazy fox", "fox")
    assert result == [(16, "fox"), (40, "fox")]

def test_case_sensitive():
    result = find_word_occurrences("Fox fox FOX", "fox")
    assert result == [(4, "fox")]