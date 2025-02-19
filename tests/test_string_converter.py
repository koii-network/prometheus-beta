import pytest
from src.string_converter import to_snake_case

def test_to_snake_case():
    # Test basic conversions
    assert to_snake_case("helloWorld") == "hello_world"
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("hello_world") == "hello_world"
    assert to_snake_case("HelloWorldExample") == "hello_world_example"
    
    # Test with special characters and spaces
    assert to_snake_case("hello world") == "hello_world"
    assert to_snake_case("hello-world") == "hello_world"
    assert to_snake_case("hello_World") == "hello_world"
    
    # Test with numbers
    assert to_snake_case("hello2World") == "hello2_world"
    assert to_snake_case("hello_2_world") == "hello_2_world"
    
    # Test edge cases
    assert to_snake_case("") == ""
    assert to_snake_case("a") == "a"
    assert to_snake_case("A") == "a"
    
    # Test error handling
    with pytest.raises(TypeError):
        to_snake_case(123)
    with pytest.raises(TypeError):
        to_snake_case(None)