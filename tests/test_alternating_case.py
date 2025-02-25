import pytest
from src.alternating_case import to_alternating_case

def test_alternating_case_normal_string():
    assert to_alternating_case("hello") == "HeLlO"
    assert to_alternating_case("world") == "WoRlD"

def test_alternating_case_mixed_input():
    assert to_alternating_case("HeLLo") == "HeLlO"

def test_alternating_case_empty_string():
    assert to_alternating_case("") == ""

def test_alternating_case_single_character():
    assert to_alternating_case("a") == "A"
    assert to_alternating_case("Z") == "Z"

def test_alternating_case_with_spaces():
    assert to_alternating_case("hello world") == "HeLlO WoRlD"

def test_alternating_case_with_numbers_and_symbols():
    assert to_alternating_case("hello123world!") == "HeLlO123WoRlD!"

def test_alternating_case_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_case(123)
    with pytest.raises(TypeError):
        to_alternating_case(None)