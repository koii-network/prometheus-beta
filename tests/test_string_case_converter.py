import pytest
from src.string_case_converter import convert_to_header_case

def test_convert_to_header_case():
    # Test basic string conversion
    assert convert_to_header_case("hello world") == "HelloWorld"
    assert convert_to_header_case("python is awesome") == "PythonIsAwesome"
    
    # Test with different separators
    assert convert_to_header_case("python_is_awesome") == "PythonIsAwesome"
    assert convert_to_header_case("convert-to-header-case") == "ConvertToHeaderCase"
    
    # Test with mixed case input
    assert convert_to_header_case("Hello_world-TESTING") == "HelloWorldTesting"
    
    # Test with single word
    assert convert_to_header_case("hello") == "Hello"
    
    # Test empty string
    assert convert_to_header_case("") == ""
    
    # Test type error
    with pytest.raises(TypeError):
        convert_to_header_case(123)
    
    with pytest.raises(TypeError):
        convert_to_header_case(None)