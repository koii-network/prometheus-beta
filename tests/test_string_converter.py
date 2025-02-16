import pytest
from src.string_converter import to_constant_case

def test_to_constant_case_basic():
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("Python Programming") == "PYTHON_PROGRAMMING"

def test_to_constant_case_mixed_case():
    assert to_constant_case("helloWorld") == "HELLO_WORLD"
    assert to_constant_case("HelloWorld") == "HELLO_WORLD"

def test_to_constant_case_special_chars():
    assert to_constant_case("hello-world") == "HELLO_WORLD"
    assert to_constant_case("hello_world!") == "HELLO_WORLD"
    assert to_constant_case("hello@world") == "HELLO_WORLD"

def test_to_constant_case_edge_cases():
    assert to_constant_case("") == ""
    assert to_constant_case("   ") == ""
    assert to_constant_case("a") == "A"

def test_to_constant_case_multiple_spaces():
    assert to_constant_case("hello   world") == "HELLO_WORLD"

def test_to_constant_case_invalid_input():
    with pytest.raises(TypeError):
        to_constant_case(123)
    with pytest.raises(TypeError):
        to_constant_case(None)