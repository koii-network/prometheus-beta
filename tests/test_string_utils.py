import pytest
from src.string_utils import to_sentence_case

def test_to_sentence_case_normal_string():
    assert to_sentence_case("hello world") == "Hello world"
    assert to_sentence_case("HELLO WORLD") == "Hello world"
    assert to_sentence_case("hElLo WoRlD") == "Hello world"

def test_to_sentence_case_single_word():
    assert to_sentence_case("hello") == "Hello"
    assert to_sentence_case("HELLO") == "Hello"

def test_to_sentence_case_empty_string():
    assert to_sentence_case("") == ""

def test_to_sentence_case_whitespace():
    assert to_sentence_case("  hello world  ") == "  hello world  "

def test_to_sentence_case_invalid_input():
    with pytest.raises(TypeError):
        to_sentence_case(123)
    with pytest.raises(TypeError):
        to_sentence_case(None)