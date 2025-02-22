import pytest
from src.string_converter import to_snake_case

def test_to_snake_case_basic_conversions():
    assert to_snake_case("hello world") == "hello_world"
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("hello-world") == "hello_world"
    assert to_snake_case("Hello_World") == "hello_world"

def test_to_snake_case_edge_cases():
    assert to_snake_case("") == ""
    assert to_snake_case("a") == "a"
    assert to_snake_case("ABC") == "abc"

def test_to_snake_case_complex_cases():
    assert to_snake_case("snake_case") == "snake_case"
    assert to_snake_case("camelCase") == "camel_case"
    assert to_snake_case("PascalCase") == "pascal_case"
    assert to_snake_case("mixed Case-With_Separators") == "mixed_case_with_separators"

def test_to_snake_case_special_characters():
    assert to_snake_case("hello@world") == "hello_world"
    assert to_snake_case("hello world!") == "hello_world"
    assert to_snake_case("  hello  world  ") == "hello_world"

def test_to_snake_case_error_handling():
    with pytest.raises(TypeError):
        to_snake_case(123)
    with pytest.raises(TypeError):
        to_snake_case(None)
    with pytest.raises(TypeError):
        to_snake_case(["hello", "world"])