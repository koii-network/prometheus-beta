import pytest
from src.word_counter import count_words

def test_basic_word_count():
    assert count_words("Hello world") == 2
    assert count_words("One") == 1

def test_multiple_spaces():
    assert count_words("  Multiple   spaces   between words  ") == 4

def test_empty_string():
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_punctuation_and_numbers():
    assert count_words("Hello, world! 123") == 3

def test_unicode_and_special_characters():
    assert count_words("Привет мир") == 2  # Russian words
    assert count_words("Hello, café") == 2  # Accented characters

def test_edge_cases():
    assert count_words("\t\nSpaces\rand\ttabs") == 3  # Various whitespace characters