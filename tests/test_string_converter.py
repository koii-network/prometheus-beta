import pytest
from src.string_converter import to_dot_case

def test_basic_string_conversion():
    assert to_dot_case("hello world") == "hello.world"
    assert to_dot_case("HelloWorld") == "hello.world"
    assert to_dot_case("hello_world") == "hello.world"
    assert to_dot_case("HELLO-WORLD") == "hello.world"

def test_multiple_separators():
    assert to_dot_case("hello world_test-case") == "hello.world.test.case"

def test_consecutive_separators():
    assert to_dot_case("hello   world__test--case") == "hello.world.test.case"

def test_leading_trailing_separators():
    assert to_dot_case(" hello world ") == "hello.world"
    assert to_dot_case("_hello_world_") == "hello.world"
    assert to_dot_case("-hello-world-") == "hello.world"

def test_empty_string():
    assert to_dot_case("") == ""

def test_single_word():
    assert to_dot_case("hello") == "hello"

def test_error_handling():
    with pytest.raises(TypeError):
        to_dot_case(None)
    
    with pytest.raises(TypeError):
        to_dot_case(123)
    
    with pytest.raises(TypeError):
        to_dot_case(["hello", "world"])