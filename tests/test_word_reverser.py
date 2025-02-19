import pytest
from src.word_reverser import reverse_words_in_string

def test_basic_word_reversal():
    assert reverse_words_in_string("hello world") == "olleh dlrow"

def test_mixed_case_preservation():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"

def test_punctuation_preservation():
    assert reverse_words_in_string("Hello, world!") == "olleH, dlrow!"

def test_multiple_words():
    assert reverse_words_in_string("Python is awesome") == "nohtyP si emosewa"

def test_all_uppercase():
    assert reverse_words_in_string("HELLO WORLD") == "OLLEH DLROW"

def test_mixed_case_complex():
    assert reverse_words_in_string("Hello, Python Programming!") == "olleH, nohtyP gnimmargorP!"

def test_empty_string():
    assert reverse_words_in_string("") == ""

def test_single_word():
    assert reverse_words_in_string("Radar") == "radaR"

def test_spaces_and_punctuation():
    assert reverse_words_in_string("  Hello,   world!  ") == "  olleH,   dlrow!  "

def test_numbers_and_words():
    assert reverse_words_in_string("Python 3.9 is great") == "nohtyP 9.3 si taerg"