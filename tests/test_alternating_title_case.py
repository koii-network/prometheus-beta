import pytest
from src.alternating_title_case import convert_to_alternating_title_case

def test_convert_to_alternating_title_case_normal():
    """Test with a normal string of multiple words."""
    assert convert_to_alternating_title_case("hello world python programming") == \
           "Hello world Python programming"

def test_convert_to_alternating_title_case_single_word():
    """Test with a single word."""
    assert convert_to_alternating_title_case("hello") == "Hello"

def test_convert_to_alternating_title_case_empty_string():
    """Test with an empty string."""
    assert convert_to_alternating_title_case("") == ""

def test_convert_to_alternating_title_case_multiple_spaces():
    """Test with multiple spaces between words."""
    assert convert_to_alternating_title_case("hello   world   python") == \
           "Hello world Python"

def test_convert_to_alternating_title_case_error_handling():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError):
        convert_to_alternating_title_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_title_case(None)