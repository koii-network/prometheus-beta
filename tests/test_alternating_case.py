import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_normal_string():
    assert convert_to_alternating_case("hello") == "hElLo"
    assert convert_to_alternating_case("world") == "wOrLd"

def test_convert_to_alternating_case_mixed_case():
    assert convert_to_alternating_case("HeLLo") == "hElLo"

def test_convert_to_alternating_case_empty_string():
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_with_spaces():
    assert convert_to_alternating_case("hello world") == "hElLo WoRlD"

def test_convert_to_alternating_case_with_numbers_and_symbols():
    assert convert_to_alternating_case("hello123world!") == "hElLo123WoRlD!"

def test_convert_to_alternating_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_case(None)