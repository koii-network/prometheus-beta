import pytest
from src.string_converter import convert_to_uppercase

def test_convert_to_uppercase_basic():
    """Test basic string uppercase conversion."""
    assert convert_to_uppercase("hello") == "HELLO"
    assert convert_to_uppercase("world") == "WORLD"

def test_convert_to_uppercase_mixed_case():
    """Test mixed case string conversion."""
    assert convert_to_uppercase("HeLLo WoRLd") == "HELLO WORLD"

def test_convert_to_uppercase_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_uppercase("") == ""

def test_convert_to_uppercase_with_special_chars():
    """Test conversion with special characters and numbers."""
    assert convert_to_uppercase("hello, world! 123") == "HELLO, WORLD! 123"

def test_convert_to_uppercase_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(["hello"])