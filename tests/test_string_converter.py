import pytest
from src.string_converter import to_snake_case

def test_camel_case_conversion():
    """Test conversion of camelCase to snake_case"""
    assert to_snake_case("helloWorld") == "hello_world"
    assert to_snake_case("camelCase") == "camel_case"

def test_pascal_case_conversion():
    """Test conversion of PascalCase to snake_case"""
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("PascalCase") == "pascal_case"

def test_existing_snake_case():
    """Test that existing snake_case remains unchanged"""
    assert to_snake_case("hello_world") == "hello_world"
    assert to_snake_case("snake_case_string") == "snake_case_string"

def test_mixed_delimiters():
    """Test conversion with mixed delimiters"""
    assert to_snake_case("Hello World") == "hello_world"
    assert to_snake_case("hello-world") == "hello_world"
    assert to_snake_case("hello_World") == "hello_world"

def test_empty_string():
    """Test empty string conversion"""
    assert to_snake_case("") == ""

def test_single_word():
    """Test single word conversion"""
    assert to_snake_case("Hello") == "hello"
    assert to_snake_case("world") == "world"

def test_mixed_case_with_numbers():
    """Test conversion with numbers"""
    assert to_snake_case("hello2World") == "hello2_world"
    assert to_snake_case("Hello2World") == "hello2_world"

def test_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        to_snake_case(123)
    
    with pytest.raises(TypeError):
        to_snake_case(None)

def test_special_characters():
    """Test handling of special characters"""
    assert to_snake_case("Hello, World!") == "hello_world"
    assert to_snake_case("hello@world") == "hello_world"