import pytest
from src.string_converter import convert_to_uppercase_with_spaces

def test_convert_to_uppercase_with_spaces():
    # Test basic camel case conversion
    assert convert_to_uppercase_with_spaces("helloWorld") == "HELLO WORLD"
    assert convert_to_uppercase_with_spaces("camelCaseString") == "CAMEL CASE STRING"
    
    # Test string with existing spaces
    assert convert_to_uppercase_with_spaces("hello world") == "HELLO WORLD"
    
    # Test single word
    assert convert_to_uppercase_with_spaces("hello") == "HELLO"
    
    # Test empty string
    assert convert_to_uppercase_with_spaces("") == ""
    
    # Test with multiple capital letters
    assert convert_to_uppercase_with_spaces("HelloWorldExample") == "HELLO WORLD EXAMPLE"

def test_convert_to_uppercase_with_spaces_error_handling():
    # Test non-string input
    with pytest.raises(TypeError):
        convert_to_uppercase_with_spaces(123)
    
    with pytest.raises(TypeError):
        convert_to_uppercase_with_spaces(None)
    
    with pytest.raises(TypeError):
        convert_to_uppercase_with_spaces(["hello"])