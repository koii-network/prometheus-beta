import pytest
from src.string_converter import to_constant_case

def test_to_constant_case_basic():
    """Test basic string conversion to constant case."""
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("camelCaseString") == "CAMEL_CASE_STRING"
    assert to_constant_case("snake_case_string") == "SNAKE_CASE_STRING"

def test_to_constant_case_edge_cases():
    """Test edge cases of constant case conversion."""
    assert to_constant_case("") == ""
    assert to_constant_case("a") == "A"
    assert to_constant_case("A") == "A"

def test_to_constant_case_mixed_cases():
    """Test mixed case and special character scenarios."""
    assert to_constant_case("mixedCAMELCase") == "MIXED_CAMEL_CASE"
    assert to_constant_case("hello-world") == "HELLO_WORLD"
    assert to_constant_case("hello_world") == "HELLO_WORLD"
    assert to_constant_case("hello world!") == "HELLO_WORLD"

def test_to_constant_case_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        to_constant_case(123)
    
    with pytest.raises(TypeError):
        to_constant_case(None)

def test_to_constant_case_special_characters():
    """Test handling of special characters."""
    assert to_constant_case("hello@world") == "HELLO_WORLD"
    assert to_constant_case("hello world!@#") == "HELLO_WORLD"
    assert to_constant_case("!@#special chars") == "SPECIAL_CHARS"