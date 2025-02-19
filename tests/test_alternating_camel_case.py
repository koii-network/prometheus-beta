import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string conversion to alternating camel case."""
    assert to_alternating_camel_case("hello world python") == "helloWorldpython"
    assert to_alternating_camel_case("this is a test") == "thisIsa"

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_camel_case("hello") == "hello"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_camel_case("") == ""

def test_multiple_spaces():
    """Test conversion with multiple spaces between words."""
    assert to_alternating_camel_case("hello   world   python") == "helloWorldpython"

def test_edge_cases():
    """Test various edge cases."""
    assert to_alternating_camel_case("a b c") == "aBc"
    assert to_alternating_camel_case("ONE TWO THREE") == "oneTwoThree"

def test_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        to_alternating_camel_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_camel_case(None)