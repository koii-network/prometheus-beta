import pytest
from src.string_utils import convert_to_snake_case

def test_convert_to_snake_case():
    # Test basic conversions
    assert convert_to_snake_case("hello world") == "hello_world"
    assert convert_to_snake_case("HelloWorld") == "hello_world"
    assert convert_to_snake_case("helloWorld") == "hello_world"
    
    # Test with special characters
    assert convert_to_snake_case("hello-world") == "hello_world"
    assert convert_to_snake_case("hello_World") == "hello_world"
    assert convert_to_snake_case("Hello@World") == "hello_world"
    
    # Test with numbers
    assert convert_to_snake_case("hello2World") == "hello2_world"
    assert convert_to_snake_case("Hello123World") == "hello123_world"
    
    # Test edge cases
    assert convert_to_snake_case("") == ""
    assert convert_to_snake_case("a") == "a"
    assert convert_to_snake_case("ABC") == "abc"
    
    # Test multiple consecutive special characters
    assert convert_to_snake_case("hello---world") == "hello_world"
    assert convert_to_snake_case("hello__world") == "hello_world"

def test_convert_to_snake_case_error_handling():
    # Test error handling
    with pytest.raises(TypeError):
        convert_to_snake_case(123)
    
    with pytest.raises(TypeError):
        convert_to_snake_case(None)
    
    with pytest.raises(TypeError):
        convert_to_snake_case(["hello", "world"])