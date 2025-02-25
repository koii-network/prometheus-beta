import pytest
from src.lowercase_converter import convert_to_lowercase_with_spaces

def test_convert_to_lowercase_with_spaces():
    # Test basic lowercase conversion
    assert convert_to_lowercase_with_spaces("Hello World") == "hello world"
    
    # Test already lowercase string
    assert convert_to_lowercase_with_spaces("hello world") == "hello world"
    
    # Test string with mixed case
    assert convert_to_lowercase_with_spaces("HeLLo WoRLD") == "hello world"
    
    # Test string with numbers and special characters
    assert convert_to_lowercase_with_spaces("Hello123 World!") == "hello123 world!"
    
    # Test empty string
    assert convert_to_lowercase_with_spaces("") == ""
    
    # Test string with multiple spaces
    assert convert_to_lowercase_with_spaces("  Spaced  Out  ") == "  spaced  out  "

def test_convert_to_lowercase_with_spaces_error_handling():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(["Hello", "World"])