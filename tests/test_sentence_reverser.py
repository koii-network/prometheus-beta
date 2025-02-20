import pytest
from src.sentence_reverser import reverse_sentence_words

def test_basic_sentence_reversal():
    assert reverse_sentence_words("hello world") == "olleh dlrow"
    assert reverse_sentence_words("Python is awesome") == "nohtyP si emosewa"

def test_single_word():
    assert reverse_sentence_words("hello") == "olleh"

def test_empty_string():
    assert reverse_sentence_words("") == ""

def test_sentence_with_punctuation():
    assert reverse_sentence_words("Hello, world!") == "olleH, dlrow!"

def test_mixed_case_sentence():
    assert reverse_sentence_words("Python Is Great") == "nohtyP sI taerG"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        reverse_sentence_words(123)
    
    with pytest.raises(TypeError):
        reverse_sentence_words(None)