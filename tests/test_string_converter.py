import pytest
from src.string_converter import convert_to_uppercase_with_spaces

def test_convert_to_uppercase_with_spaces():
    # Test basic string conversion
    assert convert_to_uppercase_with_spaces("hello world") == "HELLO WORLD"
    
    # Test string with mixed case
    assert convert_to_uppercase_with_spaces("Hello World") == "HELLO WORLD"
    
    # Test string with existing spaces
    assert convert_to_uppercase_with_spaces("  hello  world  ") == "  HELLO  WORLD  "
    
    # Test empty string
    assert convert_to_uppercase_with_spaces("") == ""
    
def test_convert_to_uppercase_with_spaces_error_handling():
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(["hello"])