import pytest
from src.header_case_converter import convert_to_header_case

def test_basic_string():
    assert convert_to_header_case("hello world") == "Hello World"

def test_snake_case():
    assert convert_to_header_case("hello_world") == "Hello World"

def test_kebab_case():
    assert convert_to_header_case("hello-world") == "Hello World"

def test_camel_case():
    assert convert_to_header_case("helloWorld") == "Hello World"
    assert convert_to_header_case("HelloWorld") == "Hello World"

def test_mixed_case():
    assert convert_to_header_case("hello_world-test") == "Hello World Test"

def test_empty_string():
    assert convert_to_header_case("") == ""

def test_single_word():
    assert convert_to_header_case("hello") == "Hello"

def test_multiple_separators():
    assert convert_to_header_case("hello__world-test") == "Hello World Test"

def test_invalid_input():
    with pytest.raises(TypeError):
        convert_to_header_case(123)
    
    with pytest.raises(TypeError):
        convert_to_header_case(None)

def test_complex_cases():
    assert convert_to_header_case("helloWorldTest") == "Hello World Test"
    assert convert_to_header_case("hello-world_test") == "Hello World Test"