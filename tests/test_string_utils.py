import pytest
from src.string_utils import convert_to_lowercase

def test_convert_to_lowercase_basic():
    """Test basic lowercase conversion."""
    assert convert_to_lowercase("HELLO") == "hello"
    assert convert_to_lowercase("World") == "world"

def test_convert_to_lowercase_already_lowercase():
    """Test string that is already lowercase."""
    assert convert_to_lowercase("hello") == "hello"

def test_convert_to_lowercase_mixed_case():
    """Test mixed case string conversion."""
    assert convert_to_lowercase("HeLLo WoRLd") == "hello world"

def test_convert_to_lowercase_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase("") == ""

def test_convert_to_lowercase_with_numbers_and_symbols():
    """Test conversion of string with numbers and symbols."""
    assert convert_to_lowercase("Hello123!@#") == "hello123!@#"

def test_convert_to_lowercase_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(None)