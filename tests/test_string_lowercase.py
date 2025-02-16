import pytest
from src.string_lowercase import convert_to_lowercase

def test_convert_to_lowercase_normal_string():
    """Test converting a normal mixed-case string to lowercase."""
    assert convert_to_lowercase("Hello World") == "hello world"

def test_convert_to_lowercase_already_lowercase():
    """Test converting an already lowercase string."""
    assert convert_to_lowercase("hello") == "hello"

def test_convert_to_lowercase_uppercase():
    """Test converting an uppercase string to lowercase."""
    assert convert_to_lowercase("PYTHON") == "python"

def test_convert_to_lowercase_empty_string():
    """Test converting an empty string."""
    assert convert_to_lowercase("") == ""

def test_convert_to_lowercase_with_numbers_and_symbols():
    """Test converting a string with numbers and symbols."""
    assert convert_to_lowercase("Hello123!@#") == "hello123!@#"

def test_convert_to_lowercase_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(["list"])