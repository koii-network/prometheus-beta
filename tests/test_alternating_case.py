import pytest
from src.alternating_case import convert_to_alternating_lower

def test_convert_to_alternating_lower_normal_string():
    assert convert_to_alternating_lower("Hello World") == "hElLo wOrLd"

def test_convert_to_alternating_lower_empty_string():
    assert convert_to_alternating_lower("") == ""

def test_convert_to_alternating_lower_single_char():
    assert convert_to_alternating_lower("a") == "a"
    assert convert_to_alternating_lower("B") == "b"

def test_convert_to_alternating_lower_special_chars():
    assert convert_to_alternating_lower("Hello123World!") == "hElLo123wOrLd!"

def test_convert_to_alternating_lower_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_lower(123)
    with pytest.raises(TypeError):
        convert_to_alternating_lower(None)