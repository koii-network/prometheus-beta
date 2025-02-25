import pytest
from src.string_case_converter import alternating_constant_case

def test_alternating_constant_case_normal_input():
    assert alternating_constant_case("hello world") == "HELLO world"
    assert alternating_constant_case("python is awesome") == "PYTHON is AWESOME"

def test_alternating_constant_case_single_word():
    assert alternating_constant_case("hello") == "HELLO"
    assert alternating_constant_case("world") == "WORLD"

def test_alternating_constant_case_empty_string():
    assert alternating_constant_case("") == ""

def test_alternating_constant_case_multiple_words():
    assert alternating_constant_case("a b c d e") == "A b C d E"

def test_alternating_constant_case_invalid_input():
    with pytest.raises(TypeError):
        alternating_constant_case(123)
    with pytest.raises(TypeError):
        alternating_constant_case(None)