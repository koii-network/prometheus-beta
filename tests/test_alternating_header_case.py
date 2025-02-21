import pytest
from src.alternating_header_case import to_alternating_header_case

def test_basic_alternating_header_case():
    assert to_alternating_header_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_header_case("python is awesome") == "PyThOn Is AwEsOmE"

def test_empty_string():
    assert to_alternating_header_case("") == ""

def test_single_character():
    assert to_alternating_header_case("a") == "A"
    assert to_alternating_header_case("B") == "B"

def test_multiple_spaces():
    assert to_alternating_header_case("  hello  world  ") == "  HeLlO  WoRlD  "

def test_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_header_case(None)
    with pytest.raises(TypeError):
        to_alternating_header_case(123)
    with pytest.raises(TypeError):
        to_alternating_header_case(["hello"])