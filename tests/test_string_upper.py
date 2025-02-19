import pytest
from src.string_upper import convert_to_upper_with_spaces

def test_convert_to_upper_with_spaces():
    # Test basic conversion
    assert convert_to_upper_with_spaces("hello world") == "HELLO WORLD"
    assert convert_to_upper_with_spaces("Python is awesome") == "PYTHON IS AWESOME"
    
    # Test empty string
    assert convert_to_upper_with_spaces("") == ""
    
    # Test string with mixed case
    assert convert_to_upper_with_spaces("HeLLo WoRlD") == "HELLO WORLD"
    
    # Test string with special characters and spaces
    assert convert_to_upper_with_spaces("hello, world! 123") == "HELLO, WORLD! 123"

def test_convert_to_upper_with_spaces_error_handling():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_with_spaces(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_with_spaces(["hello"])