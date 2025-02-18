import pytest
from src.lowercase_converter import convert_to_lowercase

def test_convert_to_lowercase_basic():
    """Test basic lowercase conversion."""
    assert convert_to_lowercase("HELLO") == "hello"
    assert convert_to_lowercase("World") == "world"
    assert convert_to_lowercase("python") == "python"

def test_convert_to_lowercase_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase("") == ""

def test_convert_to_lowercase_already_lowercase():
    """Test converting an already lowercase string."""
    assert convert_to_lowercase("hello") == "hello"

def test_convert_to_lowercase_mixed_case():
    """Test converting a mixed case string."""
    assert convert_to_lowercase("HeLLo WoRLD") == "hello world"

def test_convert_to_lowercase_with_numbers_and_symbols():
    """Test converting a string with numbers and symbols."""
    assert convert_to_lowercase("Hello123!@#") == "hello123!@#"

def test_convert_to_lowercase_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(["hello"])