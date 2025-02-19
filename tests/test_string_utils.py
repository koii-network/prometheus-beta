import pytest
from src.string_utils import to_snake_case

def test_basic_snake_case_conversion():
    assert to_snake_case("hello world") == "hello_world"
    assert to_snake_case("HelloWorld") == "hello_world"

def test_mixed_case_conversion():
    assert to_snake_case("camelCaseString") == "camel_case_string"
    assert to_snake_case("PascalCaseString") == "pascal_case_string"

def test_special_characters():
    assert to_snake_case("Hello-World!") == "hello_world"
    assert to_snake_case("special@characters") == "special_characters"

def test_multiple_spaces_and_special_chars():
    assert to_snake_case("  multiple   spaces  ") == "multiple_spaces"
    assert to_snake_case("Multiple!!!Spaces") == "multiple_spaces"

def test_numbers_in_string():
    assert to_snake_case("hello2World") == "hello2_world"
    assert to_snake_case("123HelloWorld") == "123_hello_world"

def test_error_handling():
    with pytest.raises(TypeError):
        to_snake_case(123)
    with pytest.raises(TypeError):
        to_snake_case(None)

def test_empty_string():
    assert to_snake_case("") == ""
    assert to_snake_case(" ") == ""