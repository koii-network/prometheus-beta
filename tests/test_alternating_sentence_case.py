import pytest
from src.alternating_sentence_case import alternating_sentence_case

def test_alternating_sentence_case_normal():
    assert alternating_sentence_case("hello world python coding") == "Hello world Python coding"

def test_alternating_sentence_case_single_word():
    assert alternating_sentence_case("hello") == "Hello"

def test_alternating_sentence_case_empty_string():
    assert alternating_sentence_case("") == ""

def test_alternating_sentence_case_multiple_words():
    assert alternating_sentence_case("this is a test of alternating case") == "This is A test OF alternating CASE"

def test_alternating_sentence_case_invalid_input():
    with pytest.raises(TypeError):
        alternating_sentence_case(123)
    with pytest.raises(TypeError):
        alternating_sentence_case(None)