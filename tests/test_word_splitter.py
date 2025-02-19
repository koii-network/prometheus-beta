import pytest
from src.word_splitter import split_text_to_words

def test_basic_word_splitting():
    text = "HelloWorld"
    assert split_text_to_words(text) == ["Hello", "World"]

def test_with_punctuation():
    text = "Hello,World!How.Are.You"
    assert split_text_to_words(text) == ["Hello", ",World", "!How", ".Are", ".You"]

def test_consecutive_capital_letters():
    text = "HelloWORLDTest"
    assert split_text_to_words(text) == ["Hello", "WORLD", "Test"]

def test_mixed_case_with_punctuation():
    text = "Hello,WorldTestCase!"
    assert split_text_to_words(text) == ["Hello", ",World", "Test", "Case", "!"]

def test_empty_string():
    text = ""
    assert split_text_to_words(text) == []

def test_single_word():
    text = "SingleWord"
    assert split_text_to_words(text) == ["Single", "Word"]

def test_complex_text():
    text = "Hello,WorldHowAreYou!Testing123"
    assert split_text_to_words(text) == ["Hello", ",World", "How", "Are", "You", "!Testing", "123"]