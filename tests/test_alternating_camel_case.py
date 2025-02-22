import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string conversion to alternating camel case."""
    assert to_alternating_camel_case("hello world python") == "helloWorldPython"

def test_multiple_words():
    """Test conversion with multiple words."""
    assert to_alternating_camel_case("one two three four") == "oneTwoThreeFour"

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_camel_case("hello") == "hello"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_camel_case("") == ""

def test_special_characters():
    """Test conversion with special characters."""
    assert to_alternating_camel_case("hello world! python@") == "helloWorldPython"

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_alternating_camel_case("HELLO world PYTHON") == "helloWorldPython"

def test_numeric_input():
    """Test conversion with numeric input."""
    assert to_alternating_camel_case("hello 123 world") == "hello123World"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_camel_case(123)
        to_alternating_camel_case(None)

def test_only_special_characters():
    """Test conversion with only special characters."""
    assert to_alternating_camel_case("!@#$%^") == ""