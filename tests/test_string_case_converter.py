import pytest
from src.string_case_converter import to_constant_case

def test_to_constant_case_basic():
    assert to_constant_case("hello world") == "HELLO_WORLD"

def test_to_constant_case_mixed_case():
    assert to_constant_case("HelloWorld") == "HELLO_WORLD"

def test_to_constant_case_with_hyphens():
    assert to_constant_case("hello-world") == "HELLO_WORLD"

def test_to_constant_case_with_underscores():
    assert to_constant_case("hello_world") == "HELLO_WORLD"

def test_to_constant_case_multiple_separators():
    assert to_constant_case("hello   world-test_case") == "HELLO_WORLD_TEST_CASE"

def test_to_constant_case_empty_string():
    assert to_constant_case("") == ""

def test_to_constant_case_whitespace_string():
    assert to_constant_case("   ") == ""

def test_to_constant_case_already_constant_case():
    assert to_constant_case("HELLO_WORLD") == "HELLO_WORLD"

def test_to_constant_case_invalid_input():
    with pytest.raises(TypeError):
        to_constant_case(123)
    
    with pytest.raises(TypeError):
        to_constant_case(None)