import pytest
from src.word_reverser import reverse_words_in_string

def test_basic_word_reversal():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"

def test_capitalization_preservation():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"
    assert reverse_words_in_string("Python Programming") == "nohtyP gnimmargorP"

def test_punctuation_preservation():
    assert reverse_words_in_string("Hello, World!") == "olleH, dlroW!"
    assert reverse_words_in_string("Stop. Think, Create!") == "potS. knihT, etaerc!"

def test_mixed_case_words():
    assert reverse_words_in_string("Hello, MiXeD CaSe!") == "olleH, dExIm eSaC!"

def test_multiple_punctuation():
    assert reverse_words_in_string("Hello... World!!!") == "olleH... dlroW!!!"

def test_empty_string():
    assert reverse_words_in_string("") == ""

def test_single_word():
    assert reverse_words_in_string("Python") == "nohtyP"

def test_string_with_numbers():
    assert reverse_words_in_string("Hello2 World3") == "olleH2 dlroW3"

def test_whitespace_preservation():
    assert reverse_words_in_string("  Hello   World  ") == "  olleH   dlroW  "

def test_complex_string():
    assert reverse_words_in_string("Hello, World! How are you?") == "olleH, dlroW! woH era ?uoy"