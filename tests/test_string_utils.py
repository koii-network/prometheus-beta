import pytest
from src.string_utils import convert_to_uppercase

def test_convert_to_uppercase_basic():
    """Test basic string uppercase conversion."""
    assert convert_to_uppercase("hello") == "HELLO"
    assert convert_to_uppercase("World") == "WORLD"

def test_convert_to_uppercase_empty_string():
    """Test uppercase conversion with an empty string."""
    assert convert_to_uppercase("") == ""

def test_convert_to_uppercase_with_numbers_and_symbols():
    """Test uppercase conversion with numbers and symbols."""
    assert convert_to_uppercase("hello123!") == "HELLO123!"

def test_convert_to_uppercase_already_uppercase():
    """Test uppercase conversion for an already uppercase string."""
    assert convert_to_uppercase("HELLO") == "HELLO"

def test_convert_to_uppercase_mixed_case():
    """Test uppercase conversion for a mixed case string."""
    assert convert_to_uppercase("HeLLo WoRLd") == "HELLO WORLD"

def test_convert_to_uppercase_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(["hello"])