import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    """Test basic alternating case conversion."""
    assert convert_to_alternating_case("hello") == "HeLlO"
    assert convert_to_alternating_case("world") == "WoRlD"

def test_convert_to_alternating_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_single_char():
    """Test conversion of a single character."""
    assert convert_to_alternating_case("a") == "A"
    assert convert_to_alternating_case("B") == "B"

def test_convert_to_alternating_case_with_spaces():
    """Test conversion of a string with spaces."""
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"

def test_convert_to_alternating_case_with_numbers_and_symbols():
    """Test conversion of a string with numbers and symbols."""
    assert convert_to_alternating_case("h3llo world!") == "H3LlO WoRlD!"

def test_convert_to_alternating_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_alternating_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_case(None)