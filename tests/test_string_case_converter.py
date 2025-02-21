import pytest
from src.string_case_converter import to_kebab_case

def test_to_kebab_case_normal_string():
    assert to_kebab_case("Hello World") == "hello-world"

def test_to_kebab_case_with_special_chars():
    assert to_kebab_case("Hello, World!") == "hello-world"

def test_to_kebab_case_multiple_spaces():
    assert to_kebab_case("  Hello   World  ") == "hello-world"

def test_to_kebab_case_mixed_case():
    assert to_kebab_case("HelloWorld") == "helloworld"

def test_to_kebab_case_with_numbers():
    assert to_kebab_case("Hello 123 World") == "hello-123-world"

def test_to_kebab_case_empty_string():
    assert to_kebab_case("") == ""

def test_to_kebab_case_only_special_chars():
    assert to_kebab_case("!@#$%^&*()") == ""

def test_to_kebab_case_invalid_input():
    with pytest.raises(TypeError):
        to_kebab_case(123)
        to_kebab_case(None)