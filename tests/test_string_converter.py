import pytest
from src.string_converter import to_snake_case

def test_camel_case_conversion():
    assert to_snake_case("helloWorld") == "hello_world"
    assert to_snake_case("HelloWorld") == "hello_world"

def test_pascal_case_conversion():
    assert to_snake_case("HelloWorldExample") == "hello_world_example"

def test_kebab_case_conversion():
    assert to_snake_case("hello-world") == "hello_world"

def test_space_separated_conversion():
    assert to_snake_case("hello world") == "hello_world"
    assert to_snake_case("Hello World") == "hello_world"

def test_mixed_separators():
    assert to_snake_case("hello-world example") == "hello_world_example"
    assert to_snake_case("hello_world-example") == "hello_world_example"

def test_existing_snake_case():
    assert to_snake_case("hello_world") == "hello_world"

def test_empty_string():
    assert to_snake_case("") == ""

def test_single_word():
    assert to_snake_case("hello") == "hello"
    assert to_snake_case("Hello") == "hello"

def test_error_handling():
    with pytest.raises(TypeError):
        to_snake_case(None)
    with pytest.raises(TypeError):
        to_snake_case(123)

def test_complex_cases():
    assert to_snake_case("Hello_World-Example test") == "hello_world_example_test"
    assert to_snake_case("  Hello  World  ") == "hello_world"

def test_special_characters():
    assert to_snake_case("hello@world") == "hello_world"
    assert to_snake_case("hello world!example") == "hello_world_example"