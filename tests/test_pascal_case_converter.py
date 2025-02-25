import pytest
from src.pascal_case_converter import to_pascal_case

def test_basic_conversion():
    """Test basic string to Pascal case conversion."""
    assert to_pascal_case("hello world") == "HelloWorld"
    assert to_pascal_case("hello") == "Hello"

def test_different_separators():
    """Test conversion with different separators."""
    assert to_pascal_case("hello_world") == "HelloWorld"
    assert to_pascal_case("hello-world") == "HelloWorld"
    assert to_pascal_case("hello world") == "HelloWorld"

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_pascal_case("helloWorld") == "HelloWorld"
    assert to_pascal_case("HelloWorld") == "HelloWorld"

def test_multiple_separators():
    """Test conversion with multiple separators."""
    assert to_pascal_case("hello_world-test case") == "HelloWorldTestCase"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_pascal_case("") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert to_pascal_case("hello") == "Hello"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_pascal_case(123)
    
    with pytest.raises(TypeError):
        to_pascal_case(None)

def test_whitespace_handling():
    """Test handling of leading and trailing whitespace."""
    assert to_pascal_case("  hello world  ") == "HelloWorld"

def test_special_characters():
    """Test handling of special characters and numbers."""
    assert to_pascal_case("hello-world123") == "HelloWorld123"
    assert to_pascal_case("hello_world_test") == "HelloWorldTest"