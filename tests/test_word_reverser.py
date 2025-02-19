import pytest
from src.word_reverser import reverse_words_in_string

def test_simple_word_reversal():
    assert reverse_words_in_string("Hello") == "olleH"
    assert reverse_words_in_string("world") == "dlrow"

def test_multiple_words():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"
    assert reverse_words_in_string("Python is awesome") == "nohtyP si emosewa"

def test_capitalization_preservation():
    assert reverse_words_in_string("Hello") == "olleH"
    assert reverse_words_in_string("World") == "dlroW"
    assert reverse_words_in_string("Hello World") == "olleH dlroW"

def test_punctuation_preservation():
    assert reverse_words_in_string("Hello, World!") == "olleH, dlroW!"
    assert reverse_words_in_string("Python, is amazing.") == "nohtyP, si gnizama."

def test_mixed_case():
    assert reverse_words_in_string("Python Is Great") == "nohtyP sI taerG"

def test_empty_string():
    assert reverse_words_in_string("") == ""

def test_single_character():
    assert reverse_words_in_string("a") == "a"
    assert reverse_words_in_string("A") == "A"

def test_complex_sentence():
    assert reverse_words_in_string("Hello, how are you today?") == "olleH, woh era uoy yadot?"