import pytest
from src.string_utils import convert_to_constant_case

def test_convert_to_constant_case_basic():
    """Test basic string conversion."""
    assert convert_to_constant_case("hello world") == "HELLO_WORLD"
    assert convert_to_constant_case("camelCaseString") == "CAMEL_CASE_STRING"
    assert convert_to_constant_case("snake_case_string") == "SNAKE_CASE_STRING"

def test_convert_to_constant_case_edge_cases():
    """Test edge cases."""
    assert convert_to_constant_case("") == ""
    assert convert_to_constant_case("SingleWord") == "SINGLE_WORD"
    assert convert_to_constant_case("already_CONSTANT_CASE") == "ALREADY_CONSTANT_CASE"

def test_convert_to_constant_case_special_chars():
    """Test handling of special characters."""
    assert convert_to_constant_case("hello-world") == "HELLO_WORLD"
    assert convert_to_constant_case("hello world!") == "HELLO_WORLD"
    assert convert_to_constant_case("  spaced  text  ") == "SPACED_TEXT"

def test_convert_to_constant_case_mixed_cases():
    """Test conversion of mixed case strings."""
    assert convert_to_constant_case("mixedCAMELSnake_case") == "MIXED_CAMEL_SNAKE_CASE"

def test_convert_to_constant_case_type_error():
    """Test type error handling."""
    with pytest.raises(TypeError):
        convert_to_constant_case(123)
    with pytest.raises(TypeError):
        convert_to_constant_case(None)