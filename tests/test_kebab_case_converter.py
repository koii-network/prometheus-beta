import pytest
from src.kebab_case_converter import convert_to_kebab_case

def test_convert_to_kebab_case_camel_case():
    assert convert_to_kebab_case("helloWorld") == "hello-world"
    assert convert_to_kebab_case("camelCaseString") == "camel-case-string"
    assert convert_to_kebab_case("PascalCaseString") == "pascal-case-string"

def test_convert_to_kebab_case_snake_case():
    assert convert_to_kebab_case("hello_world") == "hello-world"
    assert convert_to_kebab_case("snake_case_string") == "snake-case-string"

def test_convert_to_kebab_case_space_separators():
    assert convert_to_kebab_case("Hello World") == "hello-world"
    assert convert_to_kebab_case("  Spaced  String  ") == "spaced-string"

def test_convert_to_kebab_case_mixed_separators():
    assert convert_to_kebab_case("Hello_World Test") == "hello-world-test"
    assert convert_to_kebab_case("camelCase_snake_PascalCase") == "camel-case-snake-pascal-case"

def test_convert_to_kebab_case_empty_string():
    assert convert_to_kebab_case("") == ""

def test_convert_to_kebab_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_kebab_case(123)
    with pytest.raises(TypeError):
        convert_to_kebab_case(None)