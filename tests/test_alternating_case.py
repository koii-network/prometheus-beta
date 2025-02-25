import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    """Test basic conversion of string to alternating case."""
    assert convert_to_alternating_case("hello world python programming") == "Hello world Python programming"

def test_convert_to_alternating_case_mixed_input():
    """Test conversion with mixed case input."""
    assert convert_to_alternating_case("HELLO world PYTHON programming") == "Hello world Python programming"

def test_convert_to_alternating_case_single_word():
    """Test conversion with a single word."""
    assert convert_to_alternating_case("hello") == "Hello"

def test_convert_to_alternating_case_empty_string():
    """Test conversion with an empty string."""
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(123)

def test_convert_to_alternating_case_multiple_spaces():
    """Test conversion with multiple spaces between words."""
    assert convert_to_alternating_case("hello   world  python") == "Hello world Python"