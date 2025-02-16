import pytest
from src.string_utils import convert_to_lowercase_with_spaces

def test_convert_to_lowercase_with_spaces():
    # Test basic lowercase conversion
    assert convert_to_lowercase_with_spaces("HELLO WORLD") == "hello world"
    
    # Test mixed case
    assert convert_to_lowercase_with_spaces("HeLLo WoRLD") == "hello world"
    
    # Test already lowercase
    assert convert_to_lowercase_with_spaces("hello world") == "hello world"
    
    # Test with multiple spaces
    assert convert_to_lowercase_with_spaces("  HELLO   WORLD  ") == "  hello   world  "
    
    # Test empty string
    assert convert_to_lowercase_with_spaces("") == ""
    
    # Test strings with special characters and numbers
    assert convert_to_lowercase_with_spaces("HELLO123 WORLD!") == "hello123 world!"

def test_convert_to_lowercase_with_spaces_error_handling():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(None)