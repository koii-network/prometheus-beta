import pytest
from src.string_converter import convert_to_lowercase_with_spaces

def test_convert_to_lowercase_with_spaces():
    # Test basic lowercase conversion
    assert convert_to_lowercase_with_spaces("HELLO WORLD") == "hello world"
    
    # Test mixed case conversion
    assert convert_to_lowercase_with_spaces("HeLLo WoRLd") == "hello world"
    
    # Test string with existing lowercase letters
    assert convert_to_lowercase_with_spaces("hello WORLD") == "hello world"
    
    # Test string with special characters and spaces
    assert convert_to_lowercase_with_spaces("Hello, World! 123") == "hello, world! 123"
    
    # Test empty string
    assert convert_to_lowercase_with_spaces("") == ""
    
    # Test string with only spaces
    assert convert_to_lowercase_with_spaces("   ") == "   "

def test_convert_to_lowercase_with_spaces_error_handling():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(None)