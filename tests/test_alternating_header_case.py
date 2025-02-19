import pytest
from src.alternating_header_case import alternating_header_case

def test_alternating_header_case_basic():
    assert alternating_header_case("hello world") == "HeLlO WoRlD"
    assert alternating_header_case("python programming") == "PyThOn PrOgRaMmInG"

def test_alternating_header_case_empty_string():
    assert alternating_header_case("") == ""

def test_alternating_header_case_single_character():
    assert alternating_header_case("a") == "A"
    assert alternating_header_case("B") == "B"

def test_alternating_header_case_with_numbers_and_symbols():
    assert alternating_header_case("hello 123 world!") == "HeLlO 123 WoRlD!"

def test_alternating_header_case_invalid_input():
    with pytest.raises(TypeError):
        alternating_header_case(123)
    
    with pytest.raises(TypeError):
        alternating_header_case(None)