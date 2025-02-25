import pytest
from src.lowercase_converter import convert_to_lowercase

def test_convert_to_lowercase_normal_string():
    """Test conversion of a normal mixed-case string."""
    assert convert_to_lowercase("Hello World") == "hello world"

def test_convert_to_lowercase_already_lowercase():
    """Test conversion of an already lowercase string."""
    assert convert_to_lowercase("hello") == "hello"

def test_convert_to_lowercase_uppercase():
    """Test conversion of an uppercase string."""
    assert convert_to_lowercase("PYTHON") == "python"

def test_convert_to_lowercase_mixed_case():
    """Test conversion of a mixed-case string with numbers and symbols."""
    assert convert_to_lowercase("HeLLo123!@#") == "hello123!@#"

def test_convert_to_lowercase_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase("") == ""

def test_convert_to_lowercase_non_string_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(["hello"])