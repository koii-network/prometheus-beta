import pytest
from src.string_converter import to_dot_case

def test_basic_dot_case_conversion():
    """Test basic string conversion to dot case."""
    assert to_dot_case("hello world") == "hello.world"
    assert to_dot_case("HelloWorld") == "hello.world"
    assert to_dot_case("hello-world") == "hello.world"
    assert to_dot_case("hello_world") == "hello.world"

def test_mixed_separators():
    """Test conversion with mixed separators."""
    assert to_dot_case("hello_world-test") == "hello.world.test"
    assert to_dot_case("Hello_World-Test") == "hello.world.test"

def test_special_characters():
    """Test handling of special characters."""
    assert to_dot_case("hello@world") == "hello.world"
    assert to_dot_case("hello world!test") == "hello.world.test"
    assert to_dot_case("hello & world") == "hello.world"

def test_consecutive_separators():
    """Test handling of consecutive separators."""
    assert to_dot_case("hello___world---test") == "hello.world.test"

def test_whitespace_handling():
    """Test handling of leading and trailing whitespace."""
    assert to_dot_case("  hello world  ") == "hello.world"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_dot_case("") == ""
    assert to_dot_case("   ") == ""

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_dot_case(123)
    with pytest.raises(TypeError):
        to_dot_case(None)

def test_already_dot_case():
    """Test strings that are already in dot case."""
    assert to_dot_case("hello.world") == "hello.world"
    assert to_dot_case("hello.world.test") == "hello.world.test"