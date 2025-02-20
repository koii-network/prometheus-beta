import pytest
from src.reverse_word_chars import reverse_word_chars

def test_basic_sentence():
    assert reverse_word_chars("hello world") == "olleh dlrow"

def test_multiple_words():
    assert reverse_word_chars("Python is awesome") == "nohtyP si emosewa"

def test_single_word():
    assert reverse_word_chars("programming") == "gnimmargorp"

def test_empty_string():
    assert reverse_word_chars("") == ""

def test_single_character_words():
    assert reverse_word_chars("a b c") == "a b c"

def test_mixed_case():
    assert reverse_word_chars("Hello World") == "olleH dlroW"

def test_input_type_error():
    with pytest.raises(TypeError):
        reverse_word_chars(123)
    with pytest.raises(TypeError):
        reverse_word_chars(None)