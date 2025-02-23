import pytest
from src.string_utils import to_kebab_case

def test_camel_case_conversion():
    assert to_kebab_case("helloWorld") == "hello-world"
    assert to_kebab_case("HelloWorld") == "hello-world"
    assert to_kebab_case("camelCaseString") == "camel-case-string"

def test_snake_case_conversion():
    assert to_kebab_case("hello_world") == "hello-world"
    assert to_kebab_case("snake_case_string") == "snake-case-string"

def test_space_separated_conversion():
    assert to_kebab_case("Hello World") == "hello-world"
    assert to_kebab_case("  Spaced  String  ") == "spaced-string"

def test_mixed_case_conversion():
    assert to_kebab_case("MixedCAMELCase") == "mixed-camel-case"
    assert to_kebab_case("snake_CamelCase") == "snake-camel-case"

def test_special_characters():
    assert to_kebab_case("hello-world") == "hello-world"
    assert to_kebab_case("hello_world!") == "hello-world"
    assert to_kebab_case("hello@world#test") == "hello-world-test"

def test_empty_and_whitespace():
    assert to_kebab_case("") == ""
    assert to_kebab_case("   ") == ""

def test_numeric_strings():
    assert to_kebab_case("hello123World") == "hello-123-world"
    assert to_kebab_case("123HelloWorld") == "123-hello-world"

def test_error_handling():
    with pytest.raises(TypeError):
        to_kebab_case(None)
    with pytest.raises(TypeError):
        to_kebab_case(123)

def test_already_kebab_case():
    assert to_kebab_case("already-kebab-case") == "already-kebab-case"