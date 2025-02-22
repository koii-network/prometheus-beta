import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_normal_string():
    assert convert_to_alternating_case("hello") == "HeLlO"
    assert convert_to_alternating_case("world") == "WoRlD"

def test_convert_to_alternating_case_empty_string():
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_spaces():
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"

def test_convert_to_alternating_case_special_characters():
    assert convert_to_alternating_case("hello!world") == "HeLlO!WoRlD"

def test_convert_to_alternating_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_case(None)