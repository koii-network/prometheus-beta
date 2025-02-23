import pytest
from src.header_case_converter import convert_to_header_case

def test_basic_space_separated():
    assert convert_to_header_case("hello world") == "Hello World"

def test_snake_case():
    assert convert_to_header_case("hello_world") == "Hello World"

def test_kebab_case():
    assert convert_to_header_case("hello-world") == "Hello World"

def test_camel_case():
    assert convert_to_header_case("helloWorld") == "Hello World"
    assert convert_to_header_case("helloWorldTest") == "Hello World Test"

def test_pascal_case():
    assert convert_to_header_case("HelloWorld") == "Hello World"

def test_mixed_separators():
    assert convert_to_header_case("hello_world-test") == "Hello World Test"

def test_multiple_spaces():
    assert convert_to_header_case("hello   world  test") == "Hello World Test"

def test_error_non_string():
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_header_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_header_case(None)

def test_error_empty_string():
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_header_case("")

def test_single_word():
    assert convert_to_header_case("hello") == "Hello"

def test_already_header_case():
    assert convert_to_header_case("Hello World") == "Hello World"

def test_special_characters():
    assert convert_to_header_case("hello!world") == "Hello World"
    assert convert_to_header_case("hello@world#test") == "Hello World Test"