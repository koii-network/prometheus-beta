import pytest
from src.camel_case_converter import to_camel_case

def test_basic_space_conversion():
    """Test conversion of space-separated words."""
    assert to_camel_case("hello world") == "helloWorld"

def test_hyphen_conversion():
    """Test conversion of hyphen-separated words."""
    assert to_camel_case("hello-world") == "helloWorld"

def test_underscore_conversion():
    """Test conversion of underscore-separated words."""
    assert to_camel_case("hello_world") == "helloWorld"

def test_mixed_separators():
    """Test conversion with mixed separators."""
    assert to_camel_case("hello-world_test case") == "helloWorldTestCase"

def test_single_word():
    """Test conversion of a single word."""
    assert to_camel_case("hello") == "hello"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_camel_case("") == ""

def test_multiple_spaces():
    """Test conversion with multiple spaces."""
    assert to_camel_case("hello   world  test") == "helloWorldTest"

def test_error_non_string():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_camel_case(123)
        to_camel_case(None)