import pytest
from src.string_case_converter import convert_to_inverse_case

def test_convert_to_inverse_case_basic():
    """Test basic inverse case conversion."""
    assert convert_to_inverse_case("Hello World") == "hELLO wORLD"

def test_convert_to_inverse_case_mixed():
    """Test mixed case conversion."""
    assert convert_to_inverse_case("PyThOn") == "pYtHoN"

def test_convert_to_inverse_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_inverse_case("") == ""

def test_convert_to_inverse_case_special_characters():
    """Test conversion with special characters and numbers."""
    assert convert_to_inverse_case("Hello, World! 123") == "hELLO, wORLD! 123"

def test_convert_to_inverse_case_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(123)
        convert_to_inverse_case(None)
        convert_to_inverse_case(["list"])