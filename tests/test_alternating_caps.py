import pytest
from src.alternating_caps import convert_to_alternating_caps

def test_convert_to_alternating_caps_normal_string():
    assert convert_to_alternating_caps("hello") == "HeLlO"
    assert convert_to_alternating_caps("python") == "PyThOn"

def test_convert_to_alternating_caps_empty_string():
    assert convert_to_alternating_caps("") == ""

def test_convert_to_alternating_caps_with_spaces():
    assert convert_to_alternating_caps("hello world") == "HeLlO WoRlD"

def test_convert_to_alternating_caps_with_numbers_and_symbols():
    assert convert_to_alternating_caps("hello 123 world!") == "HeLlO 123 WoRlD!"

def test_convert_to_alternating_caps_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_caps(123)
    with pytest.raises(TypeError):
        convert_to_alternating_caps(None)