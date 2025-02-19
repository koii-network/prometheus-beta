import pytest
from src.alternating_caps import convert_to_alternating_caps

def test_basic_conversion():
    assert convert_to_alternating_caps("hello") == "HeLlO"
    assert convert_to_alternating_caps("world") == "WoRlD"

def test_empty_string():
    assert convert_to_alternating_caps("") == ""

def test_single_character():
    assert convert_to_alternating_caps("a") == "A"
    assert convert_to_alternating_caps("B") == "B"

def test_multiple_words():
    assert convert_to_alternating_caps("hello world") == "HeLlO WoRlD"

def test_mixed_case_input():
    assert convert_to_alternating_caps("HeLLo") == "HeLlO"

def test_non_string_input():
    with pytest.raises(TypeError):
        convert_to_alternating_caps(123)
        convert_to_alternating_caps(None)