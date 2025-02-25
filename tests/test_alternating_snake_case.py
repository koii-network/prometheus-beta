import pytest
from src.alternating_snake_case import convert_to_alternating_snake_case

def test_basic_conversion():
    """Test basic string conversion to alternating snake case."""
    assert convert_to_alternating_snake_case("hello world") == "hello_World"
    assert convert_to_alternating_snake_case("python is awesome") == "python_Is_awesome"

def test_single_word():
    """Test conversion with a single word."""
    assert convert_to_alternating_snake_case("hello") == "hello"
    assert convert_to_alternating_snake_case("HELLO") == "hello"

def test_multiple_words():
    """Test conversion with multiple words."""
    assert convert_to_alternating_snake_case("one two three four") == "one_Two_three_Four"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_snake_case("") == ""

def test_whitespace_string():
    """Test conversion of a string with only whitespace."""
    assert convert_to_alternating_snake_case("   ") == ""

def test_type_error():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_snake_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_snake_case(None)

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert convert_to_alternating_snake_case("HeLLo WoRLd") == "hello_World"