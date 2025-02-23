import pytest
from src.alternating_constant_case import to_alternating_constant_case

def test_alternating_constant_case_basic():
    assert to_alternating_constant_case("hello") == "HeLlO"
    assert to_alternating_constant_case("world") == "WoRlD"

def test_alternating_constant_case_mixed_case():
    assert to_alternating_constant_case("PyThOn") == "PyThOn"
    assert to_alternating_constant_case("PrOgRaMmInG") == "PrOgRaMmInG"

def test_alternating_constant_case_empty_string():
    assert to_alternating_constant_case("") == ""

def test_alternating_constant_case_with_spaces():
    assert to_alternating_constant_case("hello world") == "HeLlO wOrLd"

def test_alternating_constant_case_special_characters():
    assert to_alternating_constant_case("hello123!") == "HeLlO123!"

def test_alternating_constant_case_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_constant_case(123)
    with pytest.raises(TypeError):
        to_alternating_constant_case(None)