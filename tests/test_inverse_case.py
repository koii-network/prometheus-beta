import pytest
from src.inverse_case import convert_to_inverse_case

def test_convert_to_inverse_case_basic():
    """Test basic inverse case conversion"""
    assert convert_to_inverse_case("Hello") == "hELLO"
    assert convert_to_inverse_case("wORLD") == "World"

def test_convert_to_inverse_case_mixed():
    """Test mixed case conversion"""
    assert convert_to_inverse_case("HeLLo WoRLD") == "hEllO wOrld"

def test_convert_to_inverse_case_special_chars():
    """Test preservation of special characters and numbers"""
    assert convert_to_inverse_case("Hello123!@#") == "hELLO123!@#"

def test_convert_to_inverse_case_empty_string():
    """Test empty string input"""
    assert convert_to_inverse_case("") == ""

def test_convert_to_inverse_case_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        convert_to_inverse_case(123)
    with pytest.raises(TypeError):
        convert_to_inverse_case(None)