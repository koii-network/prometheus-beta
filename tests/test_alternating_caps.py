import pytest
from src.alternating_caps import to_alternating_caps

def test_basic_alternating_caps():
    assert to_alternating_caps("hello") == "HeLlO"
    assert to_alternating_caps("world") == "WoRlD"

def test_empty_string():
    assert to_alternating_caps("") == ""

def test_single_character():
    assert to_alternating_caps("a") == "A"
    assert to_alternating_caps("B") == "B"

def test_with_spaces():
    assert to_alternating_caps("hello world") == "HeLlO WoRlD"

def test_with_numbers_and_symbols():
    assert to_alternating_caps("hello123!world") == "HeLlO123!WoRlD"

def test_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_caps(123)
    
    with pytest.raises(TypeError):
        to_alternating_caps(None)