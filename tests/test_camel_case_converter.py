import pytest
from src.camel_case_converter import convert_to_camel_case

def test_convert_to_camel_case():
    # Test basic space-separated string
    assert convert_to_camel_case("hello world") == "helloWorld"
    
    # Test hyphen-separated string
    assert convert_to_camel_case("Hello-World") == "helloWorld"
    
    # Test underscore-separated string
    assert convert_to_camel_case("hello_world") == "helloWorld"
    
    # Test already camel case string
    assert convert_to_camel_case("helloWorld") == "helloWorld"
    
    # Test mixed case with special characters
    assert convert_to_camel_case("Hello World!") == "helloWorld"
    assert convert_to_camel_case("hello-world_test") == "helloWorldTest"
    
    # Test empty string
    assert convert_to_camel_case("") == ""
    
    # Test single word
    assert convert_to_camel_case("hello") == "hello"
    assert convert_to_camel_case("World") == "world"

def test_convert_to_camel_case_edge_cases():
    # Test strings with multiple special characters
    assert convert_to_camel_case("hello!!!world") == "helloWorld"
    assert convert_to_camel_case("hello@#$world") == "helloWorld"
    
    # Test strings with numbers
    assert convert_to_camel_case("hello 123 world") == "hello123World"
    assert convert_to_camel_case("hello_world_2_test") == "helloWorld2Test"