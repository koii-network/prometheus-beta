import pytest
from src.string_utils import convert_to_kebab_case

def test_convert_to_kebab_case():
    # Test basic space-separated string
    assert convert_to_kebab_case("hello world") == "hello-world"
    
    # Test camelCase
    assert convert_to_kebab_case("helloWorld") == "hello-world"
    assert convert_to_kebab_case("HelloWorld") == "hello-world"
    
    # Test snake_case
    assert convert_to_kebab_case("hello_world") == "hello-world"
    
    # Test mixed case with multiple words
    assert convert_to_kebab_case("HelloWorldTest") == "hello-world-test"
    
    # Test with special characters
    assert convert_to_kebab_case("Hello, World!") == "hello-world"
    
    # Test with numbers
    assert convert_to_kebab_case("hello2world") == "hello-2-world"
    
    # Test empty string
    assert convert_to_kebab_case("") == ""
    
    # Test string with multiple spaces
    assert convert_to_kebab_case("hello   world") == "hello-world"
    
    # Test error case
    with pytest.raises(TypeError):
        convert_to_kebab_case(123)
    
    # Test with leading/trailing spaces
    assert convert_to_kebab_case("  hello world  ") == "hello-world"