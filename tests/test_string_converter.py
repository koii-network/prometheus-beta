import pytest
from src.string_converter import to_sentence_case

def test_to_sentence_case_normal_string():
    assert to_sentence_case("HELLO WORLD") == "Hello world"
    assert to_sentence_case("hello WORLD") == "Hello world"

def test_to_sentence_case_empty_string():
    assert to_sentence_case("") == ""

def test_to_sentence_case_single_character():
    assert to_sentence_case("a") == "A"
    assert to_sentence_case("Z") == "Z"

def test_to_sentence_case_already_sentence_case():
    assert to_sentence_case("Hello world") == "Hello world"

def test_to_sentence_case_invalid_input():
    with pytest.raises(TypeError):
        to_sentence_case(123)
    with pytest.raises(TypeError):
        to_sentence_case(None)