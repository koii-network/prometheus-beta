import pytest
from src.sentence_reverser import reverse_words_in_sentence

def test_reverse_words_in_sentence_basic():
    assert reverse_words_in_sentence("Hello World") == "olleH dlroW"
    assert reverse_words_in_sentence("Python is awesome") == "nohtyP si emosewa"

def test_reverse_words_in_sentence_empty():
    assert reverse_words_in_sentence("") == ""

def test_reverse_words_in_sentence_single_word():
    assert reverse_words_in_sentence("Hello") == "olleH"

def test_reverse_words_in_sentence_mixed_case():
    assert reverse_words_in_sentence("HeLLo WoRLd") == "oLLeH dlRoW"

def test_reverse_words_in_sentence_with_punctuation():
    assert reverse_words_in_sentence("Hello, World!") == "olleH, dlroW!"

def test_reverse_words_in_sentence_invalid_input():
    with pytest.raises(TypeError):
        reverse_words_in_sentence(123)
    with pytest.raises(TypeError):
        reverse_words_in_sentence(None)