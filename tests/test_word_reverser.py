import pytest
from src.word_reverser import reverse_words_and_characters

def test_basic_reverse():
    assert reverse_words_and_characters("Hello World") == "dlroW olleH"

def test_multiple_words():
    assert reverse_words_and_characters("Python is awesome") == "emosewa si nohtyP"

def test_single_word():
    assert reverse_words_and_characters("Python") == "nohtyP"

def test_empty_string():
    assert reverse_words_and_characters("") == ""

def test_whitespace_string():
    assert reverse_words_and_characters("   ") == "   "

def test_mixed_case():
    assert reverse_words_and_characters("Hello WORLD Test") == "tseT DLROW olleH"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        reverse_words_and_characters(123)
        
def test_string_with_punctuation():
    assert reverse_words_and_characters("Hello, World!") == "!dlroW ,olleH"