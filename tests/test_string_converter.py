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

def test_convert_to_uppercase_with_numbers_and_symbols():
    """Test conversion of strings with numbers and symbols."""
    assert convert_to_uppercase("hello123!@#") == "HELLO123!@#"

def test_convert_to_uppercase_unicode():
    """Test conversion of unicode characters."""
    assert convert_to_uppercase("héllö wörld") == "HÉLLÖ WÖRLD"

def test_convert_to_uppercase_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase(["hello"])