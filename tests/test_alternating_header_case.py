import pytest
from src.alternating_header_case import to_alternating_header_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert to_alternating_header_case("hello world") == "Hello wOrLd"
    assert to_alternating_header_case("python programming") == "Python pRoGrAmMiNg"

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_header_case("hello") == "Hello"
    assert to_alternating_header_case("world") == "World"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert to_alternating_header_case("this is a test") == "This iS a TeSt"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_header_case("") == ""

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_alternating_header_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_header_case(None)

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_alternating_header_case("HELLO world") == "Hello wOrLd"
    assert to_alternating_header_case("hello WORLD") == "Hello wOrLd"

def test_whitespace_handling():
    """Test handling of extra whitespace."""
    assert to_alternating_header_case("  hello   world  ") == "Hello wOrLd"