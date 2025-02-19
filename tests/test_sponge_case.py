import pytest
from src.sponge_case import convert_to_sponge_case

def test_convert_to_sponge_case_normal_string():
    """Test conversion of a normal string."""
    assert convert_to_sponge_case("hello world") == "hElLo WoRlD"

def test_convert_to_sponge_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_sponge_case("") == ""

def test_convert_to_sponge_case_single_char():
    """Test conversion of a single character."""
    assert convert_to_sponge_case("a") == "a"
    assert convert_to_sponge_case("B") == "b"

def test_convert_to_sponge_case_with_spaces():
    """Test conversion of a string with multiple spaces."""
    assert convert_to_sponge_case("  hello  world  ") == "  HeLlO  WoRlD  "

def test_convert_to_sponge_case_with_numbers_and_symbols():
    """Test conversion of string with numbers and symbols."""
    assert convert_to_sponge_case("hello123world!@#") == "hElLo123WoRlD!@#"

def test_convert_to_sponge_case_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_sponge_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_sponge_case(None)