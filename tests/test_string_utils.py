import pytest
from src.string_utils import convert_to_dot_case

def test_convert_to_dot_case_basic():
    """Test basic string conversion to dot case."""
    assert convert_to_dot_case("hello world") == "hello.world"
    assert convert_to_dot_case("Hello World") == "hello.world"
    assert convert_to_dot_case("hello-world") == "hello.world"
    assert convert_to_dot_case("hello_world") == "hello.world"

def test_convert_to_dot_case_mixed_chars():
    """Test conversion with mixed characters."""
    assert convert_to_dot_case("Hello, World!") == "hello.world"
    assert convert_to_dot_case("Hello123World") == "hello123world"
    assert convert_to_dot_case("Hello 123 World") == "hello.123.world"

def test_convert_to_dot_case_edge_cases():
    """Test edge cases like empty string, whitespace, etc."""
    assert convert_to_dot_case("") == ""
    assert convert_to_dot_case("   ") == ""
    assert convert_to_dot_case(".hello.world.") == "hello.world"

def test_convert_to_dot_case_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_dot_case(None)
    with pytest.raises(TypeError):
        convert_to_dot_case(123)
    with pytest.raises(TypeError):
        convert_to_dot_case(["hello", "world"])

def test_convert_to_dot_case_complex_scenarios():
    """Test more complex conversion scenarios."""
    assert convert_to_dot_case("Multiple   Spaces") == "multiple.spaces"
    assert convert_to_dot_case("!@#Special$%^Chars&*()") == ""
    assert convert_to_dot_case("snake_case_to_dot_case") == "snake.case.to.dot.case"