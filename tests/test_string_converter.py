import pytest
from src.string_converter import to_constant_case

def test_basic_string_conversion():
    assert to_constant_case("hello world") == "HELLO_WORLD"

def test_mixed_case_conversion():
    assert to_constant_case("HelloWorld") == "HELLO_WORLD"

def test_with_special_characters():
    assert to_constant_case("hello@world!123") == "HELLO_WORLD_123"

def test_with_multiple_special_characters():
    assert to_constant_case("  hello---world  ") == "HELLO_WORLD"

def test_with_numbers():
    assert to_constant_case("hello2world") == "HELLO_2_WORLD"

def test_already_uppercase():
    assert to_constant_case("HELLO_WORLD") == "HELLO_WORLD"

def test_empty_string():
    assert to_constant_case("") == ""

def test_non_string_input():
    with pytest.raises(TypeError):
        to_constant_case(123)

def test_unicode_characters():
    assert to_constant_case("hÃ©llo wÃ¶rld") == "HELLO_WORLD"