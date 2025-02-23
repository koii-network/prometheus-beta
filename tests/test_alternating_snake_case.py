import pytest
from src.alternating_snake_case import convert_to_alternating_snake_case

def test_basic_conversion():
    """Test basic string conversion to alternating snake case."""
    assert convert_to_alternating_snake_case("hello world") == 'hello_WORLD'
    assert convert_to_alternating_snake_case("python is awesome") == 'python_IS_awesome'

def test_single_word():
    """Test conversion with a single word."""
    assert convert_to_alternating_snake_case("hello") == 'hello'

def test_multiple_words():
    """Test conversion with multiple words."""
    assert convert_to_alternating_snake_case("one two three four") == 'one_TWO_three_FOUR'

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert convert_to_alternating_snake_case("Hello World") == 'hello_WORLD'

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-string input
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(123)
    
    # Test empty string
    with pytest.raises(ValueError):
        convert_to_alternating_snake_case("")
    
    # Test string with only whitespace
    with pytest.raises(ValueError):
        convert_to_alternating_snake_case("   ")

def test_whitespace_handling():
    """Test handling of extra whitespace."""
    assert convert_to_alternating_snake_case("  hello   world  ") == 'hello_WORLD'