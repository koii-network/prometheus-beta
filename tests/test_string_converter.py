import pytest
from src.string_converter import convert_to_uppercase_with_spaces

def test_convert_to_uppercase_with_spaces():
    # Test basic conversion
    assert convert_to_uppercase_with_spaces("hello") == "H E L L O"
    
    # Test string with existing spaces
    assert convert_to_uppercase_with_spaces("hello world") == "H E L L O W O R L D"
    
    # Test empty string
    assert convert_to_uppercase_with_spaces("") == ""
    
    # Test string with mixed case
    assert convert_to_uppercase_with_spaces("HeLLo WoRLd") == "H E L L O W O R L D"
    
    # Test string with numbers and special characters
    assert convert_to_uppercase_with_spaces("hello123world!") == "H E L L O 1 2 3 W O R L D !"
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_uppercase_with_spaces(123)
    
    with pytest.raises(TypeError):
        convert_to_uppercase_with_spaces(None)