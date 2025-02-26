import pytest
from src.string_utils import convert_to_snake_case

def test_convert_to_snake_case():
    # Test basic conversions
    assert convert_to_snake_case("Hello World") == "hello_world"
    assert convert_to_snake_case("HelloWorld") == "hello_world"
    assert convert_to_snake_case("hello_world") == "hello_world"
    
    # Test with special characters
    assert convert_to_snake_case("Hello-World") == "hello_world"
    assert convert_to_snake_case("Hello World!") == "hello_world"
    assert convert_to_snake_case("Hello@World") == "hello_world"
    
    # Test with numbers
    assert convert_to_snake_case("Hello2World") == "hello2_world"
    
    # Test mixed case scenarios
    assert convert_to_snake_case("camelCaseString") == "camel_case_string"
    assert convert_to_snake_case("PascalCaseString") == "pascal_case_string"
    
    # Test edge cases
    assert convert_to_snake_case("") == ""
    assert convert_to_snake_case("a") == "a"
    assert convert_to_snake_case("ABC") == "abc"

def test_convert_to_snake_case_error_handling():
    # Test non-string input
    with pytest.raises(TypeError):
        convert_to_snake_case(123)
    
    with pytest.raises(TypeError):
        convert_to_snake_case(None)
    
    with pytest.raises(TypeError):
        convert_to_snake_case(["hello", "world"])