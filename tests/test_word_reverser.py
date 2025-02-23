import pytest
from src.word_reverser import reverse_words

def test_reverse_words_basic():
    assert reverse_words("Hello World") == "World Hello"

def test_reverse_words_multiple_spaces():
    assert reverse_words("Hello   World   Python") == "Python World Hello"

def test_reverse_words_leading_trailing_spaces():
    assert reverse_words("  Hello World  ") == "World Hello"

def test_reverse_words_single_word():
    assert reverse_words("Hello") == "Hello"

def test_reverse_words_empty_string():
    assert reverse_words("") == ""

def test_reverse_words_with_punctuation():
    assert reverse_words("Hello, World! Python.") == "Python. World! Hello,"