import pytest
from src.word_counter import count_words

def test_count_words_normal_case():
    assert count_words("Hello world") == 2
    assert count_words("This is a test sentence") == 5

def test_count_words_multiple_spaces():
    assert count_words("Hello   world  with    multiple    spaces") == 5

def test_count_words_empty_string():
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_count_words_single_word():
    assert count_words("Hello") == 1

def test_count_words_with_punctuation():
    assert count_words("Hello, world! How are you?") == 5

def test_count_words_with_numbers():
    assert count_words("There are 123 words in this 456 string") == 8