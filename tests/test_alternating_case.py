import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    assert convert_to_alternating_case("hello") == "HeLlO"
    assert convert_to_alternating_case("world") == "WoRlD"

def test_convert_to_alternating_case_empty_string():
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_with_spaces():
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"

def test_convert_to_alternating_case_with_numbers_and_symbols():
    assert convert_to_alternating_case("hello123 world!") == "HeLlO123 WoRlD!"

def test_convert_to_alternating_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_case(None)