import pytest
from src.alternating_case import to_alternating_constant_case

def test_to_alternating_constant_case_basic():
    assert to_alternating_constant_case("hello") == "HeLlO"
    assert to_alternating_constant_case("world") == "WoRlD"

def test_to_alternating_constant_case_mixed_case():
    assert to_alternating_constant_case("PythON") == "PyThOn"

def test_to_alternating_constant_case_empty_string():
    assert to_alternating_constant_case("") == ""

def test_to_alternating_constant_case_single_char():
    assert to_alternating_constant_case("a") == "A"
    assert to_alternating_constant_case("B") == "B"

def test_to_alternating_constant_case_spaces_and_symbols():
    assert to_alternating_constant_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_constant_case("hello, world!") == "HeLlO, WoRlD!"

def test_to_alternating_constant_case_non_string_input():
    with pytest.raises(TypeError):
        to_alternating_constant_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_constant_case(None)