import pytest
from src.string_utils import convert_to_dot_case

def test_convert_to_dot_case_basic():
    """Test basic string conversion to dot case."""
    assert convert_to_dot_case("hello world") == "hello.world"
    assert convert_to_dot_case("HelloWorld") == "hello.world"
    assert convert_to_dot_case("hello_world") == "hello.world"
    assert convert_to_dot_case("hello-world") == "hello.world"

def test_convert_to_dot_case_mixed_characters():
    """Test conversion with mixed characters and special symbols."""
    assert convert_to_dot_case("Hello, World!") == "hello.world"
    assert convert_to_dot_case("hello123world") == "hello.123.world"
    assert convert_to_dot_case("  Hello  World  ") == "hello.world"

def test_convert_to_dot_case_empty_and_whitespace():
    """Test conversion of empty and whitespace strings."""
    assert convert_to_dot_case("") == ""
    assert convert_to_dot_case("   ") == ""

def test_convert_to_dot_case_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_dot_case(None)
    
    with pytest.raises(TypeError):
        convert_to_dot_case(123)
    
    with pytest.raises(TypeError):
        convert_to_dot_case(["hello", "world"])