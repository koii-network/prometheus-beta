import pytest
from src.string_converter import convert_to_upper_case_with_spaces

def test_convert_to_upper_case_with_spaces():
    # Test basic conversion
    assert convert_to_upper_case_with_spaces("helloWorld") == "HELLO WORLD"
    assert convert_to_upper_case_with_spaces("camelCaseString") == "CAMEL CASE STRING"
    
    # Test string with existing spaces
    assert convert_to_upper_case_with_spaces("hello world") == "HELLO WORLD"
    
    # Test single word
    assert convert_to_upper_case_with_spaces("hello") == "HELLO"
    
    # Test empty string
    assert convert_to_upper_case_with_spaces("") == ""
    
    # Test with numbers and mixed case
    assert convert_to_upper_case_with_spaces("hello2World") == "HELLO 2 WORLD"
    
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_upper_case_with_spaces(123)
    
    with pytest.raises(TypeError):
        convert_to_upper_case_with_spaces(None)