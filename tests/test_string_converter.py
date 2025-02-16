import pytest
from src.string_converter import convert_to_alternating_lower

def test_alternating_lower_normal_string():
    assert convert_to_alternating_lower("HelloWorld") == "hElLoWoRlD"

def test_alternating_lower_empty_string():
    assert convert_to_alternating_lower("") == ""

def test_alternating_lower_single_character():
    assert convert_to_alternating_lower("A") == "a"

def test_alternating_lower_with_spaces():
    assert convert_to_alternating_lower("Hello World") == "hElLo WoRlD"

def test_alternating_lower_with_numbers_and_symbols():
    assert convert_to_alternating_lower("H3llo!World") == "h3ElLo!wOrLd"

def test_alternating_lower_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_lower(123)
    with pytest.raises(TypeError):
        convert_to_alternating_lower(None)