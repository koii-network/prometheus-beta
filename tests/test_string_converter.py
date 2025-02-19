import pytest
from src.string_converter import to_constant_case

def test_to_constant_case():
    # Test basic string conversion
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("hello_world") == "HELLO_WORLD"
    assert to_constant_case("HelloWorld") == "HELLO_WORLD"
    
    # Test with special characters
    assert to_constant_case("hello-world!") == "HELLO_WORLD"
    assert to_constant_case("hello@world") == "HELLO_WORLD"
    
    # Test with numbers
    assert to_constant_case("hello2world") == "HELLO_2_WORLD"
    
    # Test empty string
    assert to_constant_case("") == ""
    
    # Test multiple consecutive delimiters
    assert to_constant_case("hello---world") == "HELLO_WORLD"
    
    # Test leading/trailing special characters
    assert to_constant_case("  hello world  ") == "HELLO_WORLD"

def test_to_constant_case_error_handling():
    # Test non-string input
    with pytest.raises(TypeError):
        to_constant_case(123)
    
    with pytest.raises(TypeError):
        to_constant_case(None)
    
    with pytest.raises(TypeError):
        to_constant_case(["hello", "world"])