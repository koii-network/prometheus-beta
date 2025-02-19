import pytest
from src.alternating_case import to_alternating_sentence_case

def test_basic_alternating_case():
    assert to_alternating_sentence_case("hello world") == "HeLlO WoRlD"

def test_mixed_case_input():
    assert to_alternating_sentence_case("Hello WORLD") == "HeLlO WoRlD"

def test_non_alphabetic_characters():
    assert to_alternating_sentence_case("hello 123 world!") == "HeLlO 123 WoRlD!"

def test_empty_string():
    assert to_alternating_sentence_case("") == ""

def test_single_character():
    assert to_alternating_sentence_case("a") == "A"

def test_non_string_input():
    with pytest.raises(TypeError):
        to_alternating_sentence_case(123)

def test_special_characters():
    assert to_alternating_sentence_case("hello, world!") == "HeLlO, WoRlD!"