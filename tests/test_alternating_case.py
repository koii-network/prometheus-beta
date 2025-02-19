import pytest
from src.alternating_case import to_alternating_sentence_case

def test_alternating_sentence_case_basic():
    assert to_alternating_sentence_case("hello") == "HeLlO"
    assert to_alternating_sentence_case("world") == "WoRlD"

def test_alternating_sentence_case_empty_string():
    assert to_alternating_sentence_case("") == ""

def test_alternating_sentence_case_special_characters():
    assert to_alternating_sentence_case("hello world!") == "HeLlO WoRlD!"
    assert to_alternating_sentence_case("123 abc") == "123 AbC"

def test_alternating_sentence_case_error_handling():
    with pytest.raises(TypeError):
        to_alternating_sentence_case(123)
    with pytest.raises(TypeError):
        to_alternating_sentence_case(None)