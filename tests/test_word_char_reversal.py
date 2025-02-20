import pytest
from src.word_char_reversal import reverse_words_and_chars

def test_reverse_words_and_chars_basic():
    assert reverse_words_and_chars("hello world") == "dlrow olleh"
    assert reverse_words_and_chars("python is awesome") == "emosewa si nohtyp"

def test_reverse_words_and_chars_single_word():
    assert reverse_words_and_chars("hello") == "olleh"

def test_reverse_words_and_chars_empty_string():
    assert reverse_words_and_chars("") == ""

def test_reverse_words_and_chars_multiple_spaces():
    assert reverse_words_and_chars("  hello   world  ") == "dlrow olleh"

def test_reverse_words_and_chars_invalid_input():
    with pytest.raises(TypeError):
        reverse_words_and_chars(123)
    with pytest.raises(TypeError):
        reverse_words_and_chars(None)