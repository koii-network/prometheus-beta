import pytest
from src.inverse_case import convert_to_inverse_case

def test_convert_to_inverse_case_basic():
    """Test basic inverse case conversion."""
    assert convert_to_inverse_case("Hello World") == "hELLO wORLD"

def test_convert_to_inverse_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_inverse_case("") == ""

def test_convert_to_inverse_case_mixed_case():
    """Test conversion of a mixed case string."""
    assert convert_to_inverse_case("MiXeD cAsE") == "mIxEd CaSe"

def test_convert_to_inverse_case_special_chars():
    """Test conversion of string with special characters."""
    assert convert_to_inverse_case("Hello, World! 123") == "hELLO, wORLD! 123"

def test_convert_to_inverse_case_non_string_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(None)