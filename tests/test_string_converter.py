import pytest
from src.string_converter import to_kebab_case

def test_camel_case_conversion():
    assert to_kebab_case("HelloWorld") == "hello-world"
    assert to_kebab_case("helloWorld") == "hello-world"

def test_snake_case_conversion():
    assert to_kebab_case("hello_world") == "hello-world"

def test_space_separated_conversion():
    assert to_kebab_case("Hello World") == "hello-world"

def test_mixed_separators_conversion():
    assert to_kebab_case("Hello_World-Test") == "hello-world-test"

def test_already_kebab_case():
    assert to_kebab_case("hello-world") == "hello-world"

def test_single_word():
    assert to_kebab_case("hello") == "hello"

def test_empty_string():
    assert to_kebab_case("") == ""

def test_multiple_spaces():
    assert to_kebab_case("Hello   World  Test") == "hello-world-test"

def test_uppercase_conversion():
    assert to_kebab_case("HELLO_WORLD") == "hello-world"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        to_kebab_case(123)
    
    with pytest.raises(TypeError):
        to_kebab_case(None)